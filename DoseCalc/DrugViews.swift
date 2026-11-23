import SwiftUI

// MARK: - List

struct DrugListView: View {
    let lang: Lang
    @StateObject private var store = CustomDrugStore()
    @State private var query = ""
    @State private var category: DrugCategory? = nil
    @State private var editing: CustomDrug? = nil

    private var filtered: [Drug] {
        let base = category.map { c in DrugLibrary.all.filter { $0.category == c } } ?? DrugLibrary.all
        return DrugLibrary.search(base, query: query)
            .sorted { $0.name.text(lang).localizedCaseInsensitiveCompare($1.name.text(lang)) == .orderedAscending }
    }

    private var filteredCustom: [CustomDrug] {
        let q = query.trimmingCharacters(in: .whitespaces)
            .folding(options: [.diacriticInsensitive, .caseInsensitive], locale: nil)
        guard category == nil else { return [] }
        return q.isEmpty ? store.drugs : store.drugs.filter { $0.searchText.contains(q) }
    }

    var body: some View {
        NavigationStack {
            List {
                if category == nil {
                    Section(lang.t("Mes médicaments", "My medications")) {
                        ForEach(filteredCustom) { d in
                            NavigationLink(value: d) {
                                DrugRow(name: d.name, subtitle: d.drugClass, icon: "person.crop.circle")
                            }
                        }
                        if query.isEmpty {
                            Button {
                                editing = CustomDrug()
                            } label: {
                                Label(lang.t("Ajouter un médicament", "Add a medication"), systemImage: "plus.circle.fill")
                            }
                        }
                    }
                }

                if !query.isEmpty || category != nil {
                    Section {
                        ForEach(filtered) { d in
                            NavigationLink(value: d) { row(d) }
                        }
                    }
                    if filtered.isEmpty && filteredCustom.isEmpty {
                        Text(lang.t("Aucun résultat. Tu peux l'ajouter dans « Mes médicaments ».",
                                    "No results. You can add it under \"My medications\"."))
                            .foregroundStyle(.secondary)
                    }
                } else {
                    ForEach(DrugCategory.allCases) { c in
                        let drugs = filtered.filter { $0.category == c }
                        if !drugs.isEmpty {
                            Section(c.title(lang)) {
                                ForEach(drugs) { d in
                                    NavigationLink(value: d) { row(d) }
                                }
                            }
                        }
                    }
                }

                Section {
                    Text(lang.t("Résumé pour l'étude. Vérifie toujours avec la FADM, le pharmacien ou une monographie (ex. Vigilance Santé, CPS) avant d'administrer.",
                                "Study summary. Always check the MAR, the pharmacist or a drug monograph (e.g. Vigilance, CPS) before giving any medication."))
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }
            .searchable(text: $query, prompt: lang.t("Nom, marque ou classe", "Name, brand or class"))
            .autocorrectionDisabled()
            .navigationTitle(lang.t("Médicaments", "Medications"))
            .navigationDestination(for: Drug.self) { DrugDetailView(drug: $0, lang: lang) }
            .navigationDestination(for: CustomDrug.self) { d in
                CustomDrugDetailView(drugID: d.id, store: store, lang: lang)
            }
            .toolbar {
                ToolbarItem(placement: .navigationBarLeading) { categoryMenu }
                ToolbarItem(placement: .navigationBarTrailing) { LangPicker() }
            }
            .sheet(item: $editing) { d in
                CustomDrugForm(drug: d, store: store, lang: lang)
            }
        }
    }

    private func row(_ d: Drug) -> some View {
        DrugRow(name: d.name.text(lang),
                subtitle: d.brands.isEmpty ? d.drugClass.text(lang) : d.brands.joined(separator: ", "),
                icon: d.category.icon)
    }

    private var categoryMenu: some View {
        Menu {
            Button {
                category = nil
            } label: {
                if category == nil { Label(lang.t("Toutes", "All"), systemImage: "checkmark") } else { Text(lang.t("Toutes", "All")) }
            }
            ForEach(DrugCategory.allCases) { c in
                Button {
                    category = c
                } label: {
                    if category == c { Label(c.title(lang), systemImage: "checkmark") } else { Text(c.title(lang)) }
                }
            }
        } label: {
            Image(systemName: category == nil ? "line.3.horizontal.decrease.circle" : "line.3.horizontal.decrease.circle.fill")
        }
    }
}

struct DrugRow: View {
    let name: String
    let subtitle: String
    let icon: String

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: icon)
                .foregroundStyle(.tint)
                .frame(width: 24)
            VStack(alignment: .leading, spacing: 2) {
                Text(name).font(.body.weight(.medium))
                if !subtitle.isEmpty {
                    Text(subtitle).font(.caption).foregroundStyle(.secondary).lineLimit(1)
                }
            }
        }
    }
}

// MARK: - Detail

struct DrugInfoSections: View {
    let lang: Lang
    let name: String
    let brands: String
    let drugClass: String
    let why: [String]
    let sideEffects: [String]
    let watch: [String]

    var body: some View {
        Section {
            VStack(alignment: .leading, spacing: 4) {
                Text(name).font(.title2.bold())
                if !brands.isEmpty {
                    Text(brands).foregroundStyle(.secondary)
                }
            }
            .padding(.vertical, 4)
        }
        if !drugClass.isEmpty {
            Section(lang.t("Classe", "Class")) {
                Text(drugClass)
            }
        }
        bullets(lang.t("Pourquoi on le donne", "Why it's given"), why, icon: "checkmark.circle", color: .green)
        bullets(lang.t("Effets secondaires", "Side effects"), sideEffects, icon: "exclamationmark.circle", color: .orange)
        bullets(lang.t("À surveiller", "What to watch"), watch, icon: "eye", color: .blue)
    }

    @ViewBuilder
    private func bullets(_ title: String, _ items: [String], icon: String, color: Color) -> some View {
        if !items.isEmpty {
            Section(title) {
                ForEach(items.indices, id: \.self) { i in
                    Label {
                        Text(items[i])
                    } icon: {
                        Image(systemName: icon).foregroundStyle(color)
                    }
                }
            }
        }
    }
}

struct DrugDetailView: View {
    let drug: Drug
    let lang: Lang

    var body: some View {
        List {
            DrugInfoSections(lang: lang,
                             name: drug.name.text(lang),
                             brands: drug.brands.joined(separator: " · "),
                             drugClass: drug.drugClass.text(lang),
                             why: drug.why.items(lang),
                             sideEffects: drug.sideEffects.items(lang),
                             watch: drug.watch.items(lang))
            Section {
                Text(lang.t("Résumé des effets les plus courants ou importants, pas une liste complète. Vérifie avec la FADM et le pharmacien.",
                            "Summary of the most common or important effects, not a complete list. Check the MAR and the pharmacist."))
                    .font(.footnote)
                    .foregroundStyle(.secondary)
            }
        }
        .navigationTitle(drug.name.text(lang))
        .navigationBarTitleDisplayMode(.inline)
        .toolbar { ToolbarItem(placement: .navigationBarTrailing) { LangPicker() } }
    }
}

struct CustomDrugDetailView: View {
    let drugID: UUID
    @ObservedObject var store: CustomDrugStore
    let lang: Lang
    @State private var editing: CustomDrug? = nil
    @State private var confirmDelete = false
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Group {
            if let d = store.drugs.first(where: { $0.id == drugID }) {
                List {
                    DrugInfoSections(lang: lang,
                                     name: d.name,
                                     brands: d.brands,
                                     drugClass: d.drugClass,
                                     why: CustomDrug.lines(d.why),
                                     sideEffects: CustomDrug.lines(d.sideEffects),
                                     watch: CustomDrug.lines(d.watch))
                    Section {
                        Button(lang.t("Supprimer", "Delete"), role: .destructive) { confirmDelete = true }
                    }
                }
                .navigationTitle(d.name)
                .navigationBarTitleDisplayMode(.inline)
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button(lang.t("Modifier", "Edit")) { editing = d }
                    }
                }
                .sheet(item: $editing) { CustomDrugForm(drug: $0, store: store, lang: lang) }
                .confirmationDialog(lang.t("Supprimer ce médicament?", "Delete this medication?"),
                                    isPresented: $confirmDelete, titleVisibility: .visible) {
                    Button(lang.t("Supprimer", "Delete"), role: .destructive) {
                        store.delete(d)
                        dismiss()
                    }
                }
            } else {
                Text(lang.t("Médicament supprimé.", "Medication deleted.")).foregroundStyle(.secondary)
            }
        }
    }
}

// MARK: - Add / edit form

struct CustomDrugForm: View {
    @State var drug: CustomDrug
    @ObservedObject var store: CustomDrugStore
    let lang: Lang
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            Form {
                Section(lang.t("Nom", "Name")) {
                    TextField(lang.t("Nom générique", "Generic name"), text: $drug.name)
                    TextField(lang.t("Noms commerciaux", "Brand names"), text: $drug.brands)
                    TextField(lang.t("Classe", "Class"), text: $drug.drugClass)
                }
                multiline(lang.t("Pourquoi on le donne", "Why it's given"), $drug.why)
                multiline(lang.t("Effets secondaires", "Side effects"), $drug.sideEffects)
                multiline(lang.t("À surveiller", "What to watch"), $drug.watch)
            }
            .navigationTitle(lang.t("Mon médicament", "My medication"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(lang.t("Annuler", "Cancel")) { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button(lang.t("Enregistrer", "Save")) {
                        drug.name = drug.name.trimmingCharacters(in: .whitespaces)
                        store.save(drug)
                        dismiss()
                    }
                    .disabled(drug.name.trimmingCharacters(in: .whitespaces).isEmpty)
                }
            }
        }
    }

    private func multiline(_ title: String, _ text: Binding<String>) -> some View {
        Section {
            TextField(title, text: text, axis: .vertical)
                .lineLimit(3...10)
        } header: {
            Text(title)
        } footer: {
            Text(lang.t("Un élément par ligne.", "One item per line."))
        }
    }
}
