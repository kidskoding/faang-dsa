from internal_tooling_problems import (
    InventoryTracker,
    clean_records,
    reconcile,
    top_shortages,
    total_by_category,
)

MESSY = [
    {"part_id": " tx-100 ", "qty": "5", "category": "RF"},
    {"part_id": "TX-100", "qty": 3, "category": "rf"},
    {"part_id": "pw-200", "qty": "", "category": "Power"},
    {"part_id": "PW-201", "qty": "12", "category": None},
    {"part_id": "", "qty": "9", "category": "RF"},
    {"part_id": "st-300", "qty": "not-a-number", "category": "Structure"},
]


def test_clean_records_normalizes_fields():
    cleaned = clean_records(MESSY)

    assert cleaned[0] == {"part_id": "TX-100", "qty": 5, "category": "rf"}
    assert cleaned[1] == {"part_id": "TX-100", "qty": 3, "category": "rf"}


def test_clean_records_drops_rows_without_a_part_id():
    assert all(row["part_id"] for row in clean_records(MESSY))
    assert len(clean_records(MESSY)) == 5


def test_clean_records_defaults_bad_quantities_to_zero():
    by_id = {row["part_id"]: row for row in clean_records(MESSY)}

    assert by_id["PW-200"]["qty"] == 0
    assert by_id["ST-300"]["qty"] == 0


def test_clean_records_defaults_missing_category():
    by_id = {row["part_id"]: row for row in clean_records(MESSY)}

    assert by_id["PW-201"]["category"] == "uncategorized"


def test_clean_records_empty_input():
    assert clean_records([]) == []


def test_clean_records_tolerates_missing_keys():
    assert clean_records([{"part_id": "a-1"}]) == [
        {"part_id": "A-1", "qty": 0, "category": "uncategorized"}
    ]


def test_total_by_category_sums_each_group():
    totals = total_by_category(clean_records(MESSY))

    assert totals["rf"] == 8
    assert totals["power"] == 0
    assert totals["uncategorized"] == 12


def test_total_by_category_empty_input():
    assert total_by_category([]) == {}


PROCUREMENT = [
    {"part_id": "TX-100", "qty": 10},
    {"part_id": "PW-200", "qty": 4},
    {"part_id": "ST-300", "qty": 7},
]
ASSEMBLY = [
    {"part_id": "TX-100", "qty": 12},
    {"part_id": "ST-300", "qty": 7},
    {"part_id": "AN-400", "qty": 3},
]


def test_reconcile_covers_both_sources_sorted():
    rows = reconcile(PROCUREMENT, ASSEMBLY)

    assert [r["part_id"] for r in rows] == ["AN-400", "PW-200", "ST-300", "TX-100"]


def test_reconcile_computes_delta():
    by_id = {r["part_id"]: r for r in reconcile(PROCUREMENT, ASSEMBLY)}

    assert by_id["TX-100"] == {
        "part_id": "TX-100",
        "procurement_qty": 10,
        "assembly_qty": 12,
        "delta": -2,
    }
    assert by_id["ST-300"]["delta"] == 0


def test_reconcile_treats_missing_side_as_zero():
    by_id = {r["part_id"]: r for r in reconcile(PROCUREMENT, ASSEMBLY)}

    assert by_id["AN-400"]["procurement_qty"] == 0
    assert by_id["PW-200"]["assembly_qty"] == 0


def test_reconcile_both_empty():
    assert reconcile([], []) == []


def test_top_shortages_most_negative_first():
    rows = reconcile(PROCUREMENT, ASSEMBLY)

    assert top_shortages(rows, 2) == ["AN-400", "TX-100"]


def test_top_shortages_excludes_non_shortages():
    rows = reconcile(PROCUREMENT, ASSEMBLY)

    assert "ST-300" not in top_shortages(rows, 10)
    assert "PW-200" not in top_shortages(rows, 10)


def test_top_shortages_handles_n_larger_than_available():
    rows = reconcile(PROCUREMENT, ASSEMBLY)

    assert len(top_shortages(rows, 99)) == 2


def test_inventory_tracker_receive_and_withdraw():
    tracker = InventoryTracker()

    assert tracker.receive("TX-100", 10) == 10
    assert tracker.receive("TX-100", 5) == 15
    assert tracker.withdraw("TX-100", 4) == 11


def test_inventory_tracker_never_goes_negative():
    tracker = InventoryTracker()
    tracker.receive("PW-200", 3)

    assert tracker.withdraw("PW-200", 10) == 0
    assert tracker.on_hand("PW-200") == 0


def test_inventory_tracker_unknown_part_is_zero():
    assert InventoryTracker().on_hand("NOPE-1") == 0


def test_inventory_tracker_withdraw_unknown_part():
    assert InventoryTracker().withdraw("NOPE-1", 5) == 0


def test_inventory_tracker_low_stock_sorted():
    tracker = InventoryTracker()
    tracker.receive("TX-100", 10)
    tracker.receive("PW-200", 2)
    tracker.receive("ST-300", 5)
    tracker.receive("AN-400", 2)

    assert tracker.low_stock(5) == ["AN-400", "PW-200", "ST-300"]


def test_inventory_tracker_low_stock_includes_depleted_parts():
    tracker = InventoryTracker()
    tracker.receive("TX-100", 4)
    tracker.withdraw("TX-100", 4)

    assert tracker.low_stock(0) == ["TX-100"]
