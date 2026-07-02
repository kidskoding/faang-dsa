# Bloom Filters

## Pattern

A Bloom filter is a space-efficient probabilistic set.

It can say:

```text
maybe present
or definitely not present
```

It can have false positives, but not false negatives if implemented correctly.

## Intuition

Instead of storing all keys, store several bits for each key using multiple hash functions.

To add a key, set its hashed bit positions to 1.

To query a key, check whether all its hashed bit positions are 1.

## How It Works

Add:

```text
for each hash function:
    bit_array[hash(key)] = 1
```

Contains:

```text
if all hashed positions are 1:
    maybe present
else:
    definitely not present
```

## Example

If `cat` sets bits `2`, `5`, and `9`, then querying `cat` checks those same bits.

Another word might coincidentally have those bits set by other insertions, causing a false positive.

## Complexity

Let `k` be number of hash functions.

```text
add: O(k)
contains: O(k)
space: fixed bit array size
```

## Pitfalls

- Expecting exact membership answers.
- Trying to delete without using a counting Bloom filter.
- Choosing too small a bit array and causing many false positives.
- Forgetting that Bloom filters trade correctness type for space.

## Interview Checklist

Before coding, make sure you can answer:

```text
Can this problem tolerate false positives, or does it need exact membership?
Why can a Bloom filter never produce a false negative if implemented correctly?
How does the number of hash functions k trade off false-positive rate against add/contains cost?
Why does deletion require a counting Bloom filter instead of just clearing bits?
How does bit array size affect the false-positive rate as more keys are added?
```
