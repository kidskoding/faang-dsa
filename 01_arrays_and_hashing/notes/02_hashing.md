# Hashing Techniques

Many array problems are slow for one reason: they repeatedly scan to answer a
question they have already asked. "Have I seen 12?", "How many times did `a`
appear?", and "Which group owns this word?" are all lookup questions.

**Hashing** stores an answer under a key so the program can return to it in
`O(1)` average time. Python gives you two hash-table containers:

- A **set** stores unique keys. Use it when the only answer is yes or no.
- A **dictionary** or **hash map** stores `key -> value`. Use it when a key needs
  an index, count, group, or other information.

The previous Python notes introduced their syntax and the requirement that keys
be [hashable](../../00_fundamentals/notes/02_python_basics.md). This note is about
choosing what the key and stored value should mean.

## Replace Repeated Scans With Stored Answers

Consider [finding whether an array contains a duplicate](https://leetcode.com/problems/contains-duplicate/).
For every value, you could scan everything before it. In the worst case that
examines `O(n²)` pairs. A set instead remembers all earlier values.

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for value in nums:
        if value in seen:
            return True
        seen.add(value)

    return False


assert contains_duplicate([4, 1, 4]) is True
assert contains_duplicate([4, 1, 7]) is False
assert contains_duplicate([]) is False
assert contains_duplicate([9]) is False
```

The order of the two lines inside the loop matters. On the first `4`, lookup is
rejected because `seen` is empty, so the code adds it. On the second `4`, lookup
succeeds and proves there are two separate occurrences. Adding before checking
would make every value appear to be its own duplicate.

```text
value=4   seen={}       lookup 4 -> REJECT, then add 4
value=1   seen={4}      lookup 1 -> REJECT, then add 1
value=4   seen={1, 4}   lookup 4 -> ACCEPT, return True
```

This is the **seen-set pattern**. The same state scales to several sets, as in
[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/): each digit must be
absent from its row set, column set, and 3-by-3 box set before being added to all
three.

## Store the Information the Lookup Must Return

A set cannot answer "where did I see it?" For [Two Sum](https://leetcode.com/problems/two-sum/),
store each earlier value's index in a dictionary. When the current value is
`value`, its needed partner is `target - value`, called the **complement**.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    index_by_value: dict[int, int] = {}

    for index, value in enumerate(nums):
        needed = target - value
        if needed in index_by_value:
            return [index_by_value[needed], index]
        index_by_value[value] = index

    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([1], 2) == []
```

Again, lookup comes before insertion. With `[3, 3]`, the first `3` cannot use
itself, so its complement lookup is rejected and index `0` is stored. The second
`3` can then use that earlier index.

The general interview question is not simply "set or dictionary?" Ask what a
successful lookup needs to give back:

- Membership needs a set.
- A matching position needs `value -> index`.
- Repetition needs `value -> count`.
- Grouping needs `signature -> list of members`.

That index mapping completes the dynamic-array swap-delete from the previous
note. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
stores `value -> index` beside a dense list. On removal, it moves the final list
value into the removed slot, updates that moved value's index, and pops the end.
A missing value is rejected before either structure changes, and inserting a
duplicate key is rejected for the same reason.

## Frequency Maps Keep Multiplicity

A **frequency map** records how many times each key appears. A set loses that
information, so it cannot distinguish `[1, 1, 2]` from `[1, 2]`.

```python
def frequencies(values: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


assert frequencies([4, 1, 4, 4]) == {4: 3, 1: 1}
assert frequencies([]) == {}
```

That one pattern prepares several workbook problems:

- [Valid Anagram](https://leetcode.com/problems/valid-anagram/) checks whether
  two strings have equal character counts.
- [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
  counts the smaller array, accepts a value from the other array only while its
  count is positive, then decrements the count.
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
  groups values by their frequency. Since no value can occur more than `n`
  times, an array of `n + 1` buckets can replace comparison sorting. A later
  [heap](../../08_heaps/notes/02_top_k.md) gives another useful solution when
  only a small `k` should be retained.

The rejected case is important for intersection. Once a stored count reaches
zero, another matching value is rejected; otherwise the output would use an
occurrence that the first array did not contain.

## Build a Key That Captures "Equivalent"

Some problems do not look up an input value directly. They first turn the value
into a **signature**, a hashable key shared by exactly the items that belong
together.

For anagrams, sorting a word's characters gives such a signature:

```text
"eat" -> "aet"
"tea" -> "aet"   same signature, same group
"tan" -> "ant"   rejects the "aet" group and starts another
```

The signature is not the answer. It is a stable name for a group. A tuple of 26
letter counts is another valid signature when the input contains only lowercase
English letters.

## Worked Example: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given a list of strings, return groups where every word in one group contains
the same characters with the same frequencies. Group order and word order do
not matter. Empty strings are valid, and all empty strings belong together.

Comparing every word against every existing group repeatedly recounts or sorts
words, which can become quadratic in the number of words. Instead, compute one
signature per word and let a dictionary find its group.

> "Two words are anagrams exactly when their sorted characters match. I will use
> that sorted string as the dictionary key and append each original word to the
> list stored under its key."

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}

    for word in words:
        signature = "".join(sorted(word))
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)

    return list(groups.values())


def normalized(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


assert normalized(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == [
    ["ate", "eat", "tea"],
    ["bat"],
    ["nat", "tan"],
]
assert group_anagrams([]) == []
assert group_anagrams([""]) == [[""]]
```

- **Time Complexity:** `O(c log w)`, where `c` is the total number of characters
  and `w` is the longest word, because sorting each word dominates its dictionary
  lookup.
- **Space Complexity:** `O(c)` including the returned groups and signature keys,
  because the stored words and keys contain a linear number of characters.

Here is the lookup trace. `tan` is the useful rejection: its signature does not
match the existing `aet` key, so it must start a new group rather than being
compared with every word already stored.

```text
word="eat"  key="aet"  lookup rejected   groups={"aet": ["eat"]}
word="tea"  key="aet"  lookup accepted   groups={"aet": ["eat", "tea"]}
word="tan"  key="ant"  rejects "aet"     groups also gets "ant": ["tan"]
word="ate"  key="aet"  lookup accepted   append to first group
word="nat"  key="ant"  lookup accepted   append to second group
word="bat"  key="abt"  lookup rejected   start third group
```

## Patterns That Change the Stored State

Once the lookup idea is clear, several harder problems differ mainly in what
they store or when they accept a candidate.

**Only start a run at its head.** In
[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/),
put every value in a set. Value `x` starts a count only if `x - 1` is absent.
If `x - 1` exists, reject `x` as a start because that sequence will be counted
from an earlier value. Each value is then visited as part of at most one accepted
run, which keeps the total average time `O(n)`.

**Make a serialized format unambiguous.** [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
is grouped here because the key lesson is representing strings without losing
boundaries. Joining on `#` fails when a string itself contains `#`. Prefix each
string with its character count and a separator instead:

```python
class Codec:
    def encode(self, words: list[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in words)

    def decode(self, encoded: str) -> list[str]:
        words: list[str] = []
        index = 0

        while index < len(encoded):
            separator = index
            while encoded[separator] != "#":
                separator += 1
            length = int(encoded[index:separator])
            start = separator + 1
            words.append(encoded[start : start + length])
            index = start + length

        return words


codec = Codec()
assert codec.decode(codec.encode(["hello", "a#b", ""])) == ["hello", "a#b", ""]
assert codec.decode(codec.encode([])) == []
```

The decoder rejects `#` inside the payload as a boundary because the recorded
length, not the next separator, determines where the string ends.

**Use a fixed number of candidates when the threshold forces it.** A value that
appears more than `n / 2` times is the only possible majority, so
[Majority Element](https://leetcode.com/problems/majority-element/) can cancel
different values in pairs and keep one candidate. For
[Majority Element II](https://leetcode.com/problems/majority-element-ii/), there
can be at most two answers above the `n / 3` threshold, so keep two candidates
and then verify their real counts in a second pass. This **Boyer-Moore voting**
family is a specialized constant-space alternative to a frequency map;
unverified candidates must be rejected because cancellation produces
possibilities, not proof.

## Time and Space Complexity

| Approach                              | Time                                                                                   | Space                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Repeated list lookup                  | `O(n²)`: up to `n` values each scan up to `n` earlier values                           | `O(1)` auxiliary: no lookup structure is stored      |
| Seen set or one-pass hash map         | `O(n)` average: each of `n` values performs constant-average-time lookup and insertion | `O(n)`: every distinct input value may be stored     |
| Frequency map                         | `O(n)` average: every value updates one expected-constant-time entry                   | `O(d)`: `d` distinct values produce at most `d` keys |
| Sort values before grouping or lookup | `O(n log n)`: comparison sorting dominates the scan                                    | `O(n)`: `sorted` creates a new list of `n` values    |

Hash-table operations are average `O(1)`, not guaranteed worst-case `O(1)`.
The [hash-table internals](05_hash_table_internals.md) note explains collisions
and the `O(n)` worst case.

## Summary

- Hashing trades `O(n)` additional space for fast lookup, which often replaces
  an `O(n²)` repeated scan with one `O(n)` average-time pass.
- A set answers membership questions, while a dictionary should be used when a
  successful lookup must return an index, count, group, or other stored state.
- Seen-set and complement patterns must usually check before inserting the
  current value, because inserting first can let one occurrence match itself.
- A frequency map preserves duplicates, which a set discards. Decrementing a
  count is what prevents one occurrence from being reused several times.
- A signature turns the exact property that defines equivalence into a stable
  key, such as sorted characters for a group of anagrams.
- Specialized problems may change the stored state: sequence heads avoid
  repeated runs, length prefixes preserve string boundaries, and Boyer-Moore
  keeps the limited number of possible majority candidates.

## Interview Checklist

```text
What repeated scan can a stored lookup replace?
Do I need membership only, or must the lookup return an index, count, or group?
Does the current element get checked before or after insertion, and why?
Do duplicates require a frequency map rather than a set?
What exact property should become the key or signature?
Can an accepted candidate be used more times than its stored frequency allows?
Am I stating hash-table time as average case rather than guaranteed worst case?
Have I tested empty input, a singleton, duplicate keys, and a rejected lookup?
```
