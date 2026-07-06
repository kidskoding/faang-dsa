# Reorganize String

Source: [LeetCode 767](https://leetcode.com/problems/reorganize-string/)

Given a string `s`, rearrange its characters so that no two adjacent
characters are the same.

Return any valid rearrangement. If no valid rearrangement is possible, return
the empty string `""`.

## Examples

### Example 1

```python
Input:  s = "aab"
Output: "aba"
```

### Example 2

```python
Input:  s = "aaab"
Output: ""
```

## Constraints

```text
1 <= s.length <= 500
s consists of lowercase English letters only
```

## Hint

Greedily place the most frequent remaining character that is not the one you
just placed. A max-heap keyed on remaining count makes this efficient.
