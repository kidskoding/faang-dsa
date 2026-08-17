# Internal Tooling Warm-Up

Prep for an Astranis Enterprise Systems live Python round. The reported shape is
practical data work rather than abstract algorithms: parsing messy exports,
aggregating them, and keeping running state as records stream in.

## The Scenario

Two systems disagree about satellite parts inventory. Procurement exports a
dirty CSV — inconsistent casing, blank fields, quantities stored as strings.
Assembly reports what it actually consumed. You are writing the internal tool
that reconciles them and flags shortages.

Nothing here may raise on bad input. An internal tool that dies on one malformed
row wakes somebody up at 2am.

## The Exercises

Work in `internal_tooling_problems.py`, in order — each is a plausible follow-up
once the previous part works.

1. **`clean_records`** — normalize the export. Uppercase part ids, coerce
   quantities to int with 0 as the fallback, default the category, drop rows
   with no usable id.
2. **`total_by_category`** — sum quantity per category.
3. **`reconcile`** — outer-join the two sources by part id, with a delta. A part
   missing from one side counts as 0 there.
4. **`top_shortages`** — the n parts where assembly consumed more than
   procurement recorded.
5. **`InventoryTracker`** — running state as receipts and withdrawals stream in,
   with a low-stock query. Stock never goes negative.

```bash
uv run pytest other/problem_sets/03_internal_tooling -q
```

## What They Are Watching For

Ask about the **data**, not the algorithm. Can fields be missing? Can a part id
repeat within one export? What should happen when the two sources conflict —
trust one, take the max, or flag it? Those questions are the instinct this team
hires for, and they are more useful than reaching for a clever data structure.

Then: reach for `defaultdict` and `Counter` rather than hand-rolled key checks,
name intermediate values instead of chaining comprehensions three deep, and say
out loud what happens on empty input before you are asked.

## Related Drills Already In The Repo

| Skill                             | Where                           |
| --------------------------------- | ------------------------------- |
| Moving average over a stream      | `MovingAverage`, module 03      |
| Time-based event window           | `RecentCounter`, module 03      |
| Rolling max with a deque          | `max_sliding_window`, module 04 |
| Grouping records by a derived key | `group_anagrams`, module 01     |
| Aggregate then rank               | `top_k_frequent`, module 01     |
| State object with corrections     | `StockPrice`, module 18         |
