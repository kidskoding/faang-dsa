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

### 2. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- Pattern: expand right and shrink left while a duplicate character exists in the window.

### 3. [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

- Pattern: fixed-size window of at most `k` indices held in a set; a hit inside the set is a duplicate.

### 4. [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

- Pattern: fixed-size window counting vowels, update as one char enters and one leaves.

### 5. [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

- Pattern: fixed-size window sum compared against `k * threshold` for each position.

### 6. [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)

- Pattern: fixed-size window of length three, count windows whose characters are all distinct.

## Mediums

These are the common medium sliding window problems.

### 7. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

- Pattern: expand right until the sum is valid, then shrink left to find the shortest window.

### 8. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

- Pattern: shrink left only when the count of zeros in the window exceeds the flip budget.

### 9. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

- Pattern: frequency map tracks the most frequent character; shrink when replacements needed exceed `k`.

### 10. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)

- Pattern: fixed-size frequency-map window compared against the target's character counts.

### 11. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

- Pattern: fixed-size frequency-map window, record every index where counts match.

### 12. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

- Pattern: frequency map window that shrinks while more than two distinct types are present.

### 13. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- Pattern: monotonic decreasing deque of indices gives the max of each window in O(1).

### 14. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

- Pattern: expand right multiplying in, shrink left while the product is too large, count windows ending at right.

### 15. [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

- Pattern: minimize the fixed-size middle window so the taken ends (its complement) are maximized.

### 16. [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

- Pattern: variable window of unique elements; shrink left when a duplicate enters, track the max window sum.

### 17. [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)

- Pattern: expand right accumulating conversion cost, shrink left while the cost exceeds `maxCost`.

### 18. [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

- Pattern: shrink left while all three characters are present, add `left` valid substrings for each right.

### 19. [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

- Pattern: window allowing at most one zero; shrink when a second zero enters, answer is length minus one.

### 20. [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

- Pattern: sort, then slide a window where cost to raise all to the right edge stays within `k`.

### 21. [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

- Pattern: exact-sum count via `atMost(goal) - atMost(goal - 1)` over a 0/1 window.

### 22. [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/)

- Pattern: fixed-size window over grumpy minutes to maximize the extra customers the technique saves.

### 23. [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)

- Pattern: shrink the smallest window whose removal lets the outside counts be rebalanced to `n / 4` each.

### 24. [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/)

- Pattern: window whose elements are pairwise AND-zero; track a running OR mask and shrink on conflict.

## Hards And Extensions

These are the sliding window follow-ups that push beyond the standard medium
set.

### 25. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

- Pattern: frequency map with a matched-count check; shrink while the window still satisfies all required counts.

### 26. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

- Pattern: frequency map shrinks while the number of distinct keys exceeds `k`.

### 27. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` using two frequency-map windows.

### 28. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` applied to a parity/frequency window.

### 29. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

- Pattern: word-length-stepped windows with a word frequency map, one pass per starting offset.

### 30. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

- Pattern: fixed-size window with two balanced heaps (plus lazy deletion) to read the median in O(1).

### 31. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

- Pattern: monotonic deque over prefix sums to find the shortest qualifying window with negatives allowed.

### 32. [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

- Pattern: track last positions of `minK`, `maxK`, and out-of-range values to count valid windows per right edge.

### 33. [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)

- Pattern: forward-scan then backtrack two-pointer window (not a classic monotonic slide).

## Recommended Order

If you want the shortest path to sliding window fluency, do them in this
order:

```text
1. [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
2. [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
3. [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
4. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
5. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
6. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
7. [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)
8. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)
9. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
10. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
11. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
12. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
13. [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
14. [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)
15. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
16. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
17. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
18. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
19. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
20. [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)
```
