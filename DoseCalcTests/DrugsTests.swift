import XCTest
@testable import DoseCalc

final class DrugsTests: XCTestCase {

    private var drugs: [Drug] { DrugLibrary.load(bundle: Bundle(for: CustomDrugStore.self)) }

    func testLibraryLoads() {
        XCTAssertGreaterThanOrEqual(drugs.count, 80)
        XCTAssertEqual(Set(drugs.map(\.id)).count, drugs.count, "duplicate ids")
    }

    func testEveryDrugIsCompleteInBothLanguages() {
        for d in drugs {
            XCTAssertFalse(d.name.fr.isEmpty, d.id)
            XCTAssertFalse(d.name.en.isEmpty, d.id)
            XCTAssertFalse(d.drugClass.fr.isEmpty, d.id)
            XCTAssertFalse(d.why.fr.isEmpty, d.id)
            XCTAssertFalse(d.sideEffects.fr.isEmpty, d.id)
            XCTAssertEqual(d.why.fr.count, d.why.en.count, d.id)
            XCTAssertEqual(d.sideEffects.fr.count, d.sideEffects.en.count, d.id)
            XCTAssertEqual(d.watch.fr.count, d.watch.en.count, d.id)
        }
    }

    func testEveryCategoryHasDrugs() {
        for c in DrugCategory.allCases {
            XCTAssertTrue(drugs.contains { $0.category == c }, c.rawValue)
        }
    }

    func testSearchByBrandAccentsAndClass() {
        XCTAssertEqual(DrugLibrary.search(drugs, query: "lasix").first?.id, "furosemide")
        XCTAssertEqual(DrugLibrary.search(drugs, query: "  EPIVAL ").first?.id, "divalproex")
        XCTAssertTrue(DrugLibrary.search(drugs, query: "acetaminophene").contains { $0.id == "acetaminophen" })
        XCTAssertTrue(DrugLibrary.search(drugs, query: "statine").contains { $0.id == "atorvastatin" })
        XCTAssertTrue(DrugLibrary.search(drugs, query: "zzzz").isEmpty)
        XCTAssertEqual(DrugLibrary.search(drugs, query: "").count, drugs.count)
    }

    /// Every medication on the stage FADM must be findable by the name printed on it.
    func testStageFADMMedsAreSearchable() {
        let fadm = ["tazocin": "piperacillin-tazobactam", "salazopyrin": "sulfasalazine",
                    "noromby": "enoxaparin", "crestor": "rosuvastatin", "monocor": "bisoprolol",
                    "eliquis": "apixaban", "biguanide": "metformin", "ventolin": "salbutamol",
                    "combivent": "ipratropium-salbutamol", "morphine": "morphine", "atasol": "acetaminophen",
                    "ativan": "lorazepam", "deltasone": "prednisone", "glycérine": "glycerin",
                    "dulcolax": "bisacodyl", "novorapid": "insulin-rapid", "codéine": "codeine"]
        for (query, id) in fadm {
            XCTAssertTrue(DrugLibrary.search(drugs, query: query).contains { $0.id == id }, query)
        }
    }

    func testCustomDrugStorePersists() {
        let suite = "test-\(UUID().uuidString)"
        let defaults = UserDefaults(suiteName: suite)!
        defer { defaults.removePersistentDomain(forName: suite) }

        let store = CustomDrugStore(defaults: defaults)
        var d = CustomDrug()
        d.name = "Pregabaline"
        d.sideEffects = "Somnolence\n\n  Étourdissements  "
        store.save(d)

        let reloaded = CustomDrugStore(defaults: defaults)
        XCTAssertEqual(reloaded.drugs.count, 1)
        XCTAssertEqual(CustomDrug.lines(reloaded.drugs[0].sideEffects), ["Somnolence", "Étourdissements"])

        reloaded.delete(reloaded.drugs[0])
        XCTAssertTrue(CustomDrugStore(defaults: defaults).drugs.isEmpty)
    }
}
