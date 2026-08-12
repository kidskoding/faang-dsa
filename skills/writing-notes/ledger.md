# Prerequisite Ledger

What each note **establishes**. A note may assume everything above it and must
not re-teach it. When you need a prior idea, link it in one line and move on:

```md
You met Dijkstra in [10_graphs/07](../../10_graphs/notes/07_weighted_shortest_paths.md).
Prim differs from it by exactly one line.
```

Readers go through the repo in module order, so "above" means lower module
number, or lower note number inside the same module.

Update this file whenever a note is added, renamed, or changes what it covers.

## 00_fundamentals

| Note                         | Establishes                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| 01_how_to_prep               | Learn → focused practice → specific review → later cold re-solve → mixed practice; OA/live/mock progression |
| 02_python_basics             | Interview Python; functions/type hints; iteration; mutation/aliasing; `list`/`dict`/`set`/tuple; slicing; sorting; comprehensions; `heapq`; `deque` |
| 03_time_and_space_complexity | Big-O derivation; named input variables; sequential/nested/halving work; worst case; output vs auxiliary space; amortized analysis |
| 04_common_operation_costs    | Documented list/dict/set/deque/heap/string/sort costs; average vs worst vs amortized bounds; choosing by the repeated operation |
| 05_interview_problem_solving | Natural clarify → example → brute force → bottleneck → optimize → code/test narration → analyze conversation; invariants, debugging, hints, and follow-ups |

Every later note may assume Big-O notation and Python fluency without comment.

## 01_arrays_and_hashing

| Note                    | Establishes                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| 01_dynamic_arrays       | Indexed contiguous storage; size vs capacity; geometric growth and amortized append; in-place mutation, swaps, swap-delete, range-to-index marking, matrix boundaries, and three-reversal rotation |
| 02_hashing              | Set membership vs map state; seen-set and complement lookup; frequency maps; signatures and grouping; sequence heads; length-prefix encoding; two-candidate Boyer-Moore cancellation and verification |
| 03_prefix_suffix_sums   | Leading-zero prefix arrays and O(1) range sums; running split totals; prefix/suffix products; prefix-frequency and earliest-index maps; equal-remainder ranges; 2D inclusion-exclusion |
| 04_kadanes_algorithm    | Local extend-or-restart state vs global optimum; all-negative initialization; boundary recovery; running-min, product, circular, absolute, turbulent, and empty-allowed repeated-array variations |
| 05_hash_table_internals | Hash functions, buckets, equality, collisions, separate chaining vs open addressing, duplicate-key updates, load factor, resizing/rehashing, and average/worst/amortized bounds |

## 02_two_pointers

| Note                       | Establishes                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 01_opposite_end_pointers   | Converging pointers on sorted input, why each move is forced, when a hash set beats it                                      |
| 02_same_direction_pointers | Read/write cursor pair, the `write <= read` invariant, in-place filtering, swapping, writing backwards, three-way partition |
| 03_in_place_mutation (absorbed) | Covered by `02_same_direction_pointers`; no standalone note exists                                                     |

## 03_stacks_and_queues

| Note               | Establishes                                      |
| ------------------ | ------------------------------------------------ |
| 01_stack           | LIFO, matching/pairing, `list` as a stack        |
| 02_queue_and_deque | FIFO, `deque`, O(1) both ends                    |
| 03_monotonic_stack | Next-greater/smaller in one pass, amortized O(n) |
| 04_monotonic_queue (absorbed) | Covered by `04_sliding_window/04_window_max_min`; no standalone note exists |

## 04_sliding_window

| Note                     | Establishes                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01_fixed_size_window     | Window of constant width, add-one/drop-one                                                                                                           |
| 02_variable_size_window  | Expand-until-invalid, shrink-until-valid                                                                                                             |
| 03_frequency_map_windows | Counts inside a window, delete-at-zero, matching character multisets, `have`/`need`/`formed` containment, `at_most(k) - at_most(k - 1)` for exact counts |
| 04_window_max_min        | **Monotonic deque**: domination, fixed-width max, min variant, two deques for a spread, prefix-sum variant for negatives, and the three expiry rules |

## 05_binary_search

| Note                    | Establishes                                                    |
| ----------------------- | -------------------------------------------------------------- |
| 01_binary_search_basics | Halving on sorted input, loop invariant, off-by-one discipline |
| 02_boundary_search      | First/last true, `bisect` semantics                            |
| 03_rotated_arrays       | Deciding which half is sorted                                  |
| 04_search_on_answer     | Binary searching a value space with a feasibility predicate    |

## 06_linked_lists

| Note                  | Establishes                                  |
| --------------------- | -------------------------------------------- |
| 01_linked_list_basics | `ListNode`, pointer walking, dummy head      |
| 02_fast_slow          | Cycle detection, midpoint, nth-from-end      |
| 03_reversal           | Three-pointer flip, recursive flip, sublist and k-group reversal, reversal as a front/back pairing subroutine |
| 04_merge_split        | Merging sorted lists, splitting in halves    |

## 07_trees

| Note             | Establishes                                                         |
| ---------------- | ------------------------------------------------------------------- |
| 01_fundamentals  | `TreeNode`, root/leaf/height/depth, recursion on subtrees           |
| 02_dfs           | Pre/in/post order, top-down vs bottom-up helpers, path backtracking |
| 03_bfs           | Level-order with a queue, level-sized loops                         |
| 04_path_problems | Root-to-leaf and any-path accumulation                              |
| 05_bst           | Ordering invariant, inorder is sorted, bounded search               |
| 06_construction  | Rebuilding from traversals, index maps                              |
| 07_serialization | Encode/decode with null markers                                     |
| 08_complexity    | Height vs node count, balanced vs skewed cost                       |

Recursion depth, call-stack space `O(h)`, and "recurse then combine" are assumed
from here on.

## 08_heaps

| Note           | Establishes                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| 01_heap_basics | Min-heap, `heapq`, O(log n) push/pop, tuple ordering, max-heap via negation |
| 02_top_k       | Size-k heap, why it beats full sorting                                      |
| 03_two_heaps   | Split-median technique                                                      |
| 04_k_way_merge | Merging k sequences with one candidate per source                           |

Heaps are assumed known in graphs and advanced modules — never re-explain
`heapq`.

## 09_backtracking

| Note                    | Establishes                                          |
| ----------------------- | ---------------------------------------------------- |
| 01_backtracking_basics  | Choose / explore / un-choose, decision tree, pruning |
| 02_subsets_combinations | Include-exclude, start index to avoid duplicates     |
| 03_permutations         | Used-set / swap approaches                           |
| 04_grid_backtracking    | Path search on a grid with visit-marking and undo    |

## 10_graphs

| Note                           | Establishes                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| 01_graph_basics                | Node/edge, directed vs undirected, weighted edges, adjacency list vs matrix, reachability |
| 02_grid_dfs                    | Grids as implicit graphs, flood fill, visited marking                                     |
| 03_grid_bfs                    | Shortest steps on unweighted grids, multi-source BFS                                      |
| 04_components_cycles_bipartite | Connected components, cycle detection, 2-coloring                                         |
| 05_topological_sort            | DAGs, in-degree/Kahn, dependency order                                                    |
| 06_implicit_state_bfs          | States as nodes when no graph is given                                                    |
| 07_weighted_shortest_paths     | **Dijkstra**, heap-based relaxation, `dist[]` accumulation                                |

Graph vocabulary and Dijkstra are settled here. Module 17 must not redefine
them.

## 11_dp

| Note               | Establishes                                                                     |
| ------------------ | ------------------------------------------------------------------------------- |
| 01_dp_fundamentals | Overlapping subproblems, optimal substructure, memo vs tabulation, state design |
| 02_1d_dp           | Linear state, rolling variables                                                 |
| 03_2d_grid_dp      | Two-index state, grid path counting                                             |
| 04_knapsack        | Capacity dimension, 0/1 vs unbounded                                            |
| 05_sequence_dp     | LIS/LCS-style two-sequence state                                                |

## 12_greedy_algorithms

| Note                   | Establishes                                              |
| ---------------------- | -------------------------------------------------------- |
| 01_greedy_fundamentals | Local choice, exchange argument, when greedy fails vs DP |
| 02_jump_game           | Reachability frontier                                    |
| 03_interval_greedy     | Sort-by-end scheduling                                   |

The exchange argument is established here — the cut property in MST can lean on
it.

## 13_intervals

| Note               | Establishes                                   |
| ------------------ | --------------------------------------------- |
| 01_interval_basics | Overlap test, sorting by start vs end         |
| 02_merge_insert    | Merging overlaps, inserting into a sorted set |
| 03_meeting_rooms   | Room counting with a heap                     |
| 04_sweep_line      | Delta events, running active count            |

## 14_tries

| Note               | Establishes                                      |
| ------------------ | ------------------------------------------------ |
| 01_trie_basics     | Prefix tree nodes, insert/search, terminal flags |
| 02_word_dictionary | Wildcard matching over a trie                    |
| 03_trie_plus_dfs   | Trie-guided grid/word search                     |

## 15_bit_manipulation

| Note              | Establishes                                 |
| ----------------- | ------------------------------------------- |
| 01_bitwise_basics | AND/OR/XOR/shift, two's complement          |
| 02_masks          | Set/clear/test a bit, mask building         |
| 03_xor_patterns   | Self-cancellation, missing/duplicate tricks |
| 04_subset_masks   | Iterating subsets as integers               |

## 16_math_geometry

| Note                  | Establishes                                             |
| --------------------- | ------------------------------------------------------- |
| 01_matrix_coordinates | Index transforms, rotation, spiral order                |
| 02_modular_arithmetic | Mod rules, overflow-safe accumulation                   |
| 03_gcd_lcm            | Euclid's algorithm                                      |
| 04_geometry_basics    | Points, distance metrics (incl. Manhattan), orientation |

Manhattan distance is defined here — MST's point-connection variant can assume
it.

## 17_advanced

| Note                  | Establishes                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| 01_union_find         | Disjoint sets, `find`/`union`, path compression, union by rank, "same component?" in ~O(1) |
| 02_shortest_paths     | Bellman-Ford, Floyd-Warshall, negative weights                                             |
| 03_mst                | **Cut property, Kruskal, Prim**                                                            |
| 04_range_structures   | Segment tree, Fenwick tree, range query/update                                             |
| 05_string_algorithms  | KMP, Z algorithm, Rabin-Karp                                                               |
| 06_divide_and_conquer | Recurrence splitting, merge-sort-shaped counting                                           |
| 07_bitmask_dp         | Subset states as DP dimensions                                                             |
| 08_bloom_filters      | Probabilistic membership, false-positive tradeoff                                          |

## 18_mixed_interview_practice

| Note               | Establishes                                     |
| ------------------ | ----------------------------------------------- |
| 01_timed_solving   | Working under a clock                           |
| 02_pattern_review  | Recognizing which pattern a blind problem wants |
| 03_mock_interviews | Full-loop simulation                            |

These assume the entire book and teach no new technique.
