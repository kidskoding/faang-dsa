# Hashing Techniques

## Pattern

Hashing uses a hash map or hash set to turn repeated lookup into average `O(1)` work.

Use a hash set when you only care whether something exists. Use a hash map when you need to store information for a key.

## Intuition

Many brute-force array problems check every pair or every previous value.

A hash table lets you ask:

```text
Have I seen the value I need already?
```

That often changes `O(n^2)` scans into `O(n)` passes.

## How It Works

Common hash-map roles:

- value -> index
- value -> frequency
- prefix sum -> count
- sorted signature -> group
- node -> cloned node
- state -> best distance

Common hash-set roles:

- seen values
- visited nodes
- duplicate detection
- membership lookup

## Template: Seen Set

```text
seen = set()
for x in nums:
    if x in seen:
        found duplicate or pair
    seen.add(x)
```

## Template: Frequency Map

```text
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

## Template: Complement Lookup

```text
seen = {}
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        return seen[need], i
    seen[x] = i
```

## Complexity

Average case:

```text
lookup/insert/delete: O(1)
full pass: O(n)
space: O(n)
```

Worst-case hash collisions can degrade, but interview analysis usually uses average-case hashing unless the problem asks otherwise.

## Pitfalls

- Adding the current value before checking when that would allow using the same element twice.
- Forgetting frequencies when duplicates matter.
- Using a set when you need counts or indices.
- Assuming dictionary iteration is sorted.
- Mutating a key object after putting it in a hash table.

## Interview Checklist

Before coding, make sure you can answer:

```text
Do I actually need counts/indices (hash map) or just membership (hash set)?
Am I checking membership before or after adding the current element, and does that order allow reusing the same element incorrectly?
Would duplicates break my answer if I used a set instead of a frequency map?
Is my key hashable, and am I mutating it after inserting it into the table?
Am I relying on dictionary iteration order for correctness?
```
