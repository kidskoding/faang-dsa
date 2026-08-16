# XOR Patterns

You already know from [bitwise basics](01_bitwise_basics.md) that `^` sets a bit
exactly where its two operands disagree. This topic is about the consequence of
that rule rather than the rule itself, and the consequence is that **XOR is its
own inverse**. Applying the same value twice returns you to where you started,
because the second application disagrees with the first in exactly the positions
the first one changed, so it undoes every one of them

That single property is what separates XOR from the running total you would
normally reach for. A running sum remembers everything ever added to it, and
recovering one contribution means subtracting it back out deliberately. A running
XOR forgets in pairs, all by itself, without being told which values were
duplicates. Feed it a value twice and it is as though you never fed it anything

The mental picture is a bank of light switches. Each bit of the accumulator is a
switch, and XOR-ing in a value flips the switches named by that value's set bits.
Flip a switch once and it changes, flip it a second time and it is back where it
started. At the end of any sequence of flips, a switch is on exactly when it was
named an odd number of times, and nothing else about the order or the grouping
matters

> This topic covers the identities that make values cancel, folding an array down
> to the value that survives, cancelling one collection against another, undoing a
> chained encoding, and the two problems where a plain fold is not enough

## Counting Occurrences, And The Constraint That Rules It Out

[Single Number](https://leetcode.com/problems/single-number/) hands you a list
where every value appears twice except one, and wants that one value. The obvious
solution is to count

```python
from collections import Counter


def single_number_counting(nums: list[int]) -> int:
    counts = Counter(nums)
    for value, seen in counts.items():
        if seen == 1:
            return value
    return -1


assert single_number_counting([4, 1, 2, 1, 2]) == 4
assert single_number_counting([1]) == 1
assert single_number_counting([]) == -1
```

This is correct, it is linear, and it is still the wrong answer in the interview,
because the problem statement asks for a solution using constant extra space and
the map holds one entry per distinct value. On a list of a million values with
half a million distinct ones, that map is half a million entries used to produce a
single integer

The failure is specific, and it points at what has to change. The counting
approach stores a value in order to remember it, when the only fact it ever reads
back is whether the count was even or odd. You do not need the counts, you need
the parity of the counts, and parity is the one thing an accumulator can track
without growing

## The Four Identities That Make Values Disappear

Everything in this topic rests on four facts, each of which follows from XOR
marking disagreement

- **A value cancels itself**, so `a ^ a == 0`, because a number never disagrees
  with itself in any position
- **Zero is the identity**, so `a ^ 0 == a`, because a zero bit never disagrees
  with whatever it meets, and so leaves the other operand alone
- **Order does not matter**, so `a ^ b == b ^ a`, because "these two bits differ"
  is a question with the same answer whichever one you name first
- **Grouping does not matter**, so `(a ^ b) ^ c == a ^ (b ^ c)`, because each
  column ends up set when an odd number of the operands have a 1 there, and
  counting to odd does not care how you bracket the values

```python
a, b, c = 12, 10, 7

assert a ^ a == 0
assert a ^ 0 == a
assert (a ^ b) ^ b == a
assert a ^ b == b ^ a
assert (a ^ b) ^ c == a ^ (b ^ c)
```

The `(a ^ b) ^ b == a` line is the self-inverse property written out, and it is
the one to have at your fingertips, because every decoding problem in this topic
is that line applied to a different pair of names

The reason the last two hold is worth naming precisely, since it is also the
reason the third-copy problem later in this topic needs a different tool. **XOR is
column-wise addition modulo 2.** Each output column is the sum of the input
columns with the carry thrown away, which is exactly what "keep the remainder
after dividing by 2" means. You met that framing in
[Sum of Two Integers](02_masks.md), where `a ^ b` was described as the sum with
every carry dropped

Put those together and you get the statement the whole topic runs on. XOR-ing a
whole collection together gives a result whose bit at each position is set exactly
when an **odd number** of the inputs had a 1 there. Any value appearing an even
number of times contributes nothing at all

## Folding An Array Down To Its Odd One Out

Since order and grouping are free, you may pretend the list arrives sorted with
every pair adjacent, even though it does not. `4 ^ 1 ^ 2 ^ 1 ^ 2` rearranges to
`4 ^ (1 ^ 1) ^ (2 ^ 2)`, which is `4 ^ 0 ^ 0`, which is `4`

```python
def single_number(nums: list[int]) -> int:
    answer = 0
    for value in nums:
        answer ^= value
    return answer


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
```

> "Every paired value cancels itself out no matter where its partner sits, since
> XOR is commutative and associative, so folding the whole array leaves only the
> value with no partner. That is one pass and one integer of state, which meets
> the constant-space requirement the hash map missed"

Two details in that loop carry the weight. The accumulator starts at `0` rather
than at `nums[0]`, because zero is the identity, so an empty list correctly folds
to zero and no special case is needed for a one-element list. There is also no
early exit and no test inside the loop, since the accumulator is meaningless until
the final value has been folded in, which the next trace makes concrete

## Cancelling One Collection Against Another

The fold does not care whether the values it cancels came from the same place. If
two collections are identical except for one extra item, XOR-ing everything from
both together cancels the shared items pairwise and leaves the extra one standing

[Missing Number](https://leetcode.com/problems/missing-number/) is that idea with
the two collections being the indices `0..n` and the values in the array. Every
number in `0..n` except the missing one appears once as an index and once as a
value, so it meets its own partner and vanishes

```python
def missing_number(nums: list[int]) -> int:
    answer = len(nums)
    for index, value in enumerate(nums):
        answer ^= index ^ value
    return answer


assert missing_number([3, 0, 1]) == 2
assert missing_number([0, 1]) == 2
assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert missing_number([0]) == 1
assert missing_number([1]) == 0
```

The seed is `len(nums)` rather than `0`, and that is the line people drop. The
array has `n` slots, so `enumerate` produces indices `0` through `n - 1` and never
produces `n` itself, even though `n` is one of the candidate answers. Seeding with
`len(nums)` puts the missing index into the fold by hand. The assert on `[0]`
proves it, since the answer there is `1`, which no index in the loop ever supplies

The same shape solves
[Find the Difference](https://leetcode.com/problems/find-the-difference/), where
`t` is `s` with one extra character inserted somewhere. Characters are not
integers, so fold their code points with `ord` and convert the survivor back

```python
def find_the_difference(s: str, t: str) -> str:
    acc = 0
    for ch in s + t:
        acc ^= ord(ch)
    return chr(acc)


assert find_the_difference("abcd", "abcde") == "e"
assert find_the_difference("", "y") == "y"
assert find_the_difference("a", "aa") == "a"
```

Concatenating the two strings and folding the result is the whole solution,
because a character present in both strings is fed in twice and cancels, so
nothing needs to know which string a character came from. The `("a", "aa")` case
is the one that catches a solution built on sets instead, since the answer there
is a character that also appears in `s`, and a set-difference approach reports
nothing

## Dry Run: Cancelling Indices Against Values

Take `nums = [3, 0, 1]`, so `n` is `3` and the missing value is `2`

```text
start                 answer = 3        seeded with len(nums)
index 0, value 3      answer = 0        3 ^ 0 ^ 3
index 1, value 0      answer = 1        0 ^ 1 ^ 0
index 2, value 1      answer = 2        1 ^ 2 ^ 1
```

The step to look at is the first one, where the accumulator lands on `0`. That
value has to be discarded rather than believed, and it is discarded silently by
the loop simply continuing. Zero is a perfectly legal answer for this problem,
since `0` is one of the numbers that could be missing, so a reader watching the
accumulator would have every reason to think the answer had arrived. It has not.
A partial XOR is not a partial answer, it is a fingerprint of the prefix consumed
so far, and it only becomes meaningful once every index and every value has been
folded in

The line above it shows the cancellation doing its job. The seed `3` met index `0`
and value `3`, and the `3` from the seed annihilated the `3` from the array even
though one came from the seed and the other from the input, because XOR has no
notion of where a value came from

## Undoing One Link At A Time

[Decode XORed Array](https://leetcode.com/problems/decode-xored-array/) gives you
`encoded`, where `encoded[i] = arr[i] ^ arr[i + 1]`, plus the value of `arr[0]`,
and asks for the original array back. Recovering `arr[i + 1]` from those two known
quantities is exactly the self-inverse identity with the names changed

```text
encoded[i]              =  arr[i] ^ arr[i + 1]
arr[i] ^ encoded[i]     =  arr[i] ^ arr[i] ^ arr[i + 1]
                        =  0 ^ arr[i + 1]
                        =  arr[i + 1]
```

XOR-ing both sides by `arr[i]` cancels it on the right, because a value met twice
disappears, and leaves the neighbour alone. Knowing one element therefore unlocks
the next, and one left-to-right pass unrolls the whole chain

```python
def decode(encoded: list[int], first: int) -> list[int]:
    arr = [first]
    for e in encoded:
        arr.append(arr[-1] ^ e)
    return arr


assert decode([1, 2, 3], 1) == [1, 0, 2, 1]
assert decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
assert decode([], 5) == [5]
```

`arr[-1]` is always the element decoded on the previous iteration, so the loop
needs no index bookkeeping. The empty-input case returns `[first]` rather than an
empty list, because an array of one element has no adjacent pairs and so encodes
to nothing

This is the same telescoping that makes
[prefix sums](../../01_arrays_and_hashing/notes/03_prefix_suffix_sums.md) work,
with XOR in place of addition and no need for a separate inverse operation, since
XOR is its own. That is why a running XOR is often called a prefix XOR, and why
the trick generalises to any problem that hands you differences and one anchor

## When The Copies Come In Threes

[Single Number II](https://leetcode.com/problems/single-number-ii/) changes one
word. Every value now appears **three** times except one, which appears once, and
that word breaks the fold completely

```text
a ^ a ^ a  =  (a ^ a) ^ a  =  0 ^ a  =  a
```

Three copies of a value XOR down to one copy of it rather than to zero, so nothing
cancels and the fold returns some mixture of every distinct value in the array.
The failure is not an edge case, it is total

It also says exactly what to fix. XOR is per-column addition modulo 2, and 2 is
the wrong modulus for a problem built out of threes. Count each column properly
and take it modulo 3 instead. A value appearing three times contributes `3` to
every column it has a 1 in, which vanishes under modulo 3, while the lone value
contributes `1` to each of its columns and survives

> "The XOR fold is addition mod 2 per bit column, and here the duplicates come in
> threes, so I want the same idea mod 3. I will count the set bits in each of the
> 32 columns, take each count mod 3, and any column whose remainder is non-zero is
> a column where the singleton has a 1"

```python
def single_number_ii(nums: list[int]) -> int:
    answer = 0
    for bit in range(32):
        column = sum((value >> bit) & 1 for value in nums)
        if column % 3:
            answer |= 1 << bit
    return answer if answer < (1 << 31) else answer - (1 << 32)


assert single_number_ii([2, 2, 3, 2]) == 3
assert single_number_ii([0, 1, 0, 1, 0, 99, 1]) == 99
assert single_number_ii([-2, -2, 1, -2]) == 1
assert single_number_ii([-4, -4, -4, -2]) == -2
assert single_number_ii([7]) == 7
```

Working `[2, 2, 3, 2]` column by column shows all three cases in four values

```text
bit index        1   0
2                1   0
2                1   0
3                1   1
2                1   0
                ---------
column sum       4   1
mod 3            1   1
answer           1   1     = 3
```

Column 1 is the interesting one. Four values have a bit there, and four is not a
multiple of three, so the column survives with remainder `1`. The three copies of
`2` accounted for three of those bits and cancelled among themselves, leaving the
one contributed by `3`. Column 0 had a single contributor and passed straight
through, and every column above these two summed to zero and was rejected

The fixed range of 32 and the subtraction at the end are the negative-number
handling from [masks](02_masks.md), and they are mandatory here rather than
decorative. The problem allows negative inputs, and Python treats a negative
integer as though its sign bit repeats forever to the left, so an unbounded loop
over bit positions would never terminate. Capping the loop at 32 columns and then
reinterpreting bit 31 as the sign is what imposes the width the problem assumes

## Worked Example: [Single Number III](https://leetcode.com/problems/single-number-iii/)

Every value in the list appears exactly twice except for **two** values, which
each appear once. Return those two values

**Input**: `nums`, a `list[int]` in which exactly two values appear once and every
other value appears exactly twice, so the length is always even and at least 2.
Values may be negative

**Output**: a `list[int]` of length 2 holding the two values that appear once. The
order is not fixed, so returning them either way round is accepted, which means
you never have to reason about which one you found first

**The approach**: this is Single Number with the survivors doubled, and folding
everything together is still the right first move, but it no longer finishes the
job. The fold returns `x ^ y` for the two singletons, which is a real fact about
them and not either of them. The hash map that would separate them is banned by
the same constant-space requirement as before

What rescues it is that `x ^ y` is guaranteed non-zero, because the two singletons
are different values, and a non-zero XOR means there is at least one bit position
where they disagree. Pick any such position and it splits the entire array into
two halves that each contain exactly one singleton, since a duplicate pair is two
copies of one value and therefore always lands on the same side. Fold each half
separately and each fold returns its own singleton

> "Folding everything gives me the XOR of the two answers rather than the answers.
> Any set bit in that result is a position where the two differ, so I will
> partition the array on that bit. Each duplicate pair stays together because both
> copies are the same number, and the two singletons are forced apart, so each side
> is a Single Number problem I already know how to solve"

Therefore,

1. Fold the whole array with XOR to get `diff`, which is `x ^ y`, because every
   duplicate pair cancels and only the two singletons survive. This value is not
   an answer, and saying so out loud avoids the mistake of returning it
2. Choose a bit position where `diff` has a 1, which is a position where `x` and
   `y` disagree. Any set bit works, so take the lowest with `diff & -diff` from
   [bitwise basics](01_bitwise_basics.md), which isolates it in one operation
   rather than looping to find one
3. Confirm the choice is always available, since `x` and `y` are distinct values,
   so `diff` cannot be zero and therefore has at least one set bit to pick
4. Walk the array a second time and route each value by testing it against that
   isolated bit, sending values with the bit set to one accumulator and everything
   else to the other
5. Trust that the routing keeps duplicates together, because two copies of the
   same value give the same answer to the same test, so a pair can never be split
   across the two accumulators and will always cancel inside whichever one it lands
   in
6. Return both accumulators, each of which is now a full XOR fold over a group
   holding one singleton and some number of cancelling pairs, so each holds its
   group's singleton

```python
def single_number_iii(nums: list[int]) -> list[int]:
    diff = 0
    for value in nums:
        diff ^= value
    lowest = diff & -diff
    first = second = 0
    for value in nums:
        if value & lowest:
            first ^= value
        else:
            second ^= value
    return [first, second]


assert sorted(single_number_iii([1, 2, 1, 3, 2, 5])) == [3, 5]
assert sorted(single_number_iii([9, 9, 4, 7])) == [4, 7]
assert sorted(single_number_iii([-1, 0])) == [-1, 0]
assert sorted(single_number_iii([0, 1])) == [0, 1]
```

Tracing `[1, 2, 1, 3, 2, 5]`, the first pass folds everything down

```text
value 1     diff = 1
value 2     diff = 3
value 1     diff = 2
value 3     diff = 1
value 2     diff = 3
value 5     diff = 6
```

The answers are `3` and `5`, and `3 ^ 5` is `6`, so the fold delivered what it
promised. Now look at which bit to split on

```text
bit index      2   1   0
diff = 6       1   1   0
                       ^ this column is 0, and it is the one to reject
3              0   1   1
5              1   0   1
```

Bit 0 is the rejected candidate, and it is rejected because `diff` has a 0 there,
which means `3` and `5` agree in that column since both are odd. Splitting on it
would send both singletons into the same group, where they would cancel each other
and leave that group holding `3 ^ 5`, which is `6`, and the other group holding
`0`. Running that split confirms it, and neither number returned is an answer.
Only a column where `diff` holds a 1 separates them, which is precisely what
`diff & -diff` guarantees

Splitting on bit 1 instead, which `diff` does have set, routes the six values like
this

```text
value 1   bit 1 clear   -> group B     B = 1
value 2   bit 1 set     -> group A     A = 2
value 1   bit 1 clear   -> group B     B = 0
value 3   bit 1 set     -> group A     A = 1
value 2   bit 1 set     -> group A     A = 3
value 5   bit 1 clear   -> group B     B = 5
```

Both copies of `1` went to B and cancelled, both copies of `2` went to A and
cancelled, and the two singletons ended up on opposite sides, leaving `A = 3` and
`B = 5`

- **Time Complexity:** `O(n)` for `n` values, because the array is walked exactly
  twice, once to build `diff` and once to route values, and every step in both
  passes is a single constant-time bitwise operation
- **Space Complexity:** `O(1)`, because the state is four integers regardless of
  input size, and the returned pair is fixed at two elements rather than growing
  with `n`

## Time and Space Complexity

Throughout, `n` is the number of input values, `d` is the number of **distinct**
values, which is roughly `n / 2` for the paired problems, and `w` is the bit width
of a value, which is 32 for every problem in this module

**One value appears once, the rest appear twice**

| Approach                                          | Time                                                                                                    | Space                                                                                                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XOR fold                                          | `O(n)`: one XOR per value in a single pass, with no comparison, lookup, or hash computation per element | `O(1)`: one integer accumulator, which is what the problem's constant-space requirement demands                                                           |
| Counting with a hash map                          | `O(n)`: one hash and one increment per value, then a scan of the map                                    | `O(d)`: one entry per distinct value, so a million-element input with half a million distinct values stores half a million entries to produce one integer |
| Sorting, then scanning for the unpaired neighbour | `O(n log n)`: the comparison sort dominates, and the pairing scan afterwards is linear                  | `O(n)`: a sort that may not mutate the caller's list needs a copy, and even an in-place sort destroys the input order                                     |

**One value appears once, the rest appear three times**

| Approach                  | Time                                                                                                                                                                               | Space                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Per-column count modulo 3 | `O(n * w)`: each of the 32 columns is summed over all `n` values, and `w` is a fixed 32 rather than a function of the input, so this is linear in `n` with a constant factor of 32 | `O(1)`: an answer accumulator and one column counter                                         |
| XOR fold                  | wrong at any cost, because `a ^ a ^ a` is `a` rather than `0`, so three copies never cancel and no amount of time fixes it                                                         | `O(1)`: the space is fine, which is why this one is tempting to submit                       |
| Counting with a hash map  | `O(n)`: one increment per value, and it beats the per-column version on constant factors                                                                                           | `O(d)`: one entry per distinct value, which the problem's constant-space follow-up rules out |

**Two values appear once, the rest appear twice**

| Approach                            | Time                                                                                                                        | Space                                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Fold, then split on a differing bit | `O(n)`: two linear passes, one to compute `diff` and one to route each value into its group, with constant work per element | `O(1)`: `diff`, the isolated bit, and two accumulators, none of which grow with `n`         |
| Counting with a hash map            | `O(n)`: one increment per value plus a final scan for the two entries with count 1                                          | `O(d)`: one entry per distinct value again, and the reason the bit-splitting version exists |

**The cross-collection and chain folds**

| Problem               | Time                                                                                                              | Space                                                                                                                                          |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| *Missing Number*      | `O(n)`: one pass folding each index together with its value, plus the seed                                        | `O(1)`: a single accumulator, and unlike the sum-formula solution every intermediate value stays inside the bit width of the inputs themselves |
| *Find the Difference* | `O(m)`: where `m` is the combined length of the two strings, since every character of both is folded exactly once | `O(1)` auxiliary in principle, though `s + t` as written builds a concatenated copy costing `O(m)`, which two separate loops would avoid       |
| *Decode XORed Array*  | `O(n)`: one XOR per encoded element, each reading only the element decoded immediately before it                  | `O(n)`: the output list of `n + 1` values, which is the answer itself, with `O(1)` auxiliary beside it                                         |

## Summary

- **XOR is its own inverse**, which means applying the same value twice returns
  the accumulator to its original state, and this is the property the entire topic
  is built from
  - The four identities are `a ^ a == 0`, `a ^ 0 == a`, `a ^ b == b ^ a`, and
    `(a ^ b) ^ c == a ^ (b ^ c)`
  - Because order and grouping are free, you may pretend the input arrives with
    every duplicate pair adjacent even when it does not, which is what licenses a
    single unordered pass
- XOR is **column-wise addition modulo 2**, since each output column is the sum of
  the input columns with the carry discarded. Folding a whole collection therefore
  produces a value whose bit at each position is set exactly when an odd number of
  inputs had a 1 there
- The signal to reach for XOR is a problem where duplicates are guaranteed to be
  **paired** and the statement asks for constant extra space. The hash map that
  counts occurrences is correct and linear, and it is rejected only because it
  stores `O(d)` entries to read back a single fact about parity
- XOR does not care where a value came from, so two different collections can be
  folded against each other and their shared members will still cancel
  - *Missing Number* folds the indices `0..n - 1` against the values and seeds the
    accumulator with `len(nums)`, because `enumerate` never produces the index `n`
    even though `n` is a candidate answer
  - *Find the Difference* folds `ord` of every character of both strings, which
    handles the case where the added character already appears in the first string
    and a set-based solution reports nothing
- A partial XOR is a fingerprint of the prefix consumed so far rather than a
  partial answer, so no fold should carry an early exit. On `[3, 0, 1]` the
  accumulator passes through `0`, which is a legal answer to that problem and is
  still wrong at that moment
- *Decode XORed Array* undoes a chain by XOR-ing the previously decoded element
  into the encoded one, because `arr[i] ^ (arr[i] ^ arr[i + 1])` collapses to
  `arr[i + 1]`. This is a prefix sum with XOR in place of addition, and it needs no
  separate inverse operation since XOR is its own
- When copies come in **threes** the fold breaks entirely, because `a ^ a ^ a` is
  `a` rather than `0`, so nothing cancels
  - The repair is to keep the per-column idea and change the modulus, counting the
    set bits in each of the 32 columns and keeping those whose count is not a
    multiple of 3
  - The loop must be capped at 32 columns with a signed conversion afterwards,
    because Python sign-extends a negative value forever and an uncapped loop over
    positions would never finish
- When **two** values appear once, fold everything to get `diff`, which is their
  XOR and not either answer, then split the array on any bit that `diff` has set
  - That bit is a position where the two singletons disagree, so it forces them
    apart, while a duplicate pair always answers the same test the same way and
    stays together to cancel
  - `diff & -diff` picks the lowest such bit in one operation, and `diff` is
    guaranteed non-zero because the two singletons are distinct values
  - Splitting on a bit where `diff` is `0` is the mistake to avoid, since both
    singletons land in one group and cancel each other, and neither returned value
    is an answer

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Do the duplicates in this problem come in pairs, or in threes, or in some other
  multiple that XOR cannot cancel?
Is the constant-space requirement stated, which is what rules the hash map out?
Does the problem promise exactly one unpaired value, or two, or a missing one?
Am I seeding the accumulator at 0, or does the problem need something folded in
  by hand, as len(nums) is in Missing Number?
Am I tempted to return the accumulator early, and do I know that a partial XOR
  means nothing until the last value is in?
If the fold gives me x ^ y rather than an answer, which bit do I split on, and
  why is that bit guaranteed to exist?
For a three-copy problem, is my column loop bounded at 32 and converted back to
  a signed value at the end?
Can any input be negative, and does my solution assume a width Python does not
  have?
Am I folding two different collections against each other, and does every shared
  member really appear exactly once on each side?
Does the empty or single-element input still do the right thing?
```
