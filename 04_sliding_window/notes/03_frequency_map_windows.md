# Frequency-Map Windows

A **frequency map** stores `value -> number of live copies`. It is the right
window state when validity depends not only on whether a value is present, but
also on how many copies are present.

That is different from **membership**:

- A set answers “is this value in the window?”
- A frequency map answers “how many copies are in the window?”

The difference matters when one copy leaves while another remains. If the
window `"aab"` drops its first `a`, a set that discards `a` now claims no `a`
is present. A map changes `a: 2` to `a: 1` and stays correct.

Growing and shrinking are mirror operations:

```text
grow with x:    counts[x] = counts.get(x, 0) + 1
shrink with y:  counts[y] -= 1
                if counts[y] == 0:
                    del counts[y]
```

Deleting at zero makes `len(counts)` equal the number of **distinct** values in
the current window. Leaving dead keys behind makes that test permanently too
large.

## When Counts Belong In The Window

Use a frequency map when the problem asks about one of these:

- The number of distinct values, as in “at most `k` characters” or two fruit
  baskets.
- A permutation or anagram, where order does not matter but multiplicity does.
- A window that contains every required character, including repeated
  requirements such as the two `A`s in `"AABC"`.
- Exactly `k` occurrences or distinct values.
- The most frequent character in the window.

Do not use a map when order is the condition. `"cba"` and `"abc"` have the
same counts but different order. Also do not pay for counts when membership or a
single running total answers the condition; the previous note's last-seen map is
smaller state for “no duplicates.”

## Fixed Width Means The Multisets Must Match

Permutation in String and Find All Anagrams in a String use a window whose width
is the target length. Since the totals are equal, the window is a permutation
exactly when every character count matches the target count.

```python
from collections import Counter


def find_anagrams(s: str, pattern: str) -> list[int]:
    width = len(pattern)
    if width > len(s):
        return []

    need = Counter(pattern)
    window = Counter(s[index] for index in range(width))
    starts: list[int] = [0] if window == need else []

    for right in range(width, len(s)):
        window[s[right]] += 1
        outgoing = s[right - width]
        window[outgoing] -= 1
        if window[outgoing] == 0:
            del window[outgoing]
        if window == need:
            starts.append(right - width + 1)

    return starts
```

For `s = "cbaebabacd"` and `pattern = "abc"`, the first window matches, the
middle windows are rejected, and the window beginning at 6 matches again, so the
answer is `[0, 6]`. Permutation in String uses the same scan and returns `True`
on the first match instead of collecting indices.

Comparing the whole maps costs `O(a)` per position for an alphabet of `a`
possible characters. When `a = 26`, that is a small fixed factor. A matched-key
counter, introduced below, removes the factor when the alphabet is not fixed.

## Distinct Values Need Counts, Not A Set

Longest Substring with At Most K Distinct Characters is the normal
[longest-valid window](02_variable_size_window.md). Grow the map, shrink while
there are too many keys, and delete only when the outgoing count reaches zero.

```python
def longest_k_distinct(s: str, k: int) -> int:
    if k <= 0:
        return 0

    counts: dict[str, int] = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        while len(counts) > k:
            outgoing = s[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        best = max(best, right - left + 1)

    return best
```

Fruit Into Baskets is this function with `k = 2` and integer fruit types. On
`"aabac"` with `k = 2`, the final `c` creates three keys. Dropping the first
two `a`s changes `a: 3` to `a: 1` but does not repair the window. Dropping the
single `b` deletes its key, finally returning the map to two distinct values.
This duplicate-heavy shrink is exactly where a set would lie.

## Turn Exactly K Into Two At-Most Questions

An **at-most** condition is easy to count. Once the window ending at `right` has
at most `k` distinct values, all `right - left + 1` suffixes inside it are valid.
An **exactly** condition does not give the same clean shrink rule.

Use subtraction:

```text
exactly k = at_most(k) - at_most(k - 1)
```

Every subarray counted by `at_most(k)` either has at most `k - 1` distinct values
or exactly `k`. Removing the first group leaves the second.

```python
def at_most_distinct(nums: list[int], k: int) -> int:
    if k < 0:
        return 0

    counts: dict[int, int] = {}
    left = 0
    total = 0

    for right, value in enumerate(nums):
        counts[value] = counts.get(value, 0) + 1
        while len(counts) > k:
            outgoing = nums[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        total += right - left + 1

    return total


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    return at_most_distinct(nums, k) - at_most_distinct(nums, k - 1)
```

Subarrays with K Different Integers uses those two passes directly. On
`[1, 2, 1]`, `at_most(2)` counts all six nonempty subarrays, while
`at_most(1)` counts the three single-value subarrays. The difference is the
three subarrays containing exactly two distinct values.

The transform is about monotonic counting, not about maps:

- Count Number of Nice Subarrays counts odd values and subtracts
  `at_most_odds(k - 1)` from `at_most_odds(k)`.
- Binary Subarrays With Sum can do the same with a running sum because every
  input is 0 or 1. The guard for a negative limit returns 0.

Negative general integers would break those at-most sum windows, just as they
break the positive-sum window in the previous note.

## Containment Uses Have, Need, And Formed

Minimum Window Substring asks for the shortest window containing every character
of `t`, including duplicates. Extra characters are allowed, so map equality is
too strict. The condition is **containment**: `have[c] >= need[c]` for every
required character.

Checking every key after every move adds an alphabet-sized scan. Instead keep:

- `need`, the fixed required counts.
- `have`, the live counts of required characters.
- `formed`, how many distinct required characters currently meet their count.

The window is valid when `formed == len(need)`.

```python
from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""

    need = Counter(t)
    have: dict[str, int] = defaultdict(int)
    formed = 0
    required = len(need)
    left = 0
    best_left = 0
    best_len = len(s) + 1

    for right, char in enumerate(s):
        if char in need:
            have[char] += 1
            if have[char] == need[char]:
                formed += 1

        while formed == required:
            if right - left + 1 < best_len:
                best_left = left
                best_len = right - left + 1

            outgoing = s[left]
            if outgoing in need:
                if have[outgoing] == need[outgoing]:
                    formed -= 1
                have[outgoing] -= 1
            left += 1

    if best_len == len(s) + 1:
        return ""
    return s[best_left : best_left + best_len]
```

The grow test happens **after** incrementing because that move may satisfy a
character. The shrink test happens **before** decrementing because that move may
make a satisfied character deficient. Surplus copies do not change `formed` in
either direction.

On `s = "AABEC"` and `t = "ABC"`, the second `A` is surplus, so `formed`
stays 1. When `C` arrives, the window becomes valid. Removing the first `A`
keeps it valid and improves `"AABEC"` to `"ABEC"`; removing the second breaks
the requirement. On `s = "ADOBE"` with the same target, `C` never arrives,
`formed` never reaches 3, and the untouched sentinel correctly returns the empty
string. That is the no-valid-cover case to test.

Number of Substrings Containing All Three Characters uses the same containment
idea with one required copy of `a`, `b`, and `c`. Shrink while all three are
present. After the loop, `left` equals the number of valid starting positions
for the current right edge, so add `left` rather than a length.

```python
def number_of_substrings(s: str) -> int:
    counts = {"a": 0, "b": 0, "c": 0}
    left = 0
    total = 0

    for char in s:
        counts[char] += 1
        while counts["a"] and counts["b"] and counts["c"]:
            counts[s[left]] -= 1
            left += 1
        total += left

    return total
```

## When The Map Describes Something Else

Several workbook problems reuse the same updates with a different meaning.

**Replace the Substring for Balanced String** counts the characters **outside**
the window. Start with counts for the entire string. Growing the candidate
replacement window decrements its incoming character from `outside`; shrinking
increments the outgoing character back. The window is valid when every outside
count is at most `len(s) // 4`, because the replacement can supply the missing
copies. If the whole string is already balanced, return 0 before scanning.

```python
from collections import Counter


def balanced_string(s: str) -> int:
    limit = len(s) // 4
    outside = Counter(s)
    if all(outside[char] <= limit for char in "QWER"):
        return 0

    left = 0
    best = len(s)
    for right, char in enumerate(s):
        outside[char] -= 1
        while all(outside[c] <= limit for c in "QWER"):
            best = min(best, right - left + 1)
            outside[s[left]] += 1
            left += 1
    return best
```

**Substring with Concatenation of All Words** treats one equal-length word as a
window unit. If each word has width `w`, run one scan for every starting offset
from 0 through `w - 1` and move by `w` each time. An unknown word clears the
current counts and jumps `left` past it; too many copies of a known word shrink
until its count fits. The `w` offset scans together visit every possible word
boundary.

```python
from collections import Counter


def find_substring(s: str, words: list[str]) -> list[int]:
    if not words:
        return []

    width = len(words[0])
    need = Counter(words)
    answer: list[int] = []

    for offset in range(width):
        have: Counter[str] = Counter()
        left = offset
        used = 0

        for right in range(offset, len(s) - width + 1, width):
            word = s[right : right + width]
            if word not in need:
                have.clear()
                used = 0
                left = right + width
                continue

            have[word] += 1
            used += 1
            while have[word] > need[word]:
                have[s[left : left + width]] -= 1
                used -= 1
                left += width

            if used == len(words):
                answer.append(left)
                have[s[left : left + width]] -= 1
                used -= 1
                left += width

    return answer
```

The offset loops perform `O(n)` word visits altogether, but Python creates and
hashes a substring of length `w` at each visit. The exact bound is therefore
`O(n * w)` time, with map state for the distinct words and temporary `O(w)`
slices.

**Minimum Window Subsequence** is the near miss. It needs the target characters
in order, not merely in matching counts. Scan forward until all target
characters have matched, then walk backward through the target to tighten that
window's start. Resume one position after that start. A frequency map cannot
distinguish the required order, which is why this problem must not be forced
into the template.

```python
def min_window_subsequence(source: str, target: str) -> str:
    if not target:
        return ""

    n, m = len(source), len(target)
    best_start = -1
    best_len = n + 1
    right = 0

    while right < n:
        target_index = 0
        while right < n and target_index < m:
            if source[right] == target[target_index]:
                target_index += 1
            right += 1
        if target_index < m:
            break

        end = right - 1
        target_index = m - 1
        start = end
        while target_index >= 0:
            if source[start] == target[target_index]:
                target_index -= 1
            start -= 1
        start += 1

        if end - start + 1 < best_len:
            best_start = start
            best_len = end - start + 1
        right = start + 1

    if best_start == -1:
        return ""
    return source[best_start : best_start + best_len]
```

The forward and backward passes use `O(1)` auxiliary space. They can revisit
source positions for different candidate ends, so the worst-case time is
`O(n * m)`, where `n` and `m` are the source and target lengths.

## Worked Example: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

You are given an uppercase string and may replace at most `k` characters. Return
the longest substring that can become one repeated character.

For a window of width `w`, keep its most frequent character and replace every
other position. If that frequency is `max_freq`, the required work is:

```text
replacements needed = w - max_freq
valid                 = w - max_freq <= k
```

This is a longest-valid window with a frequency map. The subtle decision is not
to decrease `max_freq` when the left edge moves. Recomputing the exact maximum
would scan the map after removals. The stored value is therefore a **historical
maximum** and may be stale.

> “A stale `max_freq` can let the current window remain wider than its exact
> counts justify, but it cannot create an unsupported record. The width never
> decreases in this lazy form, and `max_freq` was achieved by a real window.
> Therefore any returned width at most `max_freq + k` is attainable around that
> real group of repeated characters.”

```python
def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = {}
    left = 0
    max_freq = 0

    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        max_freq = max(max_freq, counts[char])

        if (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1

    return len(s) - left
```

The single `if` is deliberate. Each new character increases the width by one,
and one left move prevents the width from decreasing, so the maintained width is
the best width reached so far. The current characters need not form a valid
answer at the end; only that record width is returned.

Trace `s = "AABABBA"` with `k = 1`:

```text
right=0 A  counts={A:1}      max_freq=1  width=1
right=1 A  counts={A:2}      max_freq=2  width=2
right=2 B  counts={A:2,B:1}  max_freq=2  width=3
right=3 A  counts={A:3,B:1}  max_freq=3  width=4  valid record "AABA"
right=4 B  width=5 needs 2 replacements -> drop left A
           counts={A:2,B:2}  max_freq=3 is now STALE
           kept width=4; exact "ABAB" is invalid, but it does not beat record 4
right=5 B  width=5 -> drop left A, kept width=4
right=6 A  width=5 -> drop left B, kept width=4
```

The invalid `"ABAB"` is a meaningful rejected candidate. The stale count lets
it stay at the record width, but the algorithm never reports 5. If an interviewer
wants every maintained window to be literally valid, use a `while` loop and
recompute the exact maximum from the fixed 26-character alphabet; that version
is easier to prove but pays the alphabet scan.

- **Time Complexity:** `O(n)` average time, because each character updates one
  map entry and each iteration moves each boundary at most once.
- **Space Complexity:** `O(a)`, where `a` is the alphabet size. For uppercase
  English letters, the map has at most 26 keys.

## Time and Space Complexity

Let `n` be the source length, `m` a target length, `d` the number of distinct
live values, and `a` the alphabet size.

| Technique                          | Time                                                                                                 | Space                                                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Distinct-value frequency window    | `O(n)` average: both boundaries move forward and each map update is average `O(1)`                   | `O(d)`: one key is stored per distinct live value                             |
| Fixed multiset comparison          | `O(n * a)`: each slide updates in `O(1)` and compares up to `a` counts                               | `O(a)`: the target and window maps use alphabet-sized state                   |
| `have` / `need` / `formed` cover   | `O(n + m)` average: `need` reads `m` characters and each source index enters and leaves at most once | `O(d)` auxiliary, plus `O(L)` for the returned Python slice of length `L`     |
| Two at-most passes for exactly `k` | `O(n)` average: two linear scans change only the constant factor                                     | `O(d)`: the passes run one after another, so their maps are not live together |
| Recount every candidate window     | `O(n^2)` or worse: overlapping windows rebuild counts repeatedly                                     | `O(d)`: one temporary map is repeatedly discarded and rebuilt                 |

## Summary

- A **frequency map window** stores how many live copies of each value exist.
  Use it instead of a set when one copy can leave while another remains.
- Decrement the outgoing value and delete its key at zero. That makes
  `len(counts)` equal the live distinct count.
- Fixed-width anagram windows compare their multiset with the target. Variable
  containment windows allow extras and use `have`, `need`, and `formed`.
- Count exactly `k` with `at_most(k) - at_most(k - 1)`. The same transform works
  for distinct values, odd counts, and binary sums because each at-most side is
  monotonic.
- Minimum Window Substring returns an empty string when `formed` never reaches
  `required`. Always test a target the source cannot cover.
- Longest Repeating Character Replacement may keep a stale historical
  `max_freq`. It can preserve an old record width but cannot create a larger
  unsupported record.
- Counts lose order. Minimum Window Subsequence needs a forward match and a
  backward tightening pass rather than a frequency map.

## Interview Checklist

```text
Does the condition need membership, multiplicity, or a last position?
Am I deleting a frequency-map key when its count reaches zero?
Is the window fixed, making whole-map equality meaningful, or may it contain extras?
For containment, does formed change on equality after a grow and before a shrink?
If no valid cover exists, what sentinel or return value survives?
Am I counting at most k, exactly k, or every cover ending at right?
Can exactly k be written as at_most(k) - at_most(k - 1)?
Does the map describe the window, its complement, or fixed-width word units?
Does the problem care about order, which counts cannot represent?
Can I explain why a stale max_freq is safe before using it?
```
