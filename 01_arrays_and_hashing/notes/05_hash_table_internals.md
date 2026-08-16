# Hash Table Internals

The previous notes used dictionaries and sets to avoid repeated scans. A **hash
table** is the structure underneath that fast lookup. Instead of comparing a key
with every stored key, it computes where that key should probably live.

A hash table has an array of **buckets**. A **hash function** converts a key into
an integer, and that integer is reduced to a valid bucket index:

```text
bucket_index = hash(key) % number_of_buckets
```

The table still stores the original key. Different keys can choose the same
bucket, so the hash only narrows the search; equality confirms the exact key.

## Collisions Are Normal, Not an Error

A **collision** happens when two different keys map to the same bucket. With
four buckets, integer keys `1` and `5` collide because both leave remainder `1`
after division by four.

```text
bucket 0   []
bucket 1   [(1, "one"), (5, "five")]
bucket 2   []
bucket 3   []
```

The table needs a collision strategy. Two standard strategies are:

- **Separate chaining** stores a small collection of key-value entries at each
  bucket. A collision appends to that bucket's chain.
- **Open addressing** stores entries directly in the bucket array. A collision
  probes other slots according to a rule until it finds the key or an available
  slot.

This note implements separate chaining because lookup, update, and deletion are
easy to see. Open addressing needs a special deleted marker, often called a
**tombstone**, because clearing a probed slot can make a later key unreachable.

## A Put Must Search Before It Appends

A hash map stores one value per unique key. `put(1, 10)` followed by
`put(1, 99)` updates the value for key `1`; it must not append a second entry
with the same key.

For separate chaining, every operation begins the same way:

1. Compute the bucket index.
2. Search only that bucket for an equal key.
3. Accept the equal key for `get`, update, or removal. If no key matches, reject
   the search and handle the missing-key contract.

```text
bucket [(1, 10), (5, 50)]
put(5, 55)   reject key 1, accept key 5, update its value
put(9, 90)   reject keys 1 and 5, append a new entry
```

Appending without the search creates duplicate keys. A later `get` might return
an old value, and one `remove` might leave another copy behind.

## Load Factor Controls the Expected Chain Length

The **load factor** is:

```text
number of stored entries / number of buckets
```

If a table keeps accepting entries without adding buckets, chains or probe runs
grow and lookup approaches a linear scan. Resizing keeps the number of entries
proportional to the number of buckets, which keeps the expected amount of work
inside one bucket constant when hashes are well distributed.

When the load factor crosses a chosen threshold, allocate a larger bucket array
and **rehash** every entry. Rehashing is required because `% new_capacity` can
choose a different bucket than `% old_capacity`.

```text
old capacity 4:   key 5 -> 5 % 4 = 1
new capacity 8:   key 5 -> 5 % 8 = 5
                  old bucket 1 is REJECTED after resize
```

One resize costs `O(n)`, but growing the capacity by a constant factor makes
insertion `O(1)` amortized for the same geometric-growth reason as a
[dynamic array](01_dynamic_arrays.md).

## Worked Example: [Design HashMap](https://leetcode.com/problems/design-hashmap/)

Implement `put(key, value)`, `get(key)`, and `remove(key)` without using a
built-in hash-table container. `put` inserts or updates, `get` returns the stored
value or `-1` when the key is absent, and removing a missing key changes nothing.
The problem uses nonnegative integer keys, but Python's remainder operation also
keeps negative keys inside the bucket range.

**Input**: a sequence of method calls on the object, not one array. The
constructor `MyHashMap()` takes no arguments and builds an empty map.
`put(key: int, value: int) -> None` inserts the pair or overwrites the value of
an existing key, `get(key: int) -> int` looks a key up, and
`remove(key: int) -> None` deletes a key. Keys and values are integers in the
range `0` to `10^6`, and there are at most `10^4` calls across all three methods

**Output**: only `get` returns a value. It returns the `int` most recently stored
under that key, or `-1` when the key is not in the map, which is why `-1` is
reserved as the sentinel rather than a legal stored value. `put` and `remove`
return `None` and are judged by their effect on later `get` calls; removing a key
that was never inserted is a no-op rather than an error

An array alone could store a value at `array[key]`, but that allocates for the
largest possible key rather than the number of stored entries. Separate chaining
uses a smaller bucket array and resolves collisions explicitly.

> "I will use an array of chains. Every operation hashes the key to one chain
> and then checks equality inside that chain. `put` updates an equal key before
> appending, and I will resize and rehash when the load factor exceeds 0.75."

Therefore,

1. Start with a small bucket array, here four empty chains, and a stored
   `_size` count of live entries. The count is kept rather than recomputed
   because the load factor is checked on every insertion, and summing chain
   lengths each time would defeat the purpose
2. Give every operation one shared way to find its chain, `key % len(buckets)`,
   so `put`, `get`, and `remove` always agree on where a key belongs. Python's
   remainder is nonnegative for a positive divisor, so this stays a valid index
   even if a negative key ever arrives
3. For an insertion, scan only that one chain and compare keys for equality. If a
   stored key matches, overwrite its value in place and report that nothing new
   was added, because a map holds one value per key and appending here would
   create a duplicate that a later `get` or `remove` could read or leave behind
4. If no key in the chain matches, append the new pair and increment `_size`.
   Reporting insertion separately from update is what stops an overwrite from
   inflating the count and triggering a needless resize
5. After a genuine insertion, compare `_size / len(buckets)` against the 0.75
   threshold. Crossing it means chains are getting long enough that lookups drift
   toward a linear scan, so allocate a bucket array of twice the capacity, reset
   the count, and reinsert every existing entry. The reinsertion must recompute
   each bucket index, since `% new_capacity` can land a key somewhere its old
   index does not predict
6. For a lookup, scan the key's chain and return the value of the first equal
   key. Falling off the end of the chain means the key is absent, so return the
   `-1` sentinel
7. For a removal, scan the chain the same way, delete the matching entry, and
   decrement `_size`. If the scan finds nothing, return without touching
   anything, which is the missing-key no-op the problem asks for

```python
class MyHashMap:
    def __init__(self) -> None:
        self._buckets: list[list[tuple[int, int]]] = [[] for _ in range(4)]
        self._size = 0

    def _bucket(self, key: int) -> list[tuple[int, int]]:
        return self._buckets[key % len(self._buckets)]

    def _put_without_resize(self, key: int, value: int) -> bool:
        bucket = self._bucket(key)
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return False

        bucket.append((key, value))
        self._size += 1
        return True

    def _resize(self) -> None:
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self._put_without_resize(key, value)

    def put(self, key: int, value: int) -> None:
        inserted = self._put_without_resize(key, value)
        if inserted and self._size / len(self._buckets) > 0.75:
            self._resize()

    def get(self, key: int) -> int:
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                self._size -= 1
                return


mapping = MyHashMap()
mapping.put(1, 10)
mapping.put(5, 50)  # Collides with key 1 while capacity is 4.
assert mapping.get(1) == 10
assert mapping.get(5) == 50

mapping.put(1, 99)  # Update the existing key; do not append a duplicate.
assert mapping.get(1) == 99

assert mapping.get(9) == -1
mapping.remove(9)  # Removing a missing key is a no-op.
mapping.remove(5)
assert mapping.get(5) == -1

mapping.put(2, 20)
mapping.put(3, 30)
mapping.put(4, 40)  # Crosses 0.75 load and triggers a resize.
assert [mapping.get(key) for key in (1, 2, 3, 4)] == [99, 20, 30, 40]
```

- **Time Complexity:** `get`, `put`, and `remove` are `O(1)` average time when
  keys are distributed and the load factor is bounded. One `put` can take
  `O(n)` during rehashing, but insertion is `O(1)` amortized across a sequence.
- **Space Complexity:** `O(n)` for `n` stored entries, because the resized bucket
  array stays proportional to the number of entries and each key appears once.

The collision trace shows why equality and duplicate-key handling are both
necessary:

```text
put(1, 10)    bucket 1 empty                         append (1, 10)
put(5, 50)    bucket 1 checks key 1 -> REJECT        append (5, 50)
put(1, 99)    bucket 1 checks key 1 -> ACCEPT        update, size unchanged
get(9)        checks key 1 -> REJECT, key 5 -> REJECT, return -1
remove(5)     checks key 1 -> REJECT, key 5 -> ACCEPT, delete it
```

`_put_without_resize` returns whether it inserted a new key. That distinction
prevents an update from increasing `_size` or triggering a resize unnecessarily.
During `_resize`, every entry is inserted into the new array without recursively
checking the load threshold.

## Why Average O(1) Can Become Worst-Case O(n)

The average bound assumes keys spread across the bucket array. If all `n` keys
collide, separate chaining puts them in one chain and every operation may scan
that entire chain.

```text
well distributed             worst collision pattern
bucket 0 [(8, ...)]          bucket 0 []
bucket 1 [(1, ...)]          bucket 1 [(1, ...), (5, ...), (9, ...), ...]
bucket 2 [(6, ...)]          bucket 2 []
bucket 3 [(3, ...)]          bucket 3 []
```

Resizing controls load factor, but it cannot fix a poor hash function that keeps
sending related keys together. A good hash function has two jobs: equal keys
must always get equal hashes, and ordinary unequal keys should spread well.

Python's `dict` and `set` are optimized production hash tables, so use them in
normal algorithm problems. Build one yourself only when the problem explicitly
tests the design.

## Separate Chaining Versus Open Addressing

| Collision strategy | Collision behavior                                                 | Deletion consequence                                                                             |
| ------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Separate chaining  | Store every colliding entry in the bucket's chain                  | Remove the matching chain entry; other searches still reach their keys                           |
| Open addressing    | Probe other array slots until the key or an available slot appears | Leave a tombstone rather than an ordinary empty slot, or later probe searches may stop too early |

Both can provide average `O(1)` operations with a controlled load factor and a
good hash function. Separate chaining makes the collision path explicit, while
open addressing keeps entries in one array and makes probing and deletion more
subtle.

## Time and Space Complexity

Let `n` be the number of stored entries and let `b` be the number of buckets.

| Operation or design                            | Average time                                                                        | Worst-case time                                                     | Space                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| Chained `get` or `remove`                      | `O(1)`: bounded load and distributed hashes keep the expected chain length constant | `O(n)`: all keys may occupy one chain                               | `O(n + b)`: entries and the bucket array are both stored    |
| Chained `put` without resize                   | `O(1)`: it searches one expected-constant-length chain                              | `O(n)`: duplicate detection may scan one chain containing every key | `O(n + b)`: a new key adds one stored entry                 |
| One resize and rehash                          | `O(n)`: every current entry must choose a new bucket                                | `O(n)`: every current entry still must be visited                   | `O(n + b)`: old and new bucket arrays coexist temporarily   |
| Sequence of insertions with geometric resizing | `O(1)` amortized per insert: total rehash work forms a geometric series             | `O(n)` for one insertion that triggers a resize                     | `O(n + b)`: capacity remains proportional to stored entries |

## Summary

- A hash table computes a bucket from a key's hash, then uses equality to confirm
  the exact key because a hash narrows a search but does not prove identity.
- A collision is two unequal keys choosing the same bucket. Separate chaining
  stores a collection per bucket, while open addressing probes other slots.
- `put` must search for an equal key before appending, because a map updates
  duplicate keys rather than storing several values under the same key.
- Load factor is the number of entries divided by the number of buckets.
  Resizing keeps expected chains or probe runs short, then rehashes every entry
  because the bucket calculation depends on capacity.
- Hash operations are `O(1)` average case under good distribution and `O(n)`
  worst case when every key collides. A resize makes one insertion `O(n)`, while
  geometric growth keeps a sequence at `O(1)` amortized per insertion.
- Open-addressing deletion needs a tombstone so a search does not mistake a hole
  inside a probe path for proof that the key is absent.

## Interview Checklist

```text
What does the hash function compute, and why must equality still be checked?
Which collision strategy am I using?
Does put update an existing key instead of appending a duplicate?
What value does get return when a key is missing?
Is removing a missing key a safe no-op?
What load factor triggers a resize, and why must every key be rehashed?
Can I distinguish average, worst-case, and amortized operation costs?
If I use open addressing, how does deletion preserve the probe path?
Have I tested colliding keys, duplicate keys, a missing lookup, and resize?
```
