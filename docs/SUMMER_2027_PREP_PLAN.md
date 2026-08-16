# Summer 2027 Internship Prep Plan

Written 2026-08-16. Target: big tech summer 2027 SWE internship interviews,
first OAs expected mid-September onward.

## The Budget

15–20 hours a week from 2026-08-17 through 2026-10-04 is roughly 120 hours.
A medium done properly — attempt cold, get stuck, work through it, write the
complexity, say the approach out loud — runs 30–40 minutes. That buys about:

| Slice        | Hours | Output            |
| ------------ | ----- | ----------------- |
| New problems | ~80   | ~140 problems     |
| Spaced redos | ~25   | ~70 second passes |
| Timed mocks  | ~13   | ~7 sessions       |

140 problems with retention is above what most big tech intern loops require.
Blind 75 alone clears a large share of first rounds, and all 75 are in this
repo. The number is not the constraint; how the hours are spent is.

## The Four Rules

1. **Apply in parallel, starting week one.** Applications and readiness run on
   separate tracks. An application sent in August produces an OA three to six
   weeks later, so every early application buys prep time. Waiting until you
   feel ready is how people miss the early cycle.
2. **Solve cold.** Reading a solution before genuinely struggling means the
   problem did not count. The tests give a verdict without showing an answer,
   which is why no solutions live in this repo.
3. **Redo on a later day.** First pass builds recognition, second pass builds
   speed. Same-day redos do not count — that is the rule the Notion board
   already enforces for `Mastered`.
4. **Mock from week two.** Talking while coding is a separate skill from
   solving, and it is the one that actually fails people. A first mock in late
   September is too late to fix it.

## Weekly Sequence

Modules are ordered by interview frequency, not by number. Roughly 20 new
problems a week.

| Week | Dates           | Focus                                                         | New |
| ---- | --------------- | ------------------------------------------------------------- | --- |
| 1    | Aug 17 – Aug 23 | `01_arrays_and_hashing` — hashing, prefix sums, Kadane        | ~20 |
| 2    | Aug 24 – Aug 30 | `02_two_pointers`, start `04_sliding_window` · **first mock** | ~20 |
| 3    | Aug 31 – Sep 6  | finish `04_sliding_window`, `05_binary_search`                | ~20 |
| 4    | Sep 7 – Sep 13  | `03_stacks_and_queues`, start `07_trees`                      | ~20 |
| 5    | Sep 14 – Sep 20 | finish `07_trees` — DFS, BFS levels, BST                      | ~20 |
| 6    | Sep 21 – Sep 27 | `10_graphs` — grid DFS/BFS, components, topo sort             | ~20 |
| 7    | Sep 28 – Oct 4  | `08_heaps`, `13_intervals`, core `11_dp`                      | ~20 |

One timed mock every week from week two, drawn from
`18_mixed_interview_practice` or `mock-interviews/`.

## Scope

**In.** Modules 01–05, 07, 08, 10, 13, and the standard DP band in 11: climbing
stairs, house robber, coin change, LIS, LCS, edit distance, the stock problems.
In graphs: grid DFS/BFS, components, cycles, bipartite, topological sort,
implicit-state BFS, basic Dijkstra.

**Out, deliberately.** Module 17 entirely — MST, Fenwick trees, KMP, bitmask DP,
divide and conquer. The DP tail — Burst Balloons, Cherry Pickup, Min Cost to
Merge Stones. Hard-tier tries — Palindrome Pairs, Word Squares. The weighted
shortest-path tail past basic Dijkstra.

These are cut for frequency, not difficulty. They are rare in intern loops, and
every hour spent there is an hour not spent on patterns that actually appear.
`CLAUDE.md` already orders union find, shortest paths, and advanced structures
after the core is reliable. If the core finishes early, module 17 is next.

## Falling Behind

A lost week is survivable; a lost fortnight is not. When behind, cut in this
order and do not skip modules wholesale:

1. Drop the hards in the current module. Fundamentals and mediums carry the
   pattern; the hards mostly drill stamina.
2. Cut new problems to 12 a week before cutting the weekly mock. The mock is
   load-bearing.
3. Never cut the later-day redos. A half-remembered pattern is worth less than
   nothing under pressure — it produces a confident wrong start.

## Daily Loop

```bash
uv run pytest 01_arrays_and_hashing/tests/test_hashing_problems.py -k two_sum -q
```

Read the workbook entry — its one-line pattern note is the hint an interviewer
would give. Delete `raise NotImplementedError`, write the solution, fill in the
`# Time:` and `# Space:` lines. Run the test: skip means untouched, red means
wrong, green means done. Say the complexity out loud before moving on.

Whole module: `uv run pytest 01_arrays_and_hashing -q`.
Everything: `uv run pytest -q` — the skip count is the remaining backlog, and
watching it fall is the progress bar.

## Status Tracking

Report finished problems and the Notion Problem Set Grind Board gets updated:
cold first solve → In progress, hint or solution used → Needs review, and
Mastered only on a cold redo on a later day. Needs-review cards resurface in the
next 8 AM daily brief.

## One Caveat Worth Keeping

Preparation is the controllable part, and 120 focused hours on the core patterns
is enough to be competitive. Outcomes still carry noise — headcount, interviewer,
which problem comes up. Being prepared does not guarantee any single offer; it
makes you competitive across the set of them. That is the actual game.
