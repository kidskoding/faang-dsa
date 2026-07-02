# Stack Problem Set

## Goal

Build stack and queue intuition from the ground up, then use that foundation to solve the medium and hard monotonic-stack and monotonic-queue problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the stack, queue, and deque basics you should be able to do without thinking too hard.

### 1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

- Pattern: push opening brackets, pop and match on a closing bracket.

### 2. [Min Stack](https://leetcode.com/problems/min-stack/)

- Pattern: track the running minimum alongside each push.

### 3. [Implement Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

- Pattern: two stacks simulate FIFO order.

### 4. [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)

- Pattern: fixed-size buffer with head and tail indices for O(1) operations at both ends.

### 5. [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

- Pattern: push characters and pop when the top equals the incoming character.

### 6. [Number Of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

- Pattern: queue of timestamps; pop from the front until inside the sliding time window.

## Mediums

These are the stack, monotonic stack, and monotonic queue mediums you should drill for FAANG-style interviews.

### 7. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

- Pattern: push operands, pop two and apply the operator when one appears.

### 8. [Decode String](https://leetcode.com/problems/decode-string/)

- Pattern: stack of (count, partial string) to resolve nested `k[...]` brackets.

### 9. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

- Pattern: stack resolves `*`/`/` immediately, leaves `+`/`-` terms for a final sum.

### 10. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

- Pattern: monotonic decreasing stack of indices resolved by the next warmer day.

### 11. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

- Pattern: monotonic stack over the full array plus a hash map lookup for the subset query.

### 12. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

- Pattern: monotonic stack over a circular array by iterating twice the length.

### 13. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

- Pattern: monotonic stack of (price, span) pairs collapsed as new prices arrive.

### 14. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

- Pattern: stack resolves collisions immediately as each new asteroid arrives.

### 15. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

- Pattern: monotonic increasing stack removes larger trailing digits while removals remain.

### 16. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- Pattern: monotonic decreasing deque of indices; the front is always the window max.

### 17. [Simplify Path](https://leetcode.com/problems/simplify-path/)

- Pattern: stack of directory names; pop on `..` and skip `.` and empty segments.

### 18. [Minimum Remove To Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

- Pattern: stack of unmatched `(` indices marks characters to delete in one pass.

### 19. [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)

- Pattern: simulate pushes and greedily pop whenever the top matches the next popped value.

### 20. [Remove All Adjacent Duplicates In String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

- Pattern: stack of (char, count) pairs collapsed when a run reaches length k.

### 21. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

- Pattern: monotonic increasing stack keeps the lexicographically smallest result using last-occurrence counts.

### 22. [132 Pattern](https://leetcode.com/problems/132-pattern/)

- Pattern: right-to-left monotonic stack tracks the largest valid "2" below each candidate "3".

### 23. [Sum Of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

- Pattern: monotonic stack counts subarrays where each element is the minimum via span boundaries.

### 24. [Sum Of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)

- Pattern: monotonic-stack contribution counting for both subarray minimums and maximums.

### 25. [Car Fleet](https://leetcode.com/problems/car-fleet/)

- Pattern: sort by position and use a stack of arrival times to merge cars into fleets.

## Hards And Extensions

These are the stack follow-ups that push beyond the standard medium set.

### 26. [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

- Pattern: monotonic increasing stack tracks left/right boundaries for each bar's max rectangle.

### 27. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- Pattern: monotonic decreasing stack resolves trapped water between bars as taller bars appear.

### 28. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

- Pattern: stack holds sign and running result across nested parentheses.

### 29. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

- Pattern: build per-row histograms and apply the largest-rectangle monotonic stack to each.

### 30. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

- Pattern: stack of indices; each match measures the valid span back to the last unmatched boundary.

### 31. [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)

- Pattern: group elements into per-frequency stacks and pop from the highest frequency group.

### 32. [Number Of Atoms](https://leetcode.com/problems/number-of-atoms/)

- Pattern: stack of atom-count maps multiplied and merged as parentheses close.

### 33. [Shortest Subarray With Sum At Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

- Pattern: monotonic increasing deque over prefix sums finds the shortest qualifying window.

## Recommended Order

If you want the shortest path to stack and queue fluency, do them in this order:

```text
1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
2. [Min Stack](https://leetcode.com/problems/min-stack/)
3. [Implement Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
4. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
5. [Simplify Path](https://leetcode.com/problems/simplify-path/)
6. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
7. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
8. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
9. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)
10. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
11. [Decode String](https://leetcode.com/problems/decode-string/)
12. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
13. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
14. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
15. [132 Pattern](https://leetcode.com/problems/132-pattern/)
16. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
17. [Sum Of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)
18. [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
19. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
20. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)
```
