# Subset Masks

A **subset mask** is one integer standing in for a subset of a fixed list of
items. Bit `i` is 1 when item `i` is in the subset and 0 when it is out, so the
integer is not being used as a quantity at all, it is being used as a membership
record. The [masks](02_masks.md) topic treated a single bit as a switch you flip;
here you read the whole row of switches at once and call it a set

The closest thing you already have is a Python `set`, or a list of booleans like
`[True, False, True]` saying which of three items you picked. A subset mask is
that list of booleans packed into one number, with the leftmost written at the
highest bit position

```text
item        c    b    a
position    2    1    0

0b000       0    0    0     the empty subset
0b001       0    0    1     {a}
0b101       1    0    1     {a, c}
0b111       1    1    1     everything, which is (1 << 3) - 1
```

Picture `n` light switches on a wall. Any configuration of that wall is a subset,
namely the switches that are up, and reading the wall left to right gives a
binary number. Counting `0, 1, 2, 3, ...` on an odometer walks every
configuration of the wall exactly once and stops after `2^n` of them, which is
the whole enumeration technique in one sentence

> This topic covers why an integer beats a real set container, the loop that
> enumerates every subset, two problems that read the bits sideways instead,
> the walk that visits only the subsets of a given set, and how a mask becomes a
> key you remember answers under

## What Breaks When A Subset Is A Real Container

You already know how to produce every subset, since
[include-or-exclude backtracking](../../09_backtracking/notes/02_subsets_combinations.md)
does it with a `path` list. So the interesting question is not how to list
subsets, it is what happens when a subset stops being output and becomes
**something you compute with**

Take a concrete shape from this module's ladder. There are 8 bags of cookies and
several children, and you hand bags out one child at a time. To avoid redoing
work you want to remember answers keyed by the set of bags already given away,
so the key is a subset and there are `2^8 = 256` of them

Represent that key as a `frozenset` of bag indices and every operation costs a
walk of the set:

```text
adding bag i          frozenset(s | {i})    O(n): a fresh container is allocated
                                            and every existing element copied in
looking the key up    memo[key]             O(n): hashing a frozenset combines
                                            one hash per element
"is this set inside
that set?"            a <= b                O(n): every element of a is probed
```

None of those is wrong, and all of them are `O(n)` for an operation that ought to
be free. Worse, the key cannot index a flat list, so you are stuck with a
dictionary and its hashing on every access

An integer fixes all of it at once, because the whole subset fits in one machine
word. Adding an item is `mask | (1 << i)`, comparing two subsets is `==` on two
numbers, "is `a` a subset of `b`" is `a & b == a`, and `dp[mask]` indexes an
ordinary list with no hashing at all. That is the trade the rest of this topic
spends: you give up readable set syntax and you get constant-time set algebra

## Counting To 2^n Walks Every Subset Once

Every subset answers `n` independent yes-or-no questions, one per item. Nested
loops would express that, one loop per item, but you cannot write `n` nested
loops when `n` is only known at runtime. Counting does the nesting for you: the
integers from `0` to `2^n - 1` are exactly the `2^n` distinct ways to fill `n`
binary digits, so one flat loop enumerates the lot

```text
mask 0 = 000   []
mask 1 = 001   ['a']
mask 2 = 010   ['b']
mask 3 = 011   ['a', 'b']
mask 4 = 100   ['c']
mask 5 = 101   ['a', 'c']
mask 6 = 110   ['b', 'c']
mask 7 = 111   ['a', 'b', 'c']
```

Reading the items back out of a mask is the [bit test](02_masks.md) you already
have, applied once per position

```python
def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    out: list[list[int]] = []
    for mask in range(1 << n):
        out.append([nums[i] for i in range(n) if mask >> i & 1])
    return out


assert subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert subsets([9]) == [[], [9]]
assert subsets([]) == [[]]
```

**Four details in four lines**:

- `range(1 << n)` is `range(2**n)` written the way everyone writes it, and it is
  half-open, so it stops at `2^n - 1`, which is the full mask and the last subset
- `mask >> i & 1` is the test, and `i` is the **item index and the bit position
  at the same time**, which is the identification the whole technique rests on.
  Mixing the two up is how a correct-looking loop returns the wrong subsets
- Mask `0` is the empty subset and it is produced on the first iteration rather
  than being special-cased, which is why `subsets([])` returns `[[]]` instead of
  `[]`. That degenerate case is a real interview probe, since the empty list has
  exactly one subset
- Nothing about the loop cares what the items are. Swap `nums` for a list of
  strings, jobs, or people and the code is unchanged, because the mask indexes
  positions rather than values

> "There are `2^n` subsets and I need all of them, so I will count from `0` to
> `2^n - 1` and read each integer as a membership record. Bit `i` set means item
> `i` is in this subset, and the empty subset falls out as mask zero"

Two facts about this enumeration are worth having ready. `mask.bit_count()` is
the **size** of the subset, since it counts set bits, with
`bin(mask).count("1")` as the fallback before Python 3.10. And the masks come out
in increasing numeric order, which means every subset is visited before all of
its supersets, because turning a 0 bit into a 1 can only make the number bigger.
That ordering is what [bitmask DP](../../17_advanced/notes/07_bitmask_dp.md)
later builds a whole fill order on

The cost is the honest limit of the technique. `2^20` is about a million, which
is fine, and `2^25` is about 33 million, which is not. When you see a problem
capping its input at 15 or 16 or 20 items, that cap is the interviewer telling
you an exponential in `n` is the intended answer

## Reading The Array Sideways, One Bit Column At A Time

*Total Hamming Distance* asks for the sum of the
[Hamming distance](01_bitwise_basics.md) over **every pair** of numbers in a
list. The direct reading is a double loop, and it is correct:

```python
total = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        total += bin(nums[i] ^ nums[j]).count("1")
```

It dies on the pair count. There are `n * (n - 1) / 2` pairs, so once `n` reaches
the thousands the loop is doing millions of popcounts to produce one number, and
the work grows as `n²` while the answer stays a single integer

The fix comes from noticing what a popcount of a XOR actually sums. Each pair
contributes 1 for every bit position where the two numbers disagree, so the grand
total is a sum over pairs **and** over positions, and those two sums can be taken
in either order. Take positions on the outside and each position becomes an
independent question: among all `n` numbers, how many pairs disagree in this one
column? If `ones` of them have the bit set, the rest have it clear, and a pair
disagrees exactly when it takes one from each group, so the column contributes
`ones * (n - ones)` with no pair ever enumerated

```text
nums = [4, 14, 2]

bit 0    0  0  0     ones=0  zeros=3   pairs=0
bit 1    0  1  1     ones=2  zeros=1   pairs=2
bit 2    1  1  0     ones=2  zeros=1   pairs=2
bit 3    0  1  0     ones=1  zeros=2   pairs=2
                                       total=6
```

```python
def total_hamming_distance(nums: list[int]) -> int:
    n = len(nums)
    total = 0
    for bit in range(32):
        ones = sum(x >> bit & 1 for x in nums)
        total += ones * (n - ones)
    return total


assert total_hamming_distance([4, 14, 2]) == 6
assert total_hamming_distance([4, 14, 4]) == 4
assert total_hamming_distance([0, 0, 0]) == 0
assert total_hamming_distance([]) == 0
```

> "Total Hamming distance is a double sum over pairs and over bit positions, and
> those are independent, so I will swap the order. Per column I only need how
> many numbers have that bit set, and the disagreeing pairs are `ones` times
> `zeros`"

The fixed `range(32)` is a width chosen because the problem promises values below
`2^31`, and it is the one place this function makes an assumption Python itself
does not make. `total_hamming_distance([])` returning `0` is the degenerate case
worth keeping, because `ones * (n - ones)` is `0 * 0` there rather than an error

## Building The Answer From The Top Bit Down

*Maximum XOR of Two Numbers in an Array* wants the largest `a ^ b` over pairs
drawn from the list. Trying every pair is `O(n²)` again, and this problem allows
lists far too long for that

The escape is to stop looking for the pair and build the **answer** instead, one
bit at a time from the most significant end. A number with bit 4 set beats every
number without it no matter what the lower bits do, because `2^4` exceeds the sum
of all smaller powers of two. So decide the top bit first, greedily, and never
revisit it

To decide a bit you need one question answered: is there a pair whose XOR starts
with the prefix I am hoping for? Keep the top few bits of every number in a set,
then for each prefix `p` ask whether `candidate ^ p` is also in the set. That
works because XOR undoes itself, from `a ^ b = c` you get `a ^ c = b`, which the
[XOR patterns](03_xor_patterns.md) topic leans on throughout. If the partner
prefix exists, some real pair produces that candidate and the bit is genuinely
achievable

```python
def max_xor_of_two_numbers(nums: list[int]) -> int:
    best = 0
    top = max(nums, default=0).bit_length() - 1
    for bit in range(top, -1, -1):
        best <<= 1
        candidate = best | 1
        prefixes = {x >> bit for x in nums}
        if any(candidate ^ p in prefixes for p in prefixes):
            best = candidate
    return best


assert max_xor_of_two_numbers([3, 10, 5, 25, 2, 8]) == 28
assert max_xor_of_two_numbers([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127
assert max_xor_of_two_numbers([8]) == 0
assert max_xor_of_two_numbers([]) == 0
```

`best <<= 1` opens a fresh low slot before each round, so `best` always holds the
prefix of the answer decided so far, and `candidate = best | 1` is the optimistic
guess that the new bit can be a 1. When the guess fails, `best` keeps the shifted
value with a 0 in that slot and the search carries on with a shorter reach

Tracing `[3, 10, 5, 25, 2, 8]`, where the largest value is 25 so the top position
is 4:

```text
bit=4   prefixes {0, 1}                  candidate 1      found     best=1
bit=3   prefixes {0, 1, 11}              candidate 11     found     best=11
bit=2   prefixes {0, 1, 10, 110}         candidate 111    found     best=111
bit=1   prefixes {1, 10, 100, 101, 1100} candidate 1111   REJECTED  best=1110
bit=0   prefixes {10, 11, 101, 1000,     candidate 11101  REJECTED  best=11100
                  1010, 11001}
```

The two `REJECTED` rows are the mechanism. At bit 1 the greedy hope was `1111`,
and no two of the four-bit prefixes XOR to it, so that bit is settled at 0
and `best` drops to `1110` permanently. Everything after that round searches only
for answers beginning `1110`, which is why the final answer is `11100`, or 28,
from `5 ^ 25`. A rejected bit is never reconsidered, because a lower bit can
never repay the loss of a higher one

## Walking Only The Subsets Of A Mask

Enumerating every mask in `range(1 << n)` answers "try all subsets of
everything". A different question comes up constantly: given a set that is
already fixed, walk **only its subsets**. Handing some of the remaining bags to
the next child is exactly that, since the bags you may give away are a subset of
the ones still unallocated

The obvious version filters the full enumeration:

```python
for sub in range(1 << n):
    if sub & mask == sub:
        ...
```

That is correct, since `sub & mask == sub` says every bit of `sub` also appears in
`mask`, but it visits all `2^n` integers to find the `2^k` that qualify, where
`k` is the number of set bits in `mask`. Do it for every mask and the total is
`4^n`, since `2^n` masks times `2^n` candidates each

The exact walk skips the rejects entirely and is one line:

```python
def subsets_of(mask: int) -> list[int]:
    out: list[int] = []
    sub = mask
    while True:
        out.append(sub)
        if sub == 0:
            break
        sub = (sub - 1) & mask
    return out


assert subsets_of(0b1010) == [0b1010, 0b1000, 0b0010, 0b0000]
assert subsets_of(0b111) == [7, 6, 5, 4, 3, 2, 1, 0]
assert subsets_of(0) == [0]
```

`sub - 1` is ordinary borrowing, established when
[clearing the lowest set bit](01_bitwise_basics.md): it turns the lowest set bit
of `sub` into a 0 and every zero beneath it into a 1. Some of those borrowed ones
land in positions that are not in `mask` at all, and `& mask` erases exactly
those, leaving the next smaller subset of `mask`

```text
mask = 1010

sub=1010    sub-1 = 1001    & mask -> 1000    bit 0 borrowed then erased
sub=1000    sub-1 = 0111    & mask -> 0010    bits 0 and 2 borrowed then erased
sub=0010    sub-1 = 0001    & mask -> 0000    bit 0 borrowed then erased
sub=0000    stop
```

Every line has a discarded piece. At `sub = 1000` the subtraction produced
`0111`, three set bits, and two of them sit outside `mask` and are thrown away on
the spot, which is what keeps the walk inside the subsets instead of wandering
into `0111`. The values fall strictly, so no subset is visited twice, and the
loop is a `while True` with the break after the append because `0` is a legitimate
subset that has to be emitted before the walk can stop

Summed over every mask this walk costs `3^n` rather than `4^n`, because each bit
independently ends up in `sub`, in `mask` but not `sub`, or in neither, which is
three choices per bit. At `n = 16` that is 43 million against 4.3 billion

## When The Mask Becomes A Key You Remember

Everything above treats masks as things to iterate. The other use is as an
**index**: `dp[mask]` or `seen[mask]` stores the answer for the situation "these
items are already dealt with", and the mask is a legal index precisely because it
is a small non-negative integer

Three problems in this module's ladder are that shape:

- *Shortest Path Visiting All Nodes* pairs a mask of visited nodes with the node
  you are standing on, which is
  [BFS over states](../../10_graphs/notes/06_implicit_state_bfs.md) with
  `(node, mask)` as the state and `mask == (1 << n) - 1` as the goal test
- *Partition to K Equal Sum Subsets* keys how full the current bucket is by the
  set of numbers already placed, so the same set reached by two different orders
  is solved once
- *Maximum Students Taking Exam* uses a mask for a **shape** rather than a set of
  consumed items, since one mask is one row of the seating chart, and the legality
  tests against the row above become shifted overlaps like `mask & (pmask << 1)`

The common thread is that two search branches which have finished the same set of
items face the same remaining problem, so the set is a complete description of
where you are. [Bitmask DP](../../17_advanced/notes/07_bitmask_dp.md) develops
that into a full technique with fill orders and sentinels; what this topic owes
you is the representation and the walks

## Worked Example: [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/)

You have bags of cookies and `k` children. Every bag goes to exactly one child
and a bag can never be split. A child's total is the sum of the bags they
receive, the **unfairness** of a distribution is the largest total any single
child ends up with, and you want the distribution that makes that largest total
as small as possible

**Input**: `cookies`, a `list[int]` of positive counts with
`2 <= len(cookies) <= 8`, where `cookies[i]` is how many cookies are in bag `i`,
and `k`, an `int` with `2 <= k <= len(cookies)`

**Output**: an `int`, the minimum achievable unfairness, meaning the smallest
value that the best-off child's total can be forced down to across all ways of
handing out the bags. It is not a sum and not an average, it is a maximum being
minimised, so the answer is always at least `max(cookies)` because whoever gets
the biggest bag has at least that many

**Recognizing it**: `len(cookies) <= 8` is the phrase that names the technique,
because `2^8` is 256 and no other reading explains a bound that small. The choice
being made is which bags go together, the order inside a child's pile is
irrelevant, and every bag must be used, so a subset is the natural unit

The naive approach is to give each bag to one of `k` children independently,
which is `k^n` assignments and 16.7 million at `k = n = 8` before any pruning.
It also repeats itself, since two searches that have handed the same set of bags
to the first child are looking at an identical remaining problem no matter which
bag they gave away first

The idea that collapses those repeats is to fill the children **one at a time**
and remember the answer for each set of bags already given out. Once child 1's
pile is fixed, all that matters about the past is which bags survive

> "I will give out one child's whole pile per round. `dp[mask]` is the best
> unfairness achievable when exactly the bags in `mask` have been handed out to
> the children processed so far, and each round I split off one submask as the
> next child's pile"

Therefore,

1. Precompute `total[mask]`, the sum of every bag in `mask`, so that scoring a
   candidate pile is one lookup instead of a loop. Build it in one upward pass
   with `total[mask] = total[mask without its lowest bag] + that bag`, using
   [`mask & -mask`](01_bitwise_basics.md) to isolate the lowest set bit and
   `bit_length() - 1` to turn that power of two back into an item index
2. Seed `dp` as a copy of `total`, which is the one-child answer: if only one
   child exists then that child receives the whole mask, so the unfairness is
   exactly the sum of those bags
3. Repeat the following round `k - 1` times, once for each additional child,
   carrying `dp` forward as "the answer using the children handled so far"
4. In a round, for every mask, walk the submasks `sub` of that mask with the
   `(sub - 1) & mask` loop. Each `sub` is a candidate pile for the newly added
   child, and `mask ^ sub` is what the earlier children had to share
5. Score a candidate as `max(dp[mask ^ sub], total[sub])`, because unfairness is
   a maximum: either the worst-off outcome is already inside the earlier
   children's split, or it is this new child's own pile. Keep the smallest score
   over all submasks, since you are minimising that maximum
6. Answer `dp[(1 << n) - 1]` after the last round, which is the state where every
   bag has been handed out and all `k` children have been processed

```python
from math import inf


def distribute_cookies(cookies: list[int], k: int) -> int:
    n = len(cookies)
    total = [0] * (1 << n)
    for mask in range(1, 1 << n):
        low = mask & -mask
        total[mask] = total[mask ^ low] + cookies[low.bit_length() - 1]
    dp = total[:]
    for _ in range(k - 1):
        nxt = [inf] * (1 << n)
        for mask in range(1 << n):
            sub = mask
            while True:
                nxt[mask] = min(nxt[mask], max(dp[mask ^ sub], total[sub]))
                if sub == 0:
                    break
                sub = (sub - 1) & mask
        dp = nxt
    return int(dp[(1 << n) - 1])


assert distribute_cookies([8, 15, 10, 20, 8], 2) == 31
assert distribute_cookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7
assert distribute_cookies([1, 2, 3], 3) == 3
assert distribute_cookies([5], 1) == 5
```

The `sub = 0` case gives the new child nothing, and it is left in rather than
guarded against, because it is legal and never wins whenever `k <= n`. The
`total[:]` copy is what makes round one mean "one child", and starting `dp` at
all zeros instead would claim a distribution with zero unfairness exists

Trace `cookies = [3, 7, 1, 8]` with `k = 2`, so bit 0 is bag 3, bit 1 is bag 7,
bit 2 is bag 1, and bit 3 is bag 8. After the seed, `dp[mask]` is just
`total[mask]`, and the final round walks the submasks of `1111`:

```text
child 2 gets 1111  sum=19 | child 1 gets 0000  sum= 0  -> max=19  TAKE   best=19
child 2 gets 1110  sum=16 | child 1 gets 0001  sum= 3  -> max=16  TAKE   best=16
child 2 gets 1101  sum=12 | child 1 gets 0010  sum= 7  -> max=12  TAKE   best=12
child 2 gets 1100  sum= 9 | child 1 gets 0011  sum=10  -> max=10  TAKE   best=10
child 2 gets 1011  sum=18 | child 1 gets 0100  sum= 1  -> max=18  REJECT best=10
child 2 gets 1010  sum=15 | child 1 gets 0101  sum= 4  -> max=15  REJECT best=10
child 2 gets 1001  sum=11 | child 1 gets 0110  sum= 8  -> max=11  REJECT best=10
child 2 gets 1000  sum= 8 | child 1 gets 0111  sum=11  -> max=11  REJECT best=10
child 2 gets 0111  sum=11 | child 1 gets 1000  sum= 8  -> max=11  REJECT best=10
child 2 gets 0110  sum= 8 | child 1 gets 1001  sum=11  -> max=11  REJECT best=10
child 2 gets 0101  sum= 4 | child 1 gets 1010  sum=15  -> max=15  REJECT best=10
child 2 gets 0100  sum= 1 | child 1 gets 1011  sum=18  -> max=18  REJECT best=10
child 2 gets 0011  sum=10 | child 1 gets 1100  sum= 9  -> max=10  REJECT best=10
child 2 gets 0010  sum= 7 | child 1 gets 1101  sum=12  -> max=12  REJECT best=10
child 2 gets 0001  sum= 3 | child 1 gets 1110  sum=16  -> max=16  REJECT best=10
child 2 gets 0000  sum= 0 | child 1 gets 1111  sum=19  -> max=19  REJECT best=10
```

The answer is 10, from splitting `{7, 3}` against `{8, 1}`. Two rejections are
worth naming. The row where child 2 takes `0011` scores 10 as well and is still
rejected, because the comparison is a strict `<` inside `min`, so an equal
candidate changes nothing and the mirror split is discarded. The row where child
2 takes `1000`, a single bag of 8, looks appealing and scores 11, since the other
three bags sum to 11 and the maximum is what counts. Grabbing the biggest bag
alone is exactly the greedy move that loses here

Notice the walk visits both `1100` and `0011`. Every split is generated twice,
once from each side, and that redundancy is the price of the submask loop being
one line

- **Time Complexity:** `O(k * 3^n)`, where `n` is the number of bags and `k` the
  number of children, because each of the `k - 1` rounds walks the submasks of
  every mask and that total is `3^n` since each bit is in the submask, in the
  mask only, or in neither
- **Space Complexity:** `O(2^n)` for the `total`, `dp`, and `nxt` lists, which
  hold one number per subset and are the only allocations that scale, with the
  rounds reusing them rather than keeping one table per child

## Time and Space Complexity

Throughout, `n` is the number of items packed into the mask, `w` is the bit width
of a value which is 32 for the problems here, and `k` is the number of children
in the distribution problem

**Enumerating subsets**

| Approach                                                                  | Time                                                                                                         | Space                                                                                                          |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `for mask in range(1 << n)`, materialising each subset                    | `O(n * 2^n)`: `2^n` masks, each read bit by bit to collect its items                                         | `O(n * 2^n)`: the output holds `2^n` lists averaging `n / 2` items, and the loop itself allocates nothing else |
| `for mask in range(1 << n)`, scoring each subset with a precomputed table | `O(2^n)`: one lookup per mask, since nothing walks the bits                                                  | `O(2^n)`: one number per subset in the table                                                                   |
| Include-or-exclude recursion over items                                   | `O(n * 2^n)`: the same leaf count, since the recursion tree has `2^n` leaves and copying a path costs `O(n)` | `O(n)` auxiliary beyond the output: the call stack is `n` deep and one shared path list is carried down        |

**Subsets of a given mask**

| Approach                                                           | Time                                                                                                        | Space                                                                                                 |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `sub = (sub - 1) & mask`, done for every mask                      | `O(3^n)`: each bit is in the submask, in the mask only, or in neither, giving 3 independent choices per bit | `O(1)` auxiliary: the walk holds one integer and reads whatever table the caller built                |
| Filtering `range(1 << n)` with `sub & mask == sub`, for every mask | `O(4^n)`: `2^n` masks each scanning all `2^n` candidates, most of which fail the test                       | `O(1)` auxiliary: the waste is entirely in time, which is why this version submits and then times out |

**The list problems in this section**

| Approach                                         | Time                                                                                                              | Space                                                                               |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| *Total Hamming Distance* by bit column           | `O(n * w)`: one pass over the list per bit position, and the pairs are counted arithmetically rather than visited | `O(1)`: a running total and a per-column count of set bits                          |
| *Total Hamming Distance* by every pair           | `O(n² * w)`: `n(n - 1)/2` pairs, each costing a popcount of the XOR                                               | `O(1)`: the space is fine, so only the time separates the two                       |
| *Maximum XOR* by building the answer downward    | `O(n * w)`: `w` rounds, each rebuilding a prefix set of `n` entries and probing it                                | `O(n)`: the prefix set holds at most one entry per number and is rebuilt each round |
| *Maximum XOR* by every pair                      | `O(n²)`: one XOR per pair, with no popcount needed since only the maximum matters                                 | `O(1)`: a single running best                                                       |
| *Fair Distribution of Cookies* by submask splits | `O(k * 3^n)`: `k - 1` rounds over the submask walk across all masks                                               | `O(2^n)`: three lists of one number per subset                                      |

The `2^n` and `3^n` rows are the reason this technique carries a size limit
rather than a warning. Subset enumeration is comfortable to about `n = 20`, the
submask walk to about `n = 16`, and past those the loop is not slow, it is
impossible

## Summary

- A **subset mask** is a single integer used as a membership record over a fixed
  list of items, where bit `i` is 1 when item `i` is in the subset. The empty
  subset is mask `0`, the full subset is `(1 << n) - 1`, and `mask.bit_count()`
  is the number of items in it
  - The item index and the bit position are the same number, and confusing the
    two produces subsets that look plausible and are wrong
- The reason to prefer an integer over a `frozenset` is cost per operation.
  Adding an item is `mask | (1 << i)`, testing membership is `mask >> i & 1`,
  containment is `a & b == a`, and equality is one integer comparison, where the
  real container charges `O(n)` for each of those and cannot index a flat list
- `for mask in range(1 << n)` enumerates every subset exactly once, because the
  integers below `2^n` are precisely the `2^n` ways to fill `n` binary digits.
  This is the loop behind *Subsets*, and it replaces `n` nested loops that you
  cannot write when `n` is only known at runtime
  - Masks arrive in increasing numeric order, so every subset is visited before
    all of its supersets, since setting a bit only makes the number bigger
  - A list with no items has exactly one subset, the empty one, which is why
    `subsets([])` must return `[[]]` rather than `[]`
- Some problems want the bits read **sideways**, one column across all the
  numbers, instead of one number at a time. *Total Hamming Distance* is the
  example, where a column with `ones` set bits contributes `ones * (n - ones)`
  disagreeing pairs, turning an `O(n²)` pair scan into `O(n * w)` for width `w`
- *Maximum XOR of Two Numbers* builds the answer from the top bit down rather
  than searching for the pair, because a higher bit outweighs every lower bit
  combined. Each round keeps the top bits of every number in a set and asks
  whether `candidate ^ prefix` is also present, which works because `a ^ b = c`
  implies `a ^ c = b`
  - A bit rejected in one round is settled at 0 forever, since no combination of
    lower bits can make up the difference
- **Submask enumeration** walks only the subsets of a given `mask` using
  `sub = (sub - 1) & mask`, starting from `sub = mask` and emitting `0` before
  the loop stops. Subtracting one clears the lowest set bit and borrows ones
  beneath it, and the `& mask` erases the borrowed ones that fall outside the set
  - Across all masks this is `O(3^n)` rather than the `O(4^n)` of filtering the
    full enumeration, because each bit is in the submask, in the mask only, or in
    neither
  - Every two-way split is generated twice, once from each side, which is
    harmless when you are taking a minimum or a maximum
- A mask is also an **index**, so `dp[mask]` remembers the answer for "exactly
  these items are dealt with". That is what lets *Fair Distribution of Cookies*
  hand out one child's whole pile per round and score a split as
  `max(dp[mask ^ sub], total[sub])`, and it is the same representation behind
  *Partition to K Equal Sum Subsets* and the `(node, mask)` states of
  *Shortest Path Visiting All Nodes*
- The costs are `O(n * 2^n)` to list every subset, `O(2^n)` to score them from a
  table, and `O(3^n)` to walk submasks across all masks, with `O(2^n)` space for
  a table keyed by subset. Enumeration stays usable to roughly `n = 20` and the
  submask walk to roughly `n = 16`, which is why problems that intend this
  technique announce it with a tiny cap on `n`

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
What is the cap on n, and does 2^n or 3^n fit inside my time budget?
What does one bit mean here: an item taken, a node visited, or a seat filled?
Is item index i the same number as bit position i everywhere in my loop?
Does my loop include mask 0, and is the empty subset a legal answer?
Do I need all 2^n subsets, or only the subsets of one particular mask?
For a submask walk, do I emit 0 before breaking rather than after the test?
Am I iterating over items when the columns are independent and I could iterate
  over bit positions instead?
Can I decide the answer bit by bit from the top instead of searching for a pair?
Is the mask the whole state, or do I also need the node I am standing on?
Am I precomputing a per-mask table so scoring a subset is a lookup, not a loop?
What does the degenerate input do: an empty list, one item, or k equal to n?
```
