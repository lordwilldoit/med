import Foundation

// MARK: - Units

enum DoseUnit: String, CaseIterable, Identifiable {
    case g, mg, mcg, units, mEq

    var id: String { rawValue }

    /// How many mg one of this unit is. nil = not a mass unit (can't be converted to mg).
    var mgFactor: Double? {
        switch self {
        case .g: return 1000
        case .mg: return 1
        case .mcg: return 0.001
        case .units, .mEq: return nil
        }
    }
}

enum WeightUnit: String, CaseIterable, Identifiable {
    case kg, lb
    var id: String { rawValue }
}

enum DoseForm: String, CaseIterable, Identifiable {
    case tablet, liquid
    var id: String { rawValue }
}

enum CalcError: Error, Equatable {
    case nonPositive
    case incompatibleUnits
}

enum CalcWarning: Equatable {
    /// More than 3 tablets for one dose — unusual, re-check the order and the strength on hand.
    case manyTablets
    /// Result is not a whole or half tablet.
    case cannotSplit
    /// Calculated dose is above the maximum the user entered.
    case aboveMax
}

// MARK: - Parsing

/// Accepts "2,5" (French) and "2.5" (English). Returns nil for empty or invalid text.
func parseNumber(_ text: String) -> Double? {
    let cleaned = text
        .trimmingCharacters(in: .whitespaces)
        .replacingOccurrences(of: " ", with: "")
        .replacingOccurrences(of: ",", with: ".")
    guard !cleaned.isEmpty, let value = Double(cleaned), value.isFinite else { return nil }
    return value
}

// MARK: - Calculations

enum Dose {

    static let lbPerKg = 2.2046226218

    /// Converts between dose units. Mass units convert to each other; units / mEq must match exactly.
    static func convert(_ value: Double, from: DoseUnit, to: DoseUnit) throws -> Double {
        if from == to { return value }
        guard let f = from.mgFactor, let t = to.mgFactor else { throw CalcError.incompatibleUnits }
        return value * f / t
    }

    static func toKg(_ weight: Double, unit: WeightUnit) -> Double {
        unit == .kg ? weight : weight / lbPerKg
    }

    // MARK: Tablets / liquids — (Dose prescrite ÷ Dose disponible) × Quantité

    struct OnHandResult: Equatable {
        /// Ordered dose expressed in the unit of the dose on hand.
        let orderedConverted: Double
        /// Tablets, or mL for liquids.
        let amount: Double
        let warnings: [CalcWarning]
    }

    static func onHand(ordered: Double, orderedUnit: DoseUnit,
                       available: Double, availableUnit: DoseUnit,
                       quantity: Double, form: DoseForm) throws -> OnHandResult {
        guard ordered > 0, available > 0, quantity > 0 else { throw CalcError.nonPositive }
        let converted = try convert(ordered, from: orderedUnit, to: availableUnit)
        let amount = converted / available * quantity

        var warnings: [CalcWarning] = []
        if form == .tablet {
            let halves = amount * 2
            if abs(halves - halves.rounded()) > 0.01 { warnings.append(.cannotSplit) }
            if amount > 3.0001 { warnings.append(.manyTablets) }
        }
        return OnHandResult(orderedConverted: converted, amount: amount, warnings: warnings)
    }

    // MARK: Weight-based — Poids (kg) × Dose par kg

    struct WeightResult: Equatable {
        let weightKg: Double
        let perDose: Double
        /// Only when doses per day was entered.
        let perDay: Double?
        /// mL to give, only when a concentration was entered.
        let volumeML: Double?
        let warnings: [CalcWarning]
    }

    static func weightBased(weight: Double, weightUnit: WeightUnit,
                            dosePerKg: Double,
                            dosesPerDay: Double? = nil,
                            concentrationPerML: Double? = nil,
                            maxPerDose: Double? = nil) throws -> WeightResult {
        guard weight > 0, dosePerKg > 0 else { throw CalcError.nonPositive }
        if let d = dosesPerDay, d <= 0 { throw CalcError.nonPositive }
        if let c = concentrationPerML, c <= 0 { throw CalcError.nonPositive }
        if let m = maxPerDose, m <= 0 { throw CalcError.nonPositive }

        let kg = toKg(weight, unit: weightUnit)
        let perDose = kg * dosePerKg
        let perDay = dosesPerDay.map { perDose * $0 }
        let volume = concentrationPerML.map { perDose / $0 }

        var warnings: [CalcWarning] = []
        if let m = maxPerDose, perDose > m + 1e-9 { warnings.append(.aboveMax) }
        return WeightResult(weightKg: kg, perDose: perDose, perDay: perDay, volumeML: volume, warnings: warnings)
    }

    // MARK: IV — mL/h = Volume ÷ heures ; gtt/min = (Volume × facteur) ÷ minutes

    struct IVResult: Equatable {
        let mlPerHour: Double
        let dropsPerMinExact: Double?
        let dropsPerMin: Int?
    }

    static func ivRate(volumeML: Double, minutes: Double, dropFactor: Double? = nil) throws -> IVResult {
        guard volumeML > 0, minutes > 0 else { throw CalcError.nonPositive }
        if let f = dropFactor, f <= 0 { throw CalcError.nonPositive }
        let mlPerHour = volumeML / (minutes / 60)
        let exact = dropFactor.map { volumeML * $0 / minutes }
        let rounded = exact.map { Int($0.rounded()) }
        return IVResult(mlPerHour: mlPerHour, dropsPerMinExact: exact, dropsPerMin: rounded)
    }

    // MARK: Conversions

    enum Conversion: String, CaseIterable, Identifiable {
        case gToMg, mgToG, mgToMcg, mcgToMg, lToMl, mlToL, lbToKg, kgToLb, fToC, cToF
        var id: String { rawValue }

        var units: (from: String, to: String) {
            switch self {
            case .gToMg: return ("g", "mg")
            case .mgToG: return ("mg", "g")
            case .mgToMcg: return ("mg", "mcg")
            case .mcgToMg: return ("mcg", "mg")
            case .lToMl: return ("L", "mL")
            case .mlToL: return ("mL", "L")
            case .lbToKg: return ("lb", "kg")
            case .kgToLb: return ("kg", "lb")
            case .fToC: return ("°F", "°C")
            case .cToF: return ("°C", "°F")
            }
        }

        func apply(_ v: Double) -> Double {
            switch self {
            case .gToMg: return v * 1000
            case .mgToG: return v / 1000
            case .mgToMcg: return v * 1000
            case .mcgToMg: return v / 1000
            case .lToMl: return v * 1000
            case .mlToL: return v / 1000
            case .lbToKg: return v / Dose.lbPerKg
            case .kgToLb: return v * Dose.lbPerKg
            case .fToC: return (v - 32) * 5 / 9
            case .cToF: return v * 9 / 5 + 32
            }
        }
    }
}
