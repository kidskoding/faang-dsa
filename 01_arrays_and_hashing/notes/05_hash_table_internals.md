# Hash Table Internals

## Pattern

A hash table maps keys to buckets using a hash function.

The goal is average `O(1)` lookup, insert, and delete.

## Intuition

Instead of scanning every key, compute where the key should live.

```text
bucket_index = hash(key) % capacity
```

Then search only that bucket.

## How It Works

A basic hash table needs:

- array of buckets
- hash function
- collision strategy
- resizing when load factor gets too high

Load factor:

```text
number of entries / number of buckets
```

When load factor grows, collisions become more common.

## Collision Handling

Two common strategies:

```text
separate chaining: each bucket stores a list of entries
open addressing: probe for another open slot
```

Python dictionaries are highly optimized, but interview hash-table implementation questions often test these ideas.

## Template: Conceptual Put

```text
index = hash(key) % capacity
bucket = buckets[index]

if key exists in bucket:
    update value
else:
    append key-value pair
```

## Complexity

Average case:

```text
get/put/delete: O(1)
space: O(n)
```

Worst case with many collisions:

```text
get/put/delete: O(n)
```

## Pitfalls

- Forgetting to update an existing key instead of appending a duplicate.
- Not resizing when load factor grows.
- Forgetting negative hash values in languages where that matters.
- Assuming hash table order is meaningful for algorithms.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I using separate chaining or open addressing, and what does each do when a bucket collides?
At what load factor do I resize, and what happens to existing entries when I do?
Does my put logic update an existing key in its bucket instead of appending a duplicate?
What is the worst-case time if every key collides into one bucket, versus the average case?
Why can't I rely on hash table iteration order for algorithm correctness?
```
