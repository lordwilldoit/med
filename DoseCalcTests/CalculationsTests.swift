import XCTest
@testable import DoseCalc

final class CalculationsTests: XCTestCase {

    // MARK: Parsing

    func testParseNumber() {
        XCTAssertEqual(parseNumber("2,5"), 2.5)
        XCTAssertEqual(parseNumber(" 2.5 "), 2.5)
        XCTAssertEqual(parseNumber("1 000"), 1000)
        XCTAssertNil(parseNumber(""))
        XCTAssertNil(parseNumber("abc"))
        XCTAssertNil(parseNumber("2,5,1"))
    }

    // MARK: Conversion

    func testUnitConversion() throws {
        XCTAssertEqual(try Dose.convert(0.5, from: .g, to: .mg), 500, accuracy: 1e-9)
        XCTAssertEqual(try Dose.convert(250, from: .mcg, to: .mg), 0.25, accuracy: 1e-9)
        XCTAssertEqual(try Dose.convert(5000, from: .units, to: .units), 5000)
        XCTAssertThrowsError(try Dose.convert(10, from: .units, to: .mg)) {
            XCTAssertEqual($0 as? CalcError, .incompatibleUnits)
        }
    }

    // MARK: Tablets / liquids

    func testTwoTablets() throws {
        let r = try Dose.onHand(ordered: 500, orderedUnit: .mg, available: 250, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.amount, 2, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [])
    }

    func testGramsOrderedMgOnHand() throws {
        let r = try Dose.onHand(ordered: 0.5, orderedUnit: .g, available: 250, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.orderedConverted, 500, accuracy: 1e-9)
        XCTAssertEqual(r.amount, 2, accuracy: 1e-9)
    }

    func testMcgOrderedMgOnHand() throws {
        // Levothyroxine-style: 75 mcg ordered, 0.025 mg tablets → 3 tablets
        let r = try Dose.onHand(ordered: 75, orderedUnit: .mcg, available: 0.025, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.amount, 3, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [])
    }

    func testLiquid() throws {
        // 125 mg ordered, 250 mg / 5 mL → 2.5 mL
        let r = try Dose.onHand(ordered: 125, orderedUnit: .mg, available: 250, availableUnit: .mg, quantity: 5, form: .liquid)
        XCTAssertEqual(r.amount, 2.5, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [])
    }

    func testHalfTabletIsFine() throws {
        let r = try Dose.onHand(ordered: 375, orderedUnit: .mg, available: 250, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.amount, 1.5, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [])
    }

    func testCannotSplitWarning() throws {
        let r = try Dose.onHand(ordered: 300, orderedUnit: .mg, available: 250, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.amount, 1.2, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [.cannotSplit])
    }

    func testManyTabletsWarning() throws {
        let r = try Dose.onHand(ordered: 1, orderedUnit: .g, available: 250, availableUnit: .mg, quantity: 1, form: .tablet)
        XCTAssertEqual(r.amount, 4, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [.manyTablets])
    }

    func testUnitsHeparinStyle() throws {
        // 5000 units ordered, 10 000 units / mL → 0.5 mL
        let r = try Dose.onHand(ordered: 5000, orderedUnit: .units, available: 10000, availableUnit: .units, quantity: 1, form: .liquid)
        XCTAssertEqual(r.amount, 0.5, accuracy: 1e-9)
    }

    func testOnHandRejectsBadInput() {
        XCTAssertThrowsError(try Dose.onHand(ordered: 0, orderedUnit: .mg, available: 250, availableUnit: .mg, quantity: 1, form: .tablet))
        XCTAssertThrowsError(try Dose.onHand(ordered: 10, orderedUnit: .units, available: 250, availableUnit: .mg, quantity: 1, form: .tablet))
    }

    // MARK: Weight-based

    func testWeightBasedKg() throws {
        let r = try Dose.weightBased(weight: 20, weightUnit: .kg, dosePerKg: 10, dosesPerDay: 4, concentrationPerML: 40, maxPerDose: 300)
        XCTAssertEqual(r.perDose, 200, accuracy: 1e-9)
        XCTAssertEqual(r.perDay!, 800, accuracy: 1e-9)
        XCTAssertEqual(r.volumeML!, 5, accuracy: 1e-9)
        XCTAssertEqual(r.warnings, [])
    }

    func testWeightBasedPounds() throws {
        let r = try Dose.weightBased(weight: 44.092452436, weightUnit: .lb, dosePerKg: 10)
        XCTAssertEqual(r.weightKg, 20, accuracy: 1e-6)
        XCTAssertEqual(r.perDose, 200, accuracy: 1e-5)
        XCTAssertNil(r.perDay)
        XCTAssertNil(r.volumeML)
    }

    func testAboveMaxWarning() throws {
        let r = try Dose.weightBased(weight: 20, weightUnit: .kg, dosePerKg: 10, maxPerDose: 150)
        XCTAssertEqual(r.warnings, [.aboveMax])
    }

    // MARK: IV

    func testIVPump() throws {
        let r = try Dose.ivRate(volumeML: 1000, minutes: 480)
        XCTAssertEqual(r.mlPerHour, 125, accuracy: 1e-9)
        XCTAssertNil(r.dropsPerMin)
    }

    func testIVDrops() throws {
        let r = try Dose.ivRate(volumeML: 1000, minutes: 480, dropFactor: 15)
        XCTAssertEqual(r.dropsPerMinExact!, 31.25, accuracy: 1e-9)
        XCTAssertEqual(r.dropsPerMin, 31)

        let r2 = try Dose.ivRate(volumeML: 100, minutes: 30, dropFactor: 20)
        XCTAssertEqual(r2.mlPerHour, 200, accuracy: 1e-9)
        XCTAssertEqual(r2.dropsPerMin, 67)
    }

    // MARK: Conversions

    func testConversions() {
        XCTAssertEqual(Dose.Conversion.gToMg.apply(1.5), 1500, accuracy: 1e-9)
        XCTAssertEqual(Dose.Conversion.mcgToMg.apply(125), 0.125, accuracy: 1e-9)
        XCTAssertEqual(Dose.Conversion.lbToKg.apply(154), 69.853, accuracy: 0.001)
        XCTAssertEqual(Dose.Conversion.fToC.apply(98.6), 37, accuracy: 1e-9)
        XCTAssertEqual(Dose.Conversion.cToF.apply(38.5), 101.3, accuracy: 1e-9)
    }
}
