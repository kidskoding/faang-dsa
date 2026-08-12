# DSA Notes Book Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite all active DSA notes into one natural, beginner-accessible,
big-tech interview-preparation book calibrated to the approved queue note.

**Architecture:** Treat the notes as a dependency-ordered book and finish one
module at a time from `00` through `18`. Each module is an independently reviewed
editorial unit: map its problem-set coverage, rewrite its notes from the current
working tree, update the prerequisite ledger, execute examples, and pass module
verification before later modules may depend on it.

**Tech Stack:** Markdown, Python 3.12+, `mdformat`, Mermaid, Git

**Spec:**
[`docs/superpowers/specs/2026-08-12-dsa-notes-book-rewrite-design.md`](../specs/2026-08-12-dsa-notes-book-rewrite-design.md)

## Global Constraints

- Use `03_stacks_and_queues/notes/02_queue_and_deque.md` as the calibration for
  natural prose, depth, traces, interview reasoning, and revision sections.
- Write for a reader with no LeetCode experience who wants big-tech interview
  readiness quickly.
- Preserve good existing prose. Rewrite Claude-expanded drafts as freely as thin
  skeletons when they are repetitive, rigid, or unclear.
- Worked examples remain continuous under one `## Worked Example` heading. Do not
  add `What You Are Given`, `The Approach`, `Step By Step`, `The Solution`, or
  `Complexity` subheadings.
- Do not force a worked example or algorithmic dry run into the meta notes in
  modules `00` and `18`.
- Every technique note must derive the technique, use runnable Python, contain a
  trace with a rejected or discarded step, and prepare the reader for its module
  problem set.
- Use current working-tree content as source material. Do not restore, reset,
  overwrite, stage, format, or commit unrelated user changes.
- Keep the existing deletions of
  `02_two_pointers/notes/03_in_place_mutation.md` and
  `03_stacks_and_queues/notes/04_monotonic_queue.md`; verify their teaching is
  absorbed by active notes.
- Change module READMEs and problem sets only if a rewritten note exposes a broken
  link that cannot be fixed inside the note.
- Update `skills/writing-notes/ledger.md` after every module.
- Use `git commit --only <task paths>` so the pre-existing staged deletions and
  unrelated working-tree changes never enter a task commit accidentally.

______________________________________________________________________

### Task 1: Persist The Approved Writing Standard

**Files:**

- Modify: `skills/writing-notes/SKILL.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: the approved queue note and rewrite design spec.

- Produces: the house style and prerequisite ledger every later task must read.

- [ ] **Step 1: Replace the rigid worked-example instructions**

  Make the queue note the primary calibration example. State explicitly that the
  required content is a natural flow, not a set of `###` subheadings, and copy the
  approved continuous worked-example rules from the spec.

- [ ] **Step 2: Align the rest of the skill with the approved voice**

  Keep derivation, executed Python, discarded-step traces, problem-set coverage,
  and prerequisite ordering. Remove instructions that force standalone `During the Interview` or `Common Pitfalls` sections; allow narration and pitfalls to
  sit where they naturally matter.

- [ ] **Step 3: Confirm the ledger matches the 84 active-note topology**

  Keep the active rows and the absorbed-topic rows for the two deleted notes.
  Do not invent new note files.

- [ ] **Step 4: Verify and commit the standard**

  Run:

  ```bash
  .venv/bin/mdformat --check skills/writing-notes/SKILL.md skills/writing-notes/ledger.md
  git diff --check -- skills/writing-notes/SKILL.md skills/writing-notes/ledger.md
  ```

  Commit:

  ```bash
  git add skills/writing-notes/SKILL.md skills/writing-notes/ledger.md
  git commit --only skills/writing-notes/SKILL.md skills/writing-notes/ledger.md -m "docs: calibrate DSA note writing"
  ```

### Task 2: Rewrite Module 00 — Fundamentals

**Files:**

- Modify: `00_fundamentals/notes/01_how_to_prep.md`
- Modify: `00_fundamentals/notes/02_python_basics.md`
- Modify: `00_fundamentals/notes/03_time_and_space_complexity.md`
- Modify: `00_fundamentals/notes/04_common_operation_costs.md`
- Modify: `00_fundamentals/notes/05_interview_problem_solving.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: no algorithmic prerequisites.

- Produces: the Python, complexity, operation-cost, preparation, and live-coding
  vocabulary every later module may assume.

- [ ] **Step 1: Rewrite the five notes as the book's on-ramp**

  `01_how_to_prep` should explain the shortest useful learn/practice/review loop;
  `02_python_basics` should teach only interview-relevant Python and containers;
  `03_time_and_space_complexity` should derive Big-O, auxiliary space, and
  amortization from concrete loops and operations; `04_common_operation_costs`
  should make its tables explain consequences rather than stand alone; and
  `05_interview_problem_solving` should model the clarify → brute force → optimize
  → code → test conversation naturally.

- [ ] **Step 2: Remove template headings and redundant generic advice**

  Do not force LeetCode worked examples into this module. Preserve practical
  examples, short scripts, interview phrases, and the final checklists.

- [ ] **Step 3: Execute every Python snippet and update the ledger**

  Run syntax examples with `.venv/bin/python` and confirm all cost-table claims
  against Python's documented operation model. Record exactly what later notes
  may assume.

- [ ] **Step 4: Verify and commit Module 00**

  Run:

  ```bash
  .venv/bin/mdformat --check 00_fundamentals/notes/*.md
  git diff --check -- 00_fundamentals/notes skills/writing-notes/ledger.md
  ```

  Commit only the five notes and ledger with message
  `docs: rewrite fundamentals notes`.

### Task 3: Rewrite Module 01 — Arrays And Hashing

**Files:**

- Modify: `01_arrays_and_hashing/notes/01_dynamic_arrays.md`
- Modify: `01_arrays_and_hashing/notes/02_hashing.md`
- Modify: `01_arrays_and_hashing/notes/03_prefix_suffix_sums.md`
- Modify: `01_arrays_and_hashing/notes/04_kadanes_algorithm.md`
- Modify: `01_arrays_and_hashing/notes/05_hash_table_internals.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: Module 00 Python and complexity vocabulary.

- Produces: array indexing/growth, hash lookup/counting, prefix sums, Kadane's
  running optimum, and hash-table collision vocabulary.

- [ ] **Step 1: Map the five notes to the workbook**

  Cover array mutation and swap-delete, hashing and frequency maps, prefix sums
  and prefix-frequency lookup, Kadane's local/global state, and hash-table design.
  Use `Group Anagrams`, `Subarray Sum Equals K`, `Maximum Subarray`, and `Design HashMap` as the principal end-to-end examples where they fit; do not make the
  dynamic-array note assume hashing before the next note teaches it.

- [ ] **Step 2: Rewrite all five notes and update the ledger**

  Make index/state diagrams concrete, derive each optimization from repeated
  scanning or shifting, and include a rejected lookup/candidate in every trace.

- [ ] **Step 3: Execute examples and verify the module**

  Include empty/singleton arrays, duplicate keys, negative prefix sums, and an
  all-negative Kadane input.

  Run:

  ```bash
  .venv/bin/mdformat --check 01_arrays_and_hashing/notes/*.md
  git diff --check -- 01_arrays_and_hashing/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 01**

  Commit only the five notes and ledger with message
  `docs: rewrite arrays and hashing notes`.

### Task 4: Rewrite Module 02 — Two Pointers

**Files:**

- Modify: `02_two_pointers/notes/01_opposite_end_pointers.md`
- Modify: `02_two_pointers/notes/02_same_direction_pointers.md`
- Verify deletion: `02_two_pointers/notes/03_in_place_mutation.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: array indexing, hash-set alternatives, and operation costs.

- Produces: forced opposite-end movement, read/write cursors, in-place filtering,
  backward writes, partitioning, and the absorbed in-place-mutation material.

- [ ] **Step 1: Recut Claude's expanded prose to the queue-note density**

  Preserve the strongest pointer diagrams and derivations. Use `Container With Most Water` and `Sort Colors` as continuous worked examples. Remove forced
  worked-example subheadings and repeated statements of the same invariant.

- [ ] **Step 2: Prove the deleted note's coverage is absorbed**

  Confirm swapping, writing backward, and three-way partitioning live in
  `02_same_direction_pointers.md`; record that fact in the ledger without
  restoring the deleted file.

- [ ] **Step 3: Execute examples and verify**

  Test duplicate values, pointers that do not move on a rejected candidate,
  empty input, and all-equal partition input.

  Run:

  ```bash
  .venv/bin/mdformat --check 02_two_pointers/notes/*.md
  git diff --check -- 02_two_pointers/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 02**

  Commit only the two active notes and ledger with message
  `docs: rewrite two pointers notes`. Leave the pre-existing staged deletion
  untouched.

### Task 5: Rewrite Module 03 — Stacks And Queues

**Files:**

- Modify: `03_stacks_and_queues/notes/01_stack.md`
- Verify calibration: `03_stacks_and_queues/notes/02_queue_and_deque.md`
- Modify: `03_stacks_and_queues/notes/03_monotonic_stack.md`
- Verify deletion: `03_stacks_and_queues/notes/04_monotonic_queue.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: Python containers and amortized analysis.

- Produces: LIFO/FIFO, deque/ring-buffer design, nested-state stacks,
  next-greater/smaller resolution, and monotonic-queue ownership by Module 04.

- [ ] **Step 1: Rewrite stack and monotonic-stack notes**

  Use `Minimum Remove To Make Valid Parentheses` and `Daily Temperatures` as the
  continuous worked examples. Keep queue/deque as the calibration note and make
  only correctness, link, or formatting fixes to it.

- [ ] **Step 2: Prove monotonic-queue coverage moved to Module 04**

  Confirm `04_sliding_window/notes/04_window_max_min.md` owns monotonic deque
  domination and expiry. Keep the deleted Module 03 note deleted and update the
  ledger wording.

- [ ] **Step 3: Execute examples and verify**

  Test unmatched closers, nested encoded state, a decreasing temperature input,
  equal values, ring-buffer wraparound, and front-middle-back even/odd cases.

  Run:

  ```bash
  .venv/bin/mdformat --check 03_stacks_and_queues/notes/*.md
  git diff --check -- 03_stacks_and_queues/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 03**

  Commit only the three active notes and ledger with message
  `docs: rewrite stacks and queues notes`. Leave the pre-existing staged deletion
  untouched.

### Task 6: Rewrite Module 04 — Sliding Window

**Files:**

- Modify: `04_sliding_window/notes/01_fixed_size_window.md`
- Modify: `04_sliding_window/notes/02_variable_size_window.md`
- Modify: `04_sliding_window/notes/03_frequency_map_windows.md`
- Modify: `04_sliding_window/notes/04_window_max_min.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: arrays, hashing, two pointers, deques, and amortized analysis.

- Produces: fixed add/drop windows, variable shrink conditions, frequency-window
  invariants, exact-count transforms, and monotonic-deque max/min windows.

- [ ] **Step 1: Recut all four expanded notes**

  Keep the distinct variants the workbook exercises, but remove duplicate
  templates and repeated explanations. Use `Maximum Points You Can Obtain From Cards`, `Longest Substring Without Repeating Characters`, `Longest Repeating Character Replacement`, and `Longest Continuous Subarray With Absolute Difference At Most Limit` as principal continuous worked examples.

- [ ] **Step 2: Preserve the important contrasts**

  Make fixed versus variable width, counts versus membership, `at_most(k)` exact
  counting, stale maximum counts, value versus index deques, and the three expiry
  rules explicit without re-teaching prior modules.

- [ ] **Step 3: Execute examples and verify**

  Test `k = 1`, an immediately invalid window, duplicate-heavy windows, no valid
  cover, stale deque entries, and negative-prefix shortest-subarray behavior.

  Run:

  ```bash
  .venv/bin/mdformat --check 04_sliding_window/notes/*.md
  git diff --check -- 04_sliding_window/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 04**

  Commit only the four notes and ledger with message
  `docs: rewrite sliding window notes`.

### Task 7: Rewrite Module 05 — Binary Search

**Files:**

- Modify: `05_binary_search/notes/01_binary_search_basics.md`
- Modify: `05_binary_search/notes/02_boundary_search.md`
- Modify: `05_binary_search/notes/03_rotated_arrays.md`
- Modify: `05_binary_search/notes/04_search_on_answer.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: array indexing, invariants, and complexity analysis.

- Produces: exact search, first/last-true boundaries, rotated-half reasoning, and
  monotone feasibility search.

- [ ] **Step 1: Rewrite and shorten the four expanded notes**

  Preserve interval diagrams and near-miss comparisons. Use `Search A 2D Matrix`,
  `Find First And Last Position`, `Search In Rotated Sorted Array`, and `Koko Eating Bananas` as continuous worked examples.

- [ ] **Step 2: Make every boundary contract explicit**

  State whether bounds are inclusive, what remains possible, how duplicates
  change the move, and why the returned boundary is valid. Remove repeated
  off-by-one warnings once the consequence has been shown.

- [ ] **Step 3: Execute examples and verify**

  Test empty and one-element spaces, absent targets, duplicate boundaries,
  rotation at zero, and feasibility answers at both extremes.

  Run:

  ```bash
  .venv/bin/mdformat --check 05_binary_search/notes/*.md
  git diff --check -- 05_binary_search/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 05**

  Commit only the four notes and ledger with message
  `docs: rewrite binary search notes`.

### Task 8: Rewrite Module 06 — Linked Lists

**Files:**

- Modify: `06_linked_lists/notes/01_linked_list_basics.md`
- Modify: `06_linked_lists/notes/02_fast_slow.md`
- Modify: `06_linked_lists/notes/03_reversal.md`
- Modify: `06_linked_lists/notes/04_merge_split.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: pointer movement, recursion basics, and dummy-node conventions.

- Produces: node rewiring, dummy heads, fast/slow relationships, reversal
  primitives, and merge/split ownership.

- [ ] **Step 1: Rewrite and recut all four expanded notes**

  Use `Add Two Numbers`, `Reorder List`, `Reverse Linked List II`, and `Sort List`
  as continuous worked examples. Keep linked-list diagrams where they show a
  shape that prose cannot.

- [ ] **Step 2: Center the notes on pointer ownership**

  Explain what each pointer currently owns, what would be lost by assigning in
  the wrong order, and which boundary is excluded. Remove repeated definitions of
  nodes and traversal after the first note establishes them.

- [ ] **Step 3: Execute examples and verify**

  Test empty/singleton lists, even/odd midpoint behavior, a cycle entering after
  the head, full and partial reversal, and uneven merge halves.

  Run:

  ```bash
  .venv/bin/mdformat --check 06_linked_lists/notes/*.md
  git diff --check -- 06_linked_lists/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 06**

  Commit only the four notes and ledger with message
  `docs: rewrite linked list notes`.

### Task 9: Rewrite Module 07 — Trees

**Files:**

- Modify: `07_trees/notes/01_fundamentals.md`
- Modify: `07_trees/notes/02_dfs.md`
- Modify: `07_trees/notes/03_bfs.md`
- Modify: `07_trees/notes/04_path_problems.md`
- Modify: `07_trees/notes/05_bst.md`
- Modify: `07_trees/notes/06_construction.md`
- Modify: `07_trees/notes/07_serialization.md`
- Modify: `07_trees/notes/08_complexity.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: recursion, stacks, queues, hashing, and complexity.

- Produces: tree vocabulary, DFS/BFS orders, path state, BST bounds, traversal
  reconstruction, serialization, and height-sensitive cost analysis.

- [ ] **Step 1: Expand the eight partial notes into a coherent module**

  Use natural cross-references instead of redefining `TreeNode` in every file.
  Principal worked examples are `Lowest Common Ancestor Of A Binary Tree`,
  `Binary Tree Level Order Traversal`, `Path Sum II`, `Validate Binary Search Tree`, `Construct Binary Tree From Preorder And Inorder`, and `Serialize And Deserialize Binary Tree`. Fundamentals and complexity may use focused examples
  rather than forced additional mediums.

- [ ] **Step 2: Add the missing visual and verbal reasoning**

  Draw tree shapes with Mermaid, keep traversal logs in text, distinguish
  top-down from bottom-up returns, and state what each recursive call promises.

- [ ] **Step 3: Execute examples and verify**

  Test empty, leaf, balanced, and skewed trees; duplicate-value construction
  assumptions; null serialization markers; and BFS level boundaries.

  Run:

  ```bash
  .venv/bin/mdformat --check 07_trees/notes/*.md
  git diff --check -- 07_trees/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 07**

  Commit only the eight notes and ledger with message `docs: rewrite tree notes`.

### Task 10: Rewrite Module 08 — Heaps

**Files:**

- Modify: `08_heaps/notes/01_heap_basics.md`
- Modify: `08_heaps/notes/02_top_k.md`
- Modify: `08_heaps/notes/03_two_heaps.md`
- Modify: `08_heaps/notes/04_k_way_merge.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: arrays, tuple comparison, linked lists, and complexity.

- Produces: `heapq`, bounded top-k heaps, two-heap partitions, and k-way frontier
  merging.

- [ ] **Step 1: Replace the four skeletons with full teaching notes**

  Use `Kth Largest Element In An Array`, `K Closest Points To Origin`, `Find Median From Data Stream`, and `Kth Smallest Element In A Sorted Matrix` as the
  main examples. Explain tuple ordering and max-heap negation once.

- [ ] **Step 2: Trace rejected and stale candidates**

  Include an item rejected from a size-`k` heap, a rebalance across two heaps, and
  a k-way source that has no next item.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 08_heaps/notes/*.md
  git diff --check -- 08_heaps/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 08**

  Commit only the four notes and ledger with message `docs: rewrite heap notes`.

### Task 11: Rewrite Module 09 — Backtracking

**Files:**

- Modify: `09_backtracking/notes/01_backtracking_basics.md`
- Modify: `09_backtracking/notes/02_subsets_combinations.md`
- Modify: `09_backtracking/notes/03_permutations.md`
- Modify: `09_backtracking/notes/04_grid_backtracking.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: recursion, sets, grids, and call-stack space.

- Produces: choose/explore/unchoose, decision trees, start-index ownership,
  duplicate control, and grid visit/restore discipline.

- [ ] **Step 1: Replace the four skeletons with full notes**

  Use `Combination Sum`, `Subsets II`, `Permutations II`, and `Word Search` as
  continuous worked examples. Show the decision tree only where it clarifies
  branching.

- [ ] **Step 2: Make pruning and undoing concrete**

  Trace a branch that is pruned, a duplicate choice that is skipped, and a grid
  cell that is restored after a failed path.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 09_backtracking/notes/*.md
  git diff --check -- 09_backtracking/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 09**

  Commit only the four notes and ledger with message
  `docs: rewrite backtracking notes`.

### Task 12: Rewrite Module 10 — Graphs

**Files:**

- Modify: `10_graphs/notes/01_graph_basics.md`
- Modify: `10_graphs/notes/02_grid_dfs.md`
- Modify: `10_graphs/notes/03_grid_bfs.md`
- Modify: `10_graphs/notes/04_components_cycles_bipartite.md`
- Modify: `10_graphs/notes/05_topological_sort.md`
- Modify: `10_graphs/notes/06_implicit_state_bfs.md`
- Modify: `10_graphs/notes/07_weighted_shortest_paths.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: trees, queues, heaps, grids, sets, and recursion.

- Produces: graph representation, grid DFS/BFS, components/cycles/bipartite
  coloring, topological order, implicit state graphs, and Dijkstra.

- [ ] **Step 1: Replace all seven skeletons with a dependency-ordered module**

  Use `Clone Graph`, `Number Of Islands`, `Rotting Oranges`, `Graph Valid Tree`,
  `Course Schedule II`, `Open The Lock`, and `Network Delay Time` as principal
  continuous worked examples.

- [ ] **Step 2: Draw the graph mechanisms that prose cannot show**

  Include directed/undirected adjacency, visited timing, multi-source layers, a
  rejected cycle/color conflict, in-degree release, and a stale Dijkstra heap
  entry. Do not re-teach heaps.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 10_graphs/notes/*.md
  git diff --check -- 10_graphs/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 10**

  Commit the seven notes and ledger with message `docs: rewrite graph notes`.

### Task 13: Rewrite Module 11 — Dynamic Programming

**Files:**

- Modify: `11_dp/notes/01_dp_fundamentals.md`
- Modify: `11_dp/notes/02_1d_dp.md`
- Modify: `11_dp/notes/03_2d_grid_dp.md`
- Modify: `11_dp/notes/04_knapsack.md`
- Modify: `11_dp/notes/05_sequence_dp.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: recursion, arrays, grids, and complexity.

- Produces: state/transition/base-case design, memoization/tabulation, rolling
  state, 2D grids, knapsack capacity, and sequence DP.

- [ ] **Step 1: Recut fundamentals and replace four skeletons**

  Use `Coin Change`, `House Robber`, `Unique Paths`, `Partition Equal Subset Sum`, and `Longest Common Subsequence` as continuous worked examples. A DP table
  must be shown partly filled with the dependency that produces the next cell.

- [ ] **Step 2: Derive state instead of presenting recurrence formulas**

  For each note, state what one cell means in a complete sentence, where its
  predecessors come from, and why iteration order is safe. Include a discarded
  choice or unreachable state in every trace.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 11_dp/notes/*.md
  git diff --check -- 11_dp/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 11**

  Commit the five notes and ledger with message `docs: rewrite dynamic programming notes`.

### Task 14: Rewrite Module 12 — Greedy Algorithms

**Files:**

- Modify: `12_greedy_algorithms/notes/01_greedy_fundamentals.md`
- Modify: `12_greedy_algorithms/notes/02_jump_game.md`
- Modify: `12_greedy_algorithms/notes/03_interval_greedy.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: sorting, DP contrast, heaps, and intervals.

- Produces: safe local choices, exchange arguments, reachability frontiers, and
  sort-by-end scheduling.

- [ ] **Step 1: Replace all three skeletons with full notes**

  Use `Gas Station`, `Jump Game II`, and `Non-overlapping Intervals` as continuous
  worked examples.

- [ ] **Step 2: Prove why each local choice is safe**

  Include a greedy rule that fails, the counterexample that breaks it, and the
  exchange/frontier argument that validates the chosen rule.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 12_greedy_algorithms/notes/*.md
  git diff --check -- 12_greedy_algorithms/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 12**

  Commit the three notes and ledger with message `docs: rewrite greedy notes`.

### Task 15: Rewrite Module 13 — Intervals

**Files:**

- Modify: `13_intervals/notes/01_interval_basics.md`
- Modify: `13_intervals/notes/02_merge_insert.md`
- Modify: `13_intervals/notes/03_meeting_rooms.md`
- Modify: `13_intervals/notes/04_sweep_line.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: sorting, heaps, and greedy scheduling.

- Produces: overlap semantics, merge/insert scans, room allocation, and sweep-line
  event deltas.

- [ ] **Step 1: Replace all four skeletons with full notes**

  Use `Interval List Intersections`, `Insert Interval`, `Meeting Rooms II`, and
  `Car Pooling` as continuous worked examples.

- [ ] **Step 2: Make endpoint semantics visible**

  State closed versus half-open assumptions, show an interval rejected as
  disjoint, explain tie ordering at equal timestamps, and distinguish sorting by
  start from sorting by end.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 13_intervals/notes/*.md
  git diff --check -- 13_intervals/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 13**

  Commit the four notes and ledger with message `docs: rewrite interval notes`.

### Task 16: Rewrite Module 14 — Tries

**Files:**

- Modify: `14_tries/notes/01_trie_basics.md`
- Modify: `14_tries/notes/02_word_dictionary.md`
- Modify: `14_tries/notes/03_trie_plus_dfs.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: hash maps, recursion, backtracking, and strings.

- Produces: prefix-tree nodes, terminal markers, wildcard branching, and
  trie-guided DFS pruning.

- [ ] **Step 1: Replace all three skeletons with full notes**

  Use `Implement Trie`, `Design Add And Search Words Data Structure`, and `Word Search II` as continuous worked examples. The last is hard because the workbook
  has no medium that exercises the combined trie-plus-grid technique completely.

- [ ] **Step 2: Draw accepted and rejected prefixes**

  Show why a prefix is not automatically a word, how `.` branches, and how a
  missing trie edge prunes a grid path before the remaining board is searched.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 14_tries/notes/*.md
  git diff --check -- 14_tries/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 14**

  Commit the three notes and ledger with message `docs: rewrite trie notes`.

### Task 17: Rewrite Module 15 — Bit Manipulation

**Files:**

- Modify: `15_bit_manipulation/notes/01_bitwise_basics.md`
- Modify: `15_bit_manipulation/notes/02_masks.md`
- Modify: `15_bit_manipulation/notes/03_xor_patterns.md`
- Modify: `15_bit_manipulation/notes/04_subset_masks.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: binary representation, arrays, and subsets.

- Produces: bitwise operators, two's complement, masks, XOR cancellation, and
  subset-mask enumeration.

- [ ] **Step 1: Replace all four skeletons with a small-toolkit style**

  Use `Divide Two Integers`, `UTF-8 Validation`, `Single Number III`, and
  `Partition To K Equal Sum Subsets` as the principal examples. Do not force one
  brute-force narrative across unrelated bit tricks.

- [ ] **Step 2: Trace bits at fixed widths**

  Show leading zeros when they matter, a mask that rejects a bit, cancellation
  order for XOR, and a subset mask skipped because it violates the state rule.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 15_bit_manipulation/notes/*.md
  git diff --check -- 15_bit_manipulation/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 15**

  Commit the four notes and ledger with message
  `docs: rewrite bit manipulation notes`.

### Task 18: Rewrite Module 16 — Math And Geometry

**Files:**

- Modify: `16_math_geometry/notes/01_matrix_coordinates.md`
- Modify: `16_math_geometry/notes/02_modular_arithmetic.md`
- Modify: `16_math_geometry/notes/03_gcd_lcm.md`
- Modify: `16_math_geometry/notes/04_geometry_basics.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: arrays, hash maps, binary search, and arithmetic complexity.

- Produces: matrix transforms, modular arithmetic, Euclid's algorithm, distance
  metrics, slopes, and orientation.

- [ ] **Step 1: Replace all four skeletons with full notes**

  Use `Rotate Image`, `Pow(x, n)`, `Water And Jug Problem`, and `Minimum Area Rectangle` as continuous worked examples.

- [ ] **Step 2: Make mathematical conditions reconstructible**

  Derive index transforms from coordinates, state modulo equivalences with
  examples, trace Euclid's shrinking remainder, and avoid floating-point slope
  comparisons where normalized integer pairs are safer.

- [ ] **Step 3: Execute examples and verify**

  Run:

  ```bash
  .venv/bin/mdformat --check 16_math_geometry/notes/*.md
  git diff --check -- 16_math_geometry/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 16**

  Commit the four notes and ledger with message
  `docs: rewrite math and geometry notes`.

### Task 19: Rewrite Module 17 — Advanced Techniques

**Files:**

- Modify: `17_advanced/notes/01_union_find.md`
- Modify: `17_advanced/notes/02_shortest_paths.md`
- Modify: `17_advanced/notes/03_mst.md`
- Modify: `17_advanced/notes/04_range_structures.md`
- Modify: `17_advanced/notes/05_string_algorithms.md`
- Modify: `17_advanced/notes/06_divide_and_conquer.md`
- Modify: `17_advanced/notes/07_bitmask_dp.md`
- Modify: `17_advanced/notes/08_bloom_filters.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: the complete algorithmic curriculum through Module 16.

- Produces: union-find, negative-weight shortest paths, MSTs, range structures,
  string matching, divide-and-conquer counting, bitmask DP, and probabilistic
  membership.

- [ ] **Step 1: Rewrite all eight notes, including Claude's expanded drafts**

  Use `Redundant Connection`, `Cheapest Flights Within K Stops`, `Min Cost To Connect All Points`, `Range Sum Query Mutable`, `Repeated String Match`,
  `Different Ways To Add Parentheses`, and `Smallest Sufficient Team` as principal
  worked examples. Keep Bloom filters concise and conceptual because the workbook
  does not drill them.

- [ ] **Step 2: Recut the MST exemplar to the approved queue style**

  Preserve the cut-property derivation, Kruskal/Prim contrast, and both traces.
  Remove forced worked-example subheadings and any prose that repeats the same
  invariant. Apply the same natural-flow edit to divide-and-conquer and bitmask DP.

- [ ] **Step 3: Execute examples and verify**

  Test redundant union, negative cycles, stale heap edges, disconnected ranges,
  Fenwick index movement, overlapping string matches, odd recursion splits,
  unreachable subset states, and Bloom-filter false-positive semantics.

  Run:

  ```bash
  .venv/bin/mdformat --check 17_advanced/notes/*.md
  git diff --check -- 17_advanced/notes skills/writing-notes/ledger.md
  ```

- [ ] **Step 4: Commit Module 17**

  Commit the eight notes and ledger with message
  `docs: rewrite advanced algorithm notes`.

### Task 20: Rewrite Module 18 — Mixed Interview Practice

**Files:**

- Modify: `18_mixed_interview_practice/notes/01_timed_solving.md`
- Modify: `18_mixed_interview_practice/notes/02_pattern_review.md`
- Modify: `18_mixed_interview_practice/notes/03_mock_interviews.md`
- Modify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: the entire finished concept book.

- Produces: timed execution, blind pattern recognition, and full mock-interview
  simulation without teaching new algorithms.

- [ ] **Step 1: Replace the three skeletons with practical closing notes**

  Make the guidance read like a rehearsal plan rather than generic motivation.
  Use short mixed-problem classifications and timed decision logs, not forced
  single-technique worked examples.

- [ ] **Step 2: Tie every recommendation to observable behavior**

  Define what to do at 0, 5, 15, and 30 minutes; how to recover after a wrong
  pattern; what the interviewer should hear; and how to score a mock without
  pretending a same-day redo proves mastery.

- [ ] **Step 3: Verify and commit Module 18**

  Run:

  ```bash
  .venv/bin/mdformat --check 18_mixed_interview_practice/notes/*.md
  git diff --check -- 18_mixed_interview_practice/notes skills/writing-notes/ledger.md
  ```

  Commit the three notes and ledger with message
  `docs: rewrite mixed interview practice notes`.

### Task 21: Run The Whole-Book Completion Audit

**Files:**

- Verify: all 84 active `*/notes/*.md` files
- Verify: `skills/writing-notes/SKILL.md`
- Verify: `skills/writing-notes/ledger.md`

**Interfaces:**

- Consumes: completed Tasks 1–20.

- Produces: the evidence required to claim the book rewrite is complete.

- [ ] **Step 1: Audit topology and coverage**

  Confirm there are 84 active notes, the two intentional deletions remain, every
  workbook technique maps to teaching, and every ledger row resolves to an active
  note or an explicit absorbed-topic statement.

- [ ] **Step 2: Search for rigid or incomplete remnants**

  Run:

  ```bash
  rg -n '^## (Pattern|Intuition|How It Works|Template|Example|Complexity|Pitfalls)$' [0-9][0-9]_*/notes
  rg -n '^### (What You Are Given And What You Return|The Approach|Step By Step|The Solution|Complexity)' [0-9][0-9]_*/notes
  rg -n 'TBD|TODO|FIXME|NotImplementedError' [0-9][0-9]_*/notes
  ```

  Investigate every match. A topic-specific use may remain only when it reads
  naturally and is complete.

- [ ] **Step 3: Verify Markdown and file scope globally**

  Run:

  ```bash
  rg --files | rg '^[0-9]{2}_[^/]+/notes/[^/]+\.md$' | xargs .venv/bin/mdformat --check
  .venv/bin/mdformat --check skills/writing-notes/SKILL.md skills/writing-notes/ledger.md
  git diff --name-only -- '*.py'
  git diff --check
  ```

  The Python-file diff must be empty, because this project keeps exercise
  implementations intentionally incomplete and the rewrite must not alter them.
  Functional evidence comes from executing the exact Python blocks copied into
  the notes with the assertions specified in each module task.

- [ ] **Step 4: Audit local links and diagrams**

  Resolve every relative Markdown link from its containing note. Render every
  Mermaid block and correct any parse failure. Re-run the affected module's
  formatting and tests after each correction.

- [ ] **Step 5: Compare every note with the approved calibration**

  Confirm the prose flows naturally, jargon is introduced before use, the reader
  sees why the technique exists, code and traces agree, interview reasoning is
  present, worked examples have no forced subheadings, and summaries/checklists
  can be used for revision without rereading the full note.

- [ ] **Step 6: Commit final ledger or cross-link corrections**

  Commit only files changed by the completion audit with message
  `docs: complete DSA notes book rewrite`.
