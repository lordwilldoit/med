import Foundation

enum Lang: String, CaseIterable, Identifiable {
    case fr, en
    var id: String { rawValue }

    /// Pick the French or English text.
    func t(_ fr: String, _ en: String) -> String { self == .fr ? fr : en }

    var locale: Locale { Locale(identifier: self == .fr ? "fr_CA" : "en_CA") }

    /// Formats with up to `decimals` decimals, using a comma in French.
    func num(_ value: Double, decimals: Int = 2) -> String {
        let f = NumberFormatter()
        f.locale = locale
        f.numberStyle = .decimal
        f.minimumFractionDigits = 0
        f.maximumFractionDigits = decimals
        return f.string(from: NSNumber(value: value)) ?? String(value)
    }

    func unitName(_ u: DoseUnit) -> String {
        switch u {
        case .g: return "g"
        case .mg: return "mg"
        case .mcg: return "mcg"
        case .units: return t("unités", "units")
        case .mEq: return "mEq"
        }
    }

    func warning(_ w: CalcWarning) -> String {
        switch w {
        case .manyTablets:
            return t("Plus de 3 comprimés pour une dose : c'est inhabituel. Revérifie l'ordonnance et la teneur disponible.",
                     "More than 3 tablets for one dose is unusual. Re-check the order and the strength on hand.")
        case .cannotSplit:
            return t("Ce n'est pas un comprimé entier ou un demi. Revérifie le calcul et si le comprimé peut être coupé.",
                     "This isn't a whole or half tablet. Re-check the math and whether the tablet can be split.")
        case .aboveMax:
            return t("La dose calculée dépasse la dose maximale entrée.",
                     "The calculated dose is above the maximum you entered.")
        }
    }

    func error(_ e: Error) -> String {
        switch e as? CalcError {
        case .incompatibleUnits:
            return t("Unités incompatibles : les unités et mEq ne se convertissent pas en mg.",
                     "Incompatible units: units and mEq can't be converted to mg.")
        default:
            return t("Les valeurs doivent être plus grandes que 0.", "Values must be greater than 0.")
        }
    }
}
