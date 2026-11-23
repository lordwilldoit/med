import Foundation

struct LocalizedText: Codable, Hashable {
    let fr: String
    let en: String
    func text(_ lang: Lang) -> String { lang == .fr ? fr : en }
}

struct LocalizedList: Codable, Hashable {
    let fr: [String]
    let en: [String]
    func items(_ lang: Lang) -> [String] { lang == .fr ? fr : en }
}

enum DrugCategory: String, Codable, CaseIterable, Identifiable {
    case cardio, blood, endo, gi, pain, neuro, psych, resp, infection, vitamins, other
    var id: String { rawValue }

    func title(_ lang: Lang) -> String {
        switch self {
        case .cardio: return lang.t("Cœur et tension", "Heart & blood pressure")
        case .blood: return lang.t("Anticoagulants", "Blood thinners")
        case .endo: return lang.t("Diabète et hormones", "Diabetes & hormones")
        case .gi: return lang.t("Digestif", "Digestive")
        case .pain: return lang.t("Douleur", "Pain")
        case .neuro: return lang.t("Neurologie", "Neurology")
        case .psych: return lang.t("Santé mentale et sommeil", "Mental health & sleep")
        case .resp: return lang.t("Respiratoire", "Breathing")
        case .infection: return lang.t("Antibiotiques", "Antibiotics")
        case .vitamins: return lang.t("Vitamines et minéraux", "Vitamins & minerals")
        case .other: return lang.t("Autres", "Other")
        }
    }

    var icon: String {
        switch self {
        case .cardio: return "heart"
        case .blood: return "drop"
        case .endo: return "syringe"
        case .gi: return "fork.knife"
        case .pain: return "bandage"
        case .neuro: return "brain"
        case .psych: return "moon.zzz"
        case .resp: return "lungs"
        case .infection: return "allergens"
        case .vitamins: return "leaf"
        case .other: return "cross.case"
        }
    }
}

struct Drug: Codable, Identifiable, Hashable {
    let id: String
    let category: DrugCategory
    let name: LocalizedText
    let brands: [String]
    let drugClass: LocalizedText
    let why: LocalizedList
    let sideEffects: LocalizedList
    let watch: LocalizedList

    /// Lowercased text without accents, used for search in both languages.
    var searchText: String {
        ([name.fr, name.en, drugClass.fr, drugClass.en] + brands)
            .joined(separator: " ")
            .folding(options: [.diacriticInsensitive, .caseInsensitive], locale: nil)
    }
}

enum DrugLibrary {
    static func load(bundle: Bundle = .main) -> [Drug] {
        guard let url = bundle.url(forResource: "Drugs", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let drugs = try? JSONDecoder().decode([Drug].self, from: data) else { return [] }
        return drugs
    }

    static let all: [Drug] = load()

    static func search(_ drugs: [Drug], query: String) -> [Drug] {
        let q = query.trimmingCharacters(in: .whitespaces)
            .folding(options: [.diacriticInsensitive, .caseInsensitive], locale: nil)
        guard !q.isEmpty else { return drugs }
        return drugs.filter { $0.searchText.contains(q) }
    }
}

// MARK: - The user's own medications

struct CustomDrug: Codable, Identifiable, Hashable {
    var id = UUID()
    var name = ""
    var brands = ""
    var drugClass = ""
    var why = ""
    var sideEffects = ""
    var watch = ""

    var searchText: String {
        [name, brands, drugClass].joined(separator: " ")
            .folding(options: [.diacriticInsensitive, .caseInsensitive], locale: nil)
    }

    /// One item per line, ignoring blank lines.
    static func lines(_ text: String) -> [String] {
        text.split(whereSeparator: \.isNewline)
            .map { $0.trimmingCharacters(in: .whitespaces) }
            .filter { !$0.isEmpty }
    }
}

final class CustomDrugStore: ObservableObject {
    @Published private(set) var drugs: [CustomDrug] = []
    private let key = "customDrugs"
    private let defaults: UserDefaults

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        if let data = defaults.data(forKey: key),
           let saved = try? JSONDecoder().decode([CustomDrug].self, from: data) {
            drugs = saved
        }
    }

    func save(_ drug: CustomDrug) {
        if let i = drugs.firstIndex(where: { $0.id == drug.id }) {
            drugs[i] = drug
        } else {
            drugs.append(drug)
        }
        drugs.sort { $0.name.localizedCaseInsensitiveCompare($1.name) == .orderedAscending }
        persist()
    }

    func delete(_ drug: CustomDrug) {
        drugs.removeAll { $0.id == drug.id }
        persist()
    }

    private func persist() {
        if let data = try? JSONEncoder().encode(drugs) {
            defaults.set(data, forKey: key)
        }
    }
}
