# Sliding Window Problem Set

## Goal

Build sliding window intuition from fixed-size windows through variable-size,
frequency-map, and monotonic-deque windows, then use that foundation to solve
the medium and hard sliding window problems that show up in LeetCode-style
interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later
sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the sliding window basics you should be able to do without
thinking too hard.

### 1. [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

- Pattern: fixed-size window sum, add the incoming value and remove the outgoing one.

### 2. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- Pattern: a window that only ever expands right while tracking the minimum seen so far.

### 3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- Pattern: expand right and shrink left while a duplicate character exists in the window.

## Mediums

These are the common medium sliding window problems.

### 4. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

- Pattern: expand right until the sum is valid, then shrink left to find the shortest window.

### 5. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

- Pattern: shrink left only when the count of zeros in the window exceeds the flip budget.

### 6. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

- Pattern: frequency map tracks the most frequent character; shrink when replacements needed exceed `k`.

### 7. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)

- Pattern: fixed-size frequency-map window compared against the target's character counts.

### 8. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

- Pattern: fixed-size frequency-map window, record every index where counts match.

### 9. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

- Pattern: frequency map window that shrinks while more than two distinct types are present.

### 10. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- Pattern: monotonic decreasing deque of indices gives the max of each window in O(1).

## Hards And Extensions

These are the sliding window follow-ups that push beyond the standard medium
set.

### 11. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

- Pattern: frequency map with a matched-count check; shrink while the window still satisfies all required counts.

### 12. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

- Pattern: frequency map shrinks while the number of distinct keys exceeds `k`.

### 13. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` using two frequency-map windows.

### 14. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` applied to a parity/frequency window.

## Recommended Order

If you want the shortest path to sliding window fluency, do them in this
order:

```text
1. [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
2. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
4. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
5. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
6. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)
7. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
8. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
9. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
10. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
11. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
12. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
13. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
14. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)
```
