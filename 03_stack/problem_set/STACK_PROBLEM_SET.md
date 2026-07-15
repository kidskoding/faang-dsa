# Stack Problem Set

## Goal

Build stack and queue intuition across the core stack techniques — plain
LIFO stacks, queue/deque design, and the monotonic stack — then use each
technique to solve the medium and hard stack and queue problems that show up
in LeetCode-style interviews. The monotonic deque built here is applied to
window problems in `04_sliding_window`.

## How To Use

Each section maps to one solution file in this folder and to one stack or
queue technique. Work a section top to bottom: problems are ordered roughly
easy to hard, and the implemented ones come first. `solves:` names the
function in that section's file; `solves: (todo)` means the solution is not
written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Stack Fundamentals

`stack_problems.py` — plain LIFO stack: push, pop, and inspect the top to
match, evaluate, or unwind nested structure.

### 1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

- solves: `is_valid`
- Pattern: push opening brackets, pop and match on a closing bracket.

### 2. [Min Stack](https://leetcode.com/problems/min-stack/)

- solves: `MinStack`
- Pattern: track the running minimum alongside each push.

### 3. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

- solves: `eval_rpn`
- Pattern: push operands, pop two and apply the operator when one appears.

### 4. [Decode String](https://leetcode.com/problems/decode-string/)

- solves: `decode_string`
- Pattern: stack of (count, partial string) to resolve nested `k[...]` brackets.

### 5. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

- solves: `calculate_ii`
- Pattern: stack resolves `*`/`/` immediately, leaves `+`/`-` terms for a final sum.

### 6. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

- solves: `calculate`
- Pattern: stack holds sign and running result across nested parentheses.

### 7. [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

- solves: `remove_duplicates`
- Pattern: push characters and pop when the top equals the incoming character.

### 8. [Simplify Path](https://leetcode.com/problems/simplify-path/)

- solves: `simplify_path`
- Pattern: stack of directory names; pop on `..` and skip `.` and empty segments.

### 9. [Minimum Remove To Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

- solves: `min_remove_to_make_valid`
- Pattern: stack of unmatched `(` indices marks characters to delete in one pass.

### 10. [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)

- solves: `validate_stack_sequences`
- Pattern: simulate pushes and greedily pop whenever the top matches the next popped value.

### 11. [Remove All Adjacent Duplicates In String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

- solves: `remove_duplicates_ii`
- Pattern: stack of (char, count) pairs collapsed when a run reaches length k.

### 12. [Number Of Atoms](https://leetcode.com/problems/number-of-atoms/)

- solves: `count_of_atoms`
- Pattern: stack of atom-count maps multiplied and merged as parentheses close.

### 13. [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)

- solves: `FreqStack`
- Pattern: group elements into per-frequency stacks and pop from the highest frequency group.

### 14. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

- solves: `longest_valid_parentheses`
- Pattern: stack of indices; each match measures the valid span back to the last unmatched boundary.

## Queue And Deque Design

`queue_deque_problems.py` — build FIFO and double-ended structures from
scratch on top of stacks, queues, and a ring buffer.

### 15. [Implement Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

- solves: `MyQueue`
- Pattern: two stacks simulate FIFO order.

### 16. [Implement Stack Using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

- solves: `MyStack`
- Pattern: rotate a queue after each push to simulate LIFO order.

### 17. [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)

- solves: `MyCircularDeque`
- Pattern: fixed-size buffer with head and tail indices for O(1) operations at both ends.

### 18. [Number Of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

- solves: `RecentCounter`
- Pattern: queue of timestamps; pop from the front until inside the sliding time window.

### 19. [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

- solves: `MyCircularQueue`
- Pattern: fixed-size ring buffer with head index and a count for O(1) enqueue/dequeue.

### 20. [Moving Average From Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)

- solves: `MovingAverage`
- Pattern: fixed-size FIFO window; keep a running sum and evict the front when it overflows.

### 21. [Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/)

- solves: `FrontMiddleBackQueue`
- Pattern: two deques split at the middle; rebalance after each op to keep the front half sized correctly.

## Monotonic Stack

`monotonic_stack_problems.py` — a stack kept sorted so each pop resolves the
next-greater / next-smaller relationship and its span boundaries.

### 22. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

- solves: `next_greater_element`
- Pattern: monotonic stack over the full array plus a hash map lookup for the subset query.

### 23. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

- solves: `daily_temperatures`
- Pattern: monotonic decreasing stack of indices resolved by the next warmer day.

### 24. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

- solves: `next_greater_elements`
- Pattern: monotonic stack over a circular array by iterating twice the length.

### 25. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

- solves: `StockSpanner`
- Pattern: monotonic stack of (price, span) pairs collapsed as new prices arrive.

### 26. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

- solves: `asteroid_collision`
- Pattern: stack resolves collisions immediately as each new asteroid arrives.

### 27. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

- solves: `remove_k_digits`
- Pattern: monotonic increasing stack removes larger trailing digits while removals remain.

### 28. [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

- solves: `largest_rectangle_area`
- Pattern: monotonic increasing stack tracks left/right boundaries for each bar's max rectangle.

### 29. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- solves: `trap`
- Pattern: monotonic decreasing stack resolves trapped water between bars as taller bars appear.

### 30. [Car Fleet](https://leetcode.com/problems/car-fleet/)

- solves: `car_fleet`
- Pattern: sort by position and use a stack of arrival times to merge cars into fleets.

### 31. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

- solves: `remove_duplicate_letters`
- Pattern: monotonic increasing stack keeps the lexicographically smallest result using last-occurrence counts.

### 32. [132 Pattern](https://leetcode.com/problems/132-pattern/)

- solves: `find132pattern`
- Pattern: right-to-left monotonic stack tracks the largest valid "2" below each candidate "3".

### 33. [Sum Of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

- solves: `sum_subarray_mins`
- Pattern: monotonic stack counts subarrays where each element is the minimum via span boundaries.

### 34. [Sum Of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)

- solves: `sub_array_ranges`
- Pattern: monotonic-stack contribution counting for both subarray minimums and maximums.

### 35. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

- solves: `maximal_rectangle`
- Pattern: build per-row histograms and apply the largest-rectangle monotonic stack to each.
