import SwiftUI
import UIKit

func hideKeyboard() {
    UIApplication.shared.sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
}

/// Optional field: empty → nil.
func parseOptional(_ text: String) -> Double? {
    text.trimmingCharacters(in: .whitespaces).isEmpty ? nil : parseNumber(text)
}

struct LangPicker: View {
    @AppStorage("lang") private var langRaw = Lang.fr.rawValue

    var body: some View {
        Picker("Langue / Language", selection: $langRaw) {
            Text("FR").tag(Lang.fr.rawValue)
            Text("EN").tag(Lang.en.rawValue)
        }
        .pickerStyle(.segmented)
        .frame(width: 100)
    }
}

/// Shared screen: navigation title, language toggle, keyboard "OK" button, disclaimer.
struct CalcScreen<Content: View>: View {
    let title: String
    let lang: Lang
    @ViewBuilder var content: Content

    var body: some View {
        NavigationStack {
            Form {
                content
                Section {
                    Text(lang.t("Outil d'aide au calcul pour l'étude et la vérification. Vérifie toujours avec l'ordonnance, le protocole de l'établissement et ton infirmière ou ton enseignante avant d'administrer.",
                                "A calculation aid for study and double-checking. Always verify against the order, your facility's protocol and your nurse or instructor before giving any medication."))
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }
            .scrollDismissesKeyboard(.interactively)
            .navigationTitle(title)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) { LangPicker() }
                ToolbarItemGroup(placement: .keyboard) {
                    Spacer()
                    Button(lang.t("OK", "Done")) { hideKeyboard() }
                }
            }
        }
    }
}

struct NumberField: View {
    let label: String
    @Binding var text: String
    var suffix: String? = nil

    var body: some View {
        HStack {
            Text(label)
            Spacer()
            TextField("0", text: $text)
                .keyboardType(.decimalPad)
                .multilineTextAlignment(.trailing)
                .frame(maxWidth: 130)
            if let suffix {
                Text(suffix).foregroundStyle(.secondary)
            }
        }
    }
}

struct UnitPicker: View {
    let lang: Lang
    @Binding var selection: DoseUnit

    var body: some View {
        Picker(lang.t("Unité", "Unit"), selection: $selection) {
            ForEach(DoseUnit.allCases) { u in
                Text(lang.unitName(u)).tag(u)
            }
        }
    }
}

struct ResultSection: View {
    let lang: Lang
    let main: String
    var extra: [String] = []
    var steps: [String] = []
    var warnings: [CalcWarning] = []

    var body: some View {
        Section(lang.t("Résultat", "Result")) {
            Text(main)
                .font(.title2.bold())
                .foregroundStyle(.tint)
            ForEach(extra.indices, id: \.self) { i in
                Text(extra[i]).font(.headline)
            }
            if !steps.isEmpty {
                VStack(alignment: .leading, spacing: 4) {
                    Text(lang.t("Calcul", "Working")).font(.caption.bold()).foregroundStyle(.secondary)
                    ForEach(steps.indices, id: \.self) { i in
                        Text(steps[i])
                            .font(.callout.monospaced())
                            .foregroundStyle(.secondary)
                    }
                }
            }
            ForEach(warnings.indices, id: \.self) { i in
                Label(lang.warning(warnings[i]), systemImage: "exclamationmark.triangle.fill")
                    .foregroundStyle(.orange)
            }
        }
    }
}

struct MessageSection: View {
    let text: String
    var isError = false

    var body: some View {
        Section {
            if isError {
                Label(text, systemImage: "xmark.octagon.fill").foregroundStyle(.red)
            } else {
                Text(text).foregroundStyle(.secondary)
            }
        }
    }
}
