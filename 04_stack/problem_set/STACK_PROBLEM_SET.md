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

### 4. [Implement Stack Using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

- Pattern: rotate a queue after each push to simulate LIFO order.

### 5. [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)

- Pattern: fixed-size buffer with head and tail indices for O(1) operations at both ends.

## Mediums

These are the stack, monotonic stack, and monotonic queue mediums you should drill for FAANG-style interviews.

### 6. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

- Pattern: push operands, pop two and apply the operator when one appears.

### 7. [Decode String](https://leetcode.com/problems/decode-string/)

- Pattern: stack of (count, partial string) to resolve nested `k[...]` brackets.

### 8. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

- Pattern: stack resolves `*`/`/` immediately, leaves `+`/`-` terms for a final sum.

### 9. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

- Pattern: monotonic decreasing stack of indices resolved by the next warmer day.

### 10. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

- Pattern: monotonic stack over the full array plus a hash map lookup for the subset query.

### 11. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

- Pattern: monotonic stack over a circular array by iterating twice the length.

### 12. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

- Pattern: monotonic stack of (price, span) pairs collapsed as new prices arrive.

### 13. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

- Pattern: stack resolves collisions immediately as each new asteroid arrives.

### 14. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

- Pattern: monotonic increasing stack removes larger trailing digits while removals remain.

### 15. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- Pattern: monotonic decreasing deque of indices; the front is always the window max.

## Hards And Extensions

These are the stack follow-ups that push beyond the standard medium set.

### 16. [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

- Pattern: monotonic increasing stack tracks left/right boundaries for each bar's max rectangle.

### 17. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- Pattern: monotonic decreasing stack resolves trapped water between bars as taller bars appear.

### 18. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

- Pattern: stack holds sign and running result across nested parentheses.

## Recommended Order

If you want the shortest path to stack and queue fluency, do them in this order:

```text
1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
2. [Min Stack](https://leetcode.com/problems/min-stack/)
3. [Implement Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
4. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
5. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
6. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
7. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
8. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)
9. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
10. [Decode String](https://leetcode.com/problems/decode-string/)
11. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
12. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
13. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
14. [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
15. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
16. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)
```
