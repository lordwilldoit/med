import SwiftUI

@main
struct DoseCalcApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
    }
}

struct ContentView: View {
    @AppStorage("lang") private var langRaw = Lang.fr.rawValue
    private var lang: Lang { Lang(rawValue: langRaw) ?? .fr }

    var body: some View {
        TabView {
            OnHandView(lang: lang)
                .tabItem { Label(lang.t("Comprimés", "Tablets"), systemImage: "pills") }
            WeightView(lang: lang)
                .tabItem { Label(lang.t("Poids", "Weight"), systemImage: "scalemass") }
            IVView(lang: lang)
                .tabItem { Label("IV", systemImage: "drop") }
            ConvertView(lang: lang)
                .tabItem { Label(lang.t("Conversions", "Convert"), systemImage: "arrow.left.arrow.right") }
        }
    }
}

// MARK: - Tablets / liquids

struct OnHandView: View {
    let lang: Lang
    @State private var form: DoseForm = .tablet
    @State private var ordered = ""
    @State private var orderedUnit: DoseUnit = .mg
    @State private var available = ""
    @State private var availableUnit: DoseUnit = .mg
    @State private var quantity = "1"

    var body: some View {
        CalcScreen(title: lang.t("Comprimés / liquides", "Tablets / liquids"), lang: lang) {
            Section {
                Picker(lang.t("Forme", "Form"), selection: $form) {
                    Text(lang.t("Comprimés", "Tablets")).tag(DoseForm.tablet)
                    Text(lang.t("Liquide", "Liquid")).tag(DoseForm.liquid)
                }
                .pickerStyle(.segmented)
                .onChange(of: form) { newForm in
                    quantity = newForm == .tablet ? "1" : ""
                }
            } footer: {
                Text(lang.t("(Dose prescrite ÷ Dose disponible) × Quantité", "(Dose ordered ÷ Dose on hand) × Quantity"))
            }

            Section(lang.t("Dose prescrite", "Dose ordered")) {
                NumberField(label: lang.t("Dose", "Dose"), text: $ordered)
                UnitPicker(lang: lang, selection: $orderedUnit)
            }

            Section(lang.t("Dose disponible", "Dose on hand")) {
                NumberField(label: lang.t("Teneur", "Strength"), text: $available)
                UnitPicker(lang: lang, selection: $availableUnit)
                NumberField(label: form == .tablet ? lang.t("Par", "Per") : lang.t("Dans", "In"),
                            text: $quantity,
                            suffix: form == .tablet ? lang.t("comp.", "tab") : "mL")
            }

            result
        }
    }

    @ViewBuilder private var result: some View {
        if let o = parseNumber(ordered), let a = parseNumber(available), let q = parseNumber(quantity) {
            switch Result(catching: {
                try Dose.onHand(ordered: o, orderedUnit: orderedUnit, available: a,
                                availableUnit: availableUnit, quantity: q, form: form)
            }) {
            case .success(let r):
                ResultSection(lang: lang,
                              main: mainText(r.amount),
                              steps: steps(o: o, a: a, q: q, r: r),
                              warnings: r.warnings)
            case .failure(let e):
                MessageSection(text: lang.error(e), isError: true)
            }
        } else {
            MessageSection(text: lang.t("Entre la dose prescrite et la dose disponible.", "Enter the dose ordered and the dose on hand."))
        }
    }

    private func mainText(_ amount: Double) -> String {
        if form == .liquid { return "\(lang.num(amount)) mL" }
        let word = amount > 1 ? lang.t("comprimés", "tablets") : lang.t("comprimé", "tablet")
        return "\(lang.num(amount)) \(word)"
    }

    private func steps(o: Double, a: Double, q: Double, r: Dose.OnHandResult) -> [String] {
        var s: [String] = []
        let au = lang.unitName(availableUnit)
        if orderedUnit != availableUnit {
            s.append("\(lang.num(o, decimals: 4)) \(lang.unitName(orderedUnit)) = \(lang.num(r.orderedConverted, decimals: 4)) \(au)")
        }
        let unitQ = form == .tablet ? lang.t("comp.", "tab") : "mL"
        s.append("(\(lang.num(r.orderedConverted, decimals: 4)) ÷ \(lang.num(a, decimals: 4))) × \(lang.num(q)) \(unitQ)")
        s.append("= \(mainText(r.amount))")
        return s
    }
}

// MARK: - Weight-based

struct WeightView: View {
    let lang: Lang
    @State private var weight = ""
    @State private var weightUnit: WeightUnit = .kg
    @State private var dosePerKg = ""
    @State private var doseUnit: DoseUnit = .mg
    @State private var dosesPerDay = ""
    @State private var concentration = ""
    @State private var maxDose = ""

    var body: some View {
        CalcScreen(title: lang.t("Dose selon le poids", "Weight-based dose"), lang: lang) {
            Section {
                NumberField(label: lang.t("Poids", "Weight"), text: $weight)
                Picker(lang.t("Unité de poids", "Weight unit"), selection: $weightUnit) {
                    Text("kg").tag(WeightUnit.kg)
                    Text("lb").tag(WeightUnit.lb)
                }
                .pickerStyle(.segmented)
            } header: {
                Text(lang.t("Patient", "Patient"))
            } footer: {
                Text(lang.t("Poids (kg) × Dose par kg", "Weight (kg) × Dose per kg"))
            }

            Section(lang.t("Dose prescrite par kg", "Dose ordered per kg")) {
                NumberField(label: lang.t("Dose / kg", "Dose / kg"), text: $dosePerKg)
                UnitPicker(lang: lang, selection: $doseUnit)
            }

            Section(lang.t("Optionnel", "Optional")) {
                NumberField(label: lang.t("Doses par jour", "Doses per day"), text: $dosesPerDay)
                NumberField(label: lang.t("Concentration", "Concentration"), text: $concentration,
                            suffix: "\(lang.unitName(doseUnit))/mL")
                NumberField(label: lang.t("Dose max / dose", "Max per dose"), text: $maxDose,
                            suffix: lang.unitName(doseUnit))
            }

            result
        }
    }

    @ViewBuilder private var result: some View {
        if let w = parseNumber(weight), let d = parseNumber(dosePerKg) {
            switch Result(catching: {
                try Dose.weightBased(weight: w, weightUnit: weightUnit, dosePerKg: d,
                                     dosesPerDay: parseOptional(dosesPerDay),
                                     concentrationPerML: parseOptional(concentration),
                                     maxPerDose: parseOptional(maxDose))
            }) {
            case .success(let r):
                ResultSection(lang: lang,
                              main: "\(lang.num(r.perDose)) \(u) " + lang.t("par dose", "per dose"),
                              extra: extra(r),
                              steps: steps(w: w, d: d, r: r),
                              warnings: r.warnings)
            case .failure(let e):
                MessageSection(text: lang.error(e), isError: true)
            }
        } else {
            MessageSection(text: lang.t("Entre le poids et la dose par kg.", "Enter the weight and the dose per kg."))
        }
    }

    private var u: String { lang.unitName(doseUnit) }

    private func extra(_ r: Dose.WeightResult) -> [String] {
        var e: [String] = []
        if let v = r.volumeML { e.append("= \(lang.num(v)) mL " + lang.t("par dose", "per dose")) }
        if let day = r.perDay { e.append("\(lang.num(day)) \(u) " + lang.t("par jour", "per day")) }
        return e
    }

    private func steps(w: Double, d: Double, r: Dose.WeightResult) -> [String] {
        var s: [String] = []
        if weightUnit == .lb {
            s.append("\(lang.num(w)) lb ÷ \(lang.num(2.2046, decimals: 4)) = \(lang.num(r.weightKg)) kg")
        }
        s.append("\(lang.num(r.weightKg)) kg × \(lang.num(d, decimals: 4)) \(u)/kg = \(lang.num(r.perDose)) \(u)")
        if let day = r.perDay, let n = parseOptional(dosesPerDay) {
            s.append("\(lang.num(r.perDose)) \(u) × \(lang.num(n)) = \(lang.num(day)) \(u)/" + lang.t("jour", "day"))
        }
        if let v = r.volumeML, let c = parseOptional(concentration) {
            s.append("\(lang.num(r.perDose)) \(u) ÷ \(lang.num(c, decimals: 4)) \(u)/mL = \(lang.num(v)) mL")
        }
        return s
    }
}

// MARK: - IV

struct IVView: View {
    let lang: Lang
    @State private var volume = ""
    @State private var hours = ""
    @State private var minutes = ""
    @State private var dropFactor = 0   // 0 = pump only

    var body: some View {
        CalcScreen(title: lang.t("Débit IV", "IV rate"), lang: lang) {
            Section {
                NumberField(label: lang.t("Volume", "Volume"), text: $volume, suffix: "mL")
                NumberField(label: lang.t("Durée", "Time"), text: $hours, suffix: "h")
                NumberField(label: "+", text: $minutes, suffix: "min")
            } header: {
                Text(lang.t("Perfusion", "Infusion"))
            } footer: {
                Text(lang.t("mL/h = Volume ÷ heures\ngtt/min = (Volume × facteur de goutte) ÷ minutes",
                            "mL/h = Volume ÷ hours\ngtt/min = (Volume × drop factor) ÷ minutes"))
            }

            Section(lang.t("Facteur de goutte (tubulure)", "Drop factor (tubing)")) {
                Picker(lang.t("Facteur", "Factor"), selection: $dropFactor) {
                    Text(lang.t("Pompe (mL/h seulement)", "Pump (mL/h only)")).tag(0)
                    Text("10 gtt/mL").tag(10)
                    Text("15 gtt/mL").tag(15)
                    Text("20 gtt/mL").tag(20)
                    Text("60 gtt/mL (micro)").tag(60)
                }
            }

            result
        }
    }

    private var totalMinutes: Double? {
        let h = parseOptional(hours)
        let m = parseOptional(minutes)
        if h == nil && m == nil { return nil }
        return (h ?? 0) * 60 + (m ?? 0)
    }

    @ViewBuilder private var result: some View {
        if let v = parseNumber(volume), let mins = totalMinutes {
            let factor: Double? = dropFactor == 0 ? nil : Double(dropFactor)
            switch Result(catching: { try Dose.ivRate(volumeML: v, minutes: mins, dropFactor: factor) }) {
            case .success(let r):
                ResultSection(lang: lang,
                              main: "\(lang.num(r.mlPerHour, decimals: 1)) mL/h",
                              extra: r.dropsPerMin.map { ["\($0) gtt/min"] } ?? [],
                              steps: steps(v: v, mins: mins, r: r))
            case .failure(let e):
                MessageSection(text: lang.error(e), isError: true)
            }
        } else {
            MessageSection(text: lang.t("Entre le volume et la durée.", "Enter the volume and the time."))
        }
    }

    private func steps(v: Double, mins: Double, r: Dose.IVResult) -> [String] {
        var s = ["\(lang.num(v)) mL ÷ \(lang.num(mins / 60)) h = \(lang.num(r.mlPerHour, decimals: 1)) mL/h"]
        if let exact = r.dropsPerMinExact, let rounded = r.dropsPerMin {
            s.append("(\(lang.num(v)) mL × \(dropFactor)) ÷ \(lang.num(mins)) min = \(lang.num(exact)) → \(rounded) gtt/min")
        }
        return s
    }
}

// MARK: - Conversions

struct ConvertView: View {
    let lang: Lang
    @State private var conversion: Dose.Conversion = .gToMg
    @State private var value = ""

    var body: some View {
        CalcScreen(title: lang.t("Conversions", "Conversions"), lang: lang) {
            Section {
                Picker(lang.t("Conversion", "Conversion"), selection: $conversion) {
                    ForEach(Dose.Conversion.allCases) { c in
                        Text("\(c.units.from) → \(c.units.to)").tag(c)
                    }
                }
                NumberField(label: lang.t("Valeur", "Value"), text: $value, suffix: conversion.units.from)
            }

            if let v = parseNumber(value) {
                ResultSection(lang: lang,
                              main: "\(lang.num(v, decimals: 4)) \(conversion.units.from) = \(lang.num(conversion.apply(v), decimals: 4)) \(conversion.units.to)")
            } else {
                MessageSection(text: lang.t("Entre une valeur.", "Enter a value."))
            }

            Section(lang.t("Repères", "Quick reference")) {
                Text("1 g = 1000 mg")
                Text("1 mg = 1000 mcg")
                Text("1 L = 1000 mL")
                Text("1 kg = \(lang.num(2.2)) lb")
                Text("°C = (°F − 32) × 5/9")
            }
            .font(.callout.monospaced())
        }
    }
}
