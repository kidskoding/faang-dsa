# Sliding Window Problem Set

## Goal

Build sliding window intuition across the four window techniques —
fixed-size, variable-size, frequency-map, and monotonic-deque (max/min) —
then use each technique to solve the medium and hard sliding window problems
that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one window
technique. Work a section top to bottom: problems are ordered roughly
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

## Fixed Window

`fixed_window_problems.py` — window of constant size `k`; add the entering
element and remove the leaving one on each step.

### 1. [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

- solves: `find_max_average`
- Pattern: fixed-size window sum, add the incoming value and remove the outgoing one.

### 2. [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

- solves: `max_vowels`
- Pattern: size-`k` window, +1 when a vowel enters and -1 when a vowel leaves.

### 3. [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

- solves: `num_of_subarrays`
- Pattern: fixed-size window sum compared against `k * threshold` for each position.

### 4. [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

- solves: `contains_nearby_duplicate`
- Pattern: fixed-size window of at most `k` indices held in a set; a hit inside the set is a duplicate.

### 5. [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)

- solves: `count_good_substrings`
- Pattern: fixed-size window of length three, count windows whose characters are all distinct.

### 6. [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/)

- solves: `max_satisfied`
- Pattern: fixed-size window over grumpy minutes to maximize the extra customers the technique saves.

### 7. [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

- solves: `max_score`
- Pattern: minimize the fixed-size middle window so the taken ends (its complement) are maximized.

## Variable Window

`variable_window_problems.py` — window whose size changes; expand right,
shrink left while a validity condition is broken.

### 8. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- solves: `max_profit`
- Pattern: a window that only ever expands right while tracking the minimum seen so far.

### 9. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- solves: `length_of_longest_substring`
- Pattern: expand right and shrink left while a duplicate character exists in the window.

### 10. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

- solves: `min_sub_array_len`
- Pattern: expand right until the sum is valid, then shrink left to find the shortest window.

### 11. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

- solves: `longest_ones`
- Pattern: shrink left only when the count of zeros in the window exceeds the flip budget.

### 12. [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

- solves: `longest_subarray`
- Pattern: window allowing at most one zero; shrink when a second zero enters, answer is length minus one.

### 13. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

- solves: `num_subarray_product_less_than_k`
- Pattern: expand right multiplying in, shrink left while the product is too large, count windows ending at right.

### 14. [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)

- solves: `equal_substring`
- Pattern: expand right accumulating conversion cost, shrink left while the cost exceeds `maxCost`.

### 15. [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

- solves: `maximum_unique_subarray`
- Pattern: variable window of unique elements; shrink left when a duplicate enters, track the max window sum.

### 16. [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

- solves: `max_frequency`
- Pattern: sort, then slide a window where cost to raise all to the right edge stays within `k`.

### 17. [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/)

- solves: `longest_nice_subarray`
- Pattern: window whose elements are pairwise AND-zero; track a running OR mask and shrink on conflict.

## Frequency Window

`frequency_window_problems.py` — variable or fixed window backed by a
character/number frequency map, plus a match or distinct-count check.

### 18. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

- solves: `character_replacement`
- Pattern: frequency map tracks the most frequent character; shrink when replacements needed exceed `k`.

### 19. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)

- solves: `check_inclusion`
- Pattern: fixed-size frequency-map window compared against the target's character counts.

### 20. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

- solves: `find_anagrams`
- Pattern: fixed-size frequency-map window, record every index where counts match.

### 21. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

- solves: `total_fruit`
- Pattern: frequency map window that shrinks while more than two distinct types are present.

### 22. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

- solves: `length_of_longest_substring_k_distinct`
- Pattern: frequency map shrinks while the number of distinct keys exceeds `k`.

### 23. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

- solves: `subarrays_with_k_distinct`
- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` using two frequency-map windows.

### 24. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

- solves: `number_of_subarrays`
- Pattern: exactly-`k` count via `atMost(k) - atMost(k - 1)` applied to a parity/frequency window.

### 25. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

- solves: `min_window`
- Pattern: frequency map with a matched-count check; shrink while the window still satisfies all required counts.

### 26. [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

- solves: `number_of_substrings`
- Pattern: shrink left while all three characters are present, add `left` valid substrings for each right.

### 27. [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

- solves: `num_subarrays_with_sum`
- Pattern: exact-sum count via `atMost(goal) - atMost(goal - 1)` over a 0/1 window.

### 28. [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)

- solves: `balanced_string`
- Pattern: shrink the smallest window whose removal lets the outside counts be rebalanced to `n / 4` each.

### 29. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

- solves: `find_substring`
- Pattern: word-length-stepped windows with a word frequency map, one pass per starting offset.

### 30. [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)

- solves: `min_window_subsequence`
- Pattern: forward-scan then backtrack two-pointer window (not a classic monotonic slide).

## Window Max/Min

`window_max_min_problems.py` — monotonic deque of indices gives the max or
min of the current window in O(1) amortized.

### 31. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- solves: `max_sliding_window`
- Pattern: monotonic decreasing deque of indices gives the max of each window in O(1).

### 32. Sliding Window Minimum

- solves: `min_sliding_window`
- Pattern: mirror of the maximum; a monotonic increasing deque of indices gives each window min.

### 33. [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

- solves: `longest_subarray`
- Pattern: keep a max deque and a min deque over the window; shrink left while `max - min > limit`.

### 34. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

- solves: `shortest_subarray`
- Pattern: monotonic deque over prefix sums to find the shortest qualifying window with negatives allowed.

### 35. [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

- solves: `count_subarrays`
- Pattern: track last positions of `minK`, `maxK`, and out-of-range values to count valid windows per right edge.

### 36. [Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/)

- solves: `continuous_subarrays`
- Pattern: two deques track the window max and min; shrink left while `max - min > 2`, count windows per right edge.

### 37. [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/)

- solves: `find_max_value_of_equation`
- Pattern: monotonic decreasing deque of `y - x` keeps the best partner within the `|xi - xj| <= k` window.

### 38. [Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)

- solves: `maximum_robots`
- Pattern: sliding window with a monotonic deque for the running max charge time against the running sum budget.
