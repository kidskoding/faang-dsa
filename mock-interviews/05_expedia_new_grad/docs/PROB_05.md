# Koko Eating Bananas

Source: [LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/)

Koko has `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The
guards have left and will return in `h` hours.

Koko decides an eating speed of `k` bananas per hour. Each hour she picks one
pile and eats up to `k` bananas from it; if the pile has fewer than `k`, she
eats it all and does not eat more that hour.

Return the minimum integer eating speed `k` such that she can finish all the
bananas within `h` hours.

## Examples

### Example 1

```python
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
```

### Example 2

```python
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

### Example 3

```python
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

## Constraints

```text
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
```
