# Internal tooling warm-up: messy records in, clean aggregates out.
# Scenario in INTERNAL_TOOLING_PROBLEM_SET.md.
#
# Two systems disagree about satellite parts inventory. The procurement export
# is dirty: inconsistent casing, blank fields, quantities stored as strings.
# Nothing here should raise on bad input — internal tools that crash on one bad
# row wake somebody up.


def clean_records(rows: list[dict]) -> list[dict]:
    # Normalize the procurement export.
    #   part_id   -> uppercase, whitespace stripped
    #   qty       -> int; missing, blank, or unparseable becomes 0
    #   category  -> lowercase, missing becomes "uncategorized"
    # Drop rows with no usable part_id. Never raise.

    raise NotImplementedError


def total_by_category(rows: list[dict]) -> dict[str, int]:
    # Sum qty per category over already-cleaned rows.

    raise NotImplementedError


def reconcile(procurement: list[dict], assembly: list[dict]) -> list[dict]:
    # Two sources, keyed by part_id. Return one row per part id seen in either,
    # sorted by part_id, shaped:
    #   {"part_id", "procurement_qty", "assembly_qty", "delta"}
    # A part missing from a source counts as 0 there. delta is procurement minus
    # assembly.

    raise NotImplementedError


def top_shortages(reconciled: list[dict], n: int) -> list[str]:
    # The n part_ids with the most negative delta — assembly used more than
    # procurement recorded. Most negative first, ties broken by part_id.
    # Parts that are not short are excluded.

    raise NotImplementedError


class InventoryTracker:
    # Running state as receipts and withdrawals stream in.

    def __init__(self) -> None:
        raise NotImplementedError

    def receive(self, part_id: str, qty: int) -> int:
        # Add stock, return the new on-hand count.
        raise NotImplementedError

    def withdraw(self, part_id: str, qty: int) -> int:
        # Remove stock, return the new on-hand count. Never let it go negative:
        # withdraw only what is on hand.
        raise NotImplementedError

    def on_hand(self, part_id: str) -> int:
        # Unknown parts are 0, not an error.
        raise NotImplementedError

    def low_stock(self, threshold: int) -> list[str]:
        # Part ids at or below threshold, sorted by count then part_id.
        # Parts that have been seen but are now at 0 still count.
        raise NotImplementedError
