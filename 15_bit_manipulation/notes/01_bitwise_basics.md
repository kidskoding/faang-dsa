# Bitwise Basics

Every integer a computer stores is written in **binary**, meaning base 2. Decimal
gives each digit a place worth a power of ten, so `205` is `2*100 + 0*10 + 5*1`.
Binary gives each digit a place worth a power of two, and the only digits
available are `0` and `1`, so `1101` is `1*8 + 1*4 + 0*2 + 1*1`, which is `13`.
Each of those binary digits is called a **bit**

Two words come up constantly and are worth pinning down now. The **bit position**
is the exponent of the power of two that bit is worth, counted from the right
starting at zero, so in `1101` the bit at position 3 is worth `8`. A bit holding
`1` is a **set bit**, and a bit holding `0` is a **clear bit**. Position 0, the
one worth `1`, is the **least significant bit** or LSB, and the highest set
position is the **most significant bit** or MSB

```text
value      1    1    0    1        =  13
position   3    2    1    0
worth      8    4    2    1
```

The reason this gets its own module is that an integer is not really one number
to a machine, it is a row of independent switches that happens to be readable as
a number. The **bitwise operators** act on that row directly, one position at a
time, all positions simultaneously. That is the intuition hook for the whole
module: an `int` is 32 or 64 booleans travelling together, and a single operator
updates all of them in one instruction, which is why these tricks are fast and
why interviewers like them

Python prints the binary form with `bin`, which is the fastest way to check your
reasoning while debugging

## The Four Operators That Work Position By Position

There are four operators to know, and each one is defined by what it does to a
single pair of bits. Everything else in this module is built out of them

```text
a  b  |  a & b   a | b   a ^ b        ~a
0  0  |    0       0       0           1
0  1  |    0       1       1           0
1  0  |    0       1       1           1
1  1  |    1       1       0           0
```

- **AND**, written `&`, gives `1` only where **both** operands have `1`, so it
  keeps a bit only if it appears in both numbers
- **OR**, written `|`, gives `1` where **either** operand has `1`, so it merges
  the set bits of the two numbers
- **XOR** (exclusive or), written `^`, gives `1` where the two operands
  **differ**, so it marks disagreement
- **NOT**, written `~`, flips every bit of a single operand, and it is the one
  operator with a surprise in Python that gets its own section below

Lining two numbers up vertically is how you should reason about these on a
whiteboard, because the operator never carries between columns the way `+` does.
Each column is decided entirely on its own

```text
a = 12    1 1 0 0
b = 10    1 0 1 0
          -------
a & b     1 0 0 0   =  8    both had a 1 only in the 8s column
a | b     1 1 1 0   = 14    a 1 anywhere survives
a ^ b     0 1 1 0   =  6    the 4s and 2s columns are where they disagree
```

```python
a, b = 12, 10

assert a & b == 8
assert a | b == 14
assert a ^ b == 6
assert bin(a) == "0b1100"
assert bin(a ^ b) == "0b110"
```

**`&` is not `and`, and mixing them up produces a wrong answer rather than an
error.** The keyword `and` is a truth-value operator that returns one of its two
operands, while `&` combines bits. With `n = 4`, `n & 1` is `0` because 4 is
even, but `n and 1` is `1` because 4 is truthy, and a parity check written with
`and` will call every non-zero number odd

Because XOR marks exactly the positions where two numbers disagree, the number of
set bits in `x ^ y` is the count of positions where `x` and `y` differ, which is
the **Hamming distance** between them. That is the entire content of
[Hamming Distance](https://leetcode.com/problems/hamming-distance/)

```python
def hamming_distance(x: int, y: int) -> int:
    return bin(x ^ y).count("1")


assert hamming_distance(1, 4) == 2
assert hamming_distance(3, 1) == 1
assert hamming_distance(0, 0) == 0
```

Counting characters in `bin` is fine for non-negative inputs and is what most
people write. It is not fine for negative ones, since `bin(-5)` is `'-0b101'` and
the minus sign makes the string a bad proxy for the bit pattern

## Sliding The Whole Number Sideways

The two shift operators move every bit the same number of positions

- `x << k` moves every bit `k` positions **left** and fills the vacated low
  positions with zeros, which multiplies the value by `2**k` because every bit
  moved to a place worth twice as much, `k` times over
- `x >> k` moves every bit `k` positions **right** and discards whatever falls
  off the bottom, which is floor division by `2**k` for a non-negative value,
  since the discarded bits were the remainder

```text
5 << 1     0 0 1 0 1  ->  0 1 0 1 0    = 10, and 5 * 2 = 10
20 >> 2    1 0 1 0 0  ->  0 0 1 0 1    =  5, and 20 // 4 = 5
5 >> 1     0 0 1 0 1  ->  0 0 0 1 0    =  2, the 1 that fell off was the remainder
```

```python
assert 5 << 1 == 10
assert 5 << 3 == 40
assert 20 >> 2 == 5
assert 5 >> 1 == 2
assert 1 >> 1 == 0
```

**Shifts bind more loosely than `+`, which is the precedence trap in this
module.** `1 << i + 1` is parsed as `1 << (i + 1)`, so with `i = 2` it is `8`
rather than the `5` that `(1 << i) + 1` gives. Parenthesise every shift that
sits next to arithmetic

The pair `>>` and `<<` used together is a conveyor belt: pull the low bit off one
number and push it onto the bottom of another, and after `w` rounds the second
number holds the first one reversed. That is
[Reverse Bits](https://leetcode.com/problems/reverse-bits/), where the width `w`
is fixed at 32 by the problem statement rather than by Python

```python
def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


assert reverse_bits(43261596) == 964176192
assert reverse_bits(1) == 2**31
assert reverse_bits(0) == 0
```

The order inside the loop body is the whole trick. `result <<= 1` first opens an
empty slot at the bottom of `result`, then `| (n & 1)` writes the bit just read
from `n` into that slot. Reading `n` before shifting `result` would drop that bit
into a slot that is about to move, and the answer would come out shifted by one

## What Python Does Below Zero

Negative numbers are stored in **two's complement**, which means the value `-x`
is represented by taking the bit pattern of `x`, flipping every bit, and adding
one. The point of the scheme is that ordinary binary addition then produces the
right answer for negative operands with no special casing, since in a fixed-width
machine word `x + (-x)` overflows to all zeros

Two consequences matter in interviews

The first is that `~x` is not "x with the sign removed" or anything similar. From
the definition, `-x` is `~x + 1`, so rearranging gives `~x == -x - 1`. In Python
that is exact and not a truncation artifact, because Python integers have
unbounded width and are treated as if the sign bit repeats forever to the left

```python
assert ~5 == -6
assert ~0 == -1
assert ~-1 == 0
assert -5 == ~5 + 1
```

The second is that `>>` on a negative value keeps it negative, filling from the
top with copies of the sign rather than with zeros, so `-7 >> 1` is `-4` and not
some large positive number. Shifting right stays floor division, and floor
division rounds toward negative infinity

```python
assert -7 >> 1 == -4
assert -1 >> 5 == -1
```

Because Python has no fixed width, a problem that talks about 32-bit integers has
to have its width imposed by hand, usually with `& 0xFFFFFFFF` to keep the low 32
bits. The [masks](02_masks.md) topic covers building those masks properly, and
Sum of Two Integers is the problem where it becomes unavoidable

The useful width tool for this topic is `int.bit_length()`, which returns how
many bits the value needs, so `(5).bit_length()` is `3` because `5` is `101`, and
`(0).bit_length()` is `0` because zero needs no bits at all

That gives a clean solution to
[Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/),
which asks for the value with every bit flipped **within the number's own
width**. Reaching for `~n` is the natural first attempt and it is wrong, because
`~5` is `-6` rather than the `2` the problem wants, since `~` also flips the
infinitely many leading zeros. Flipping only the bits inside the width means
XOR-ing against a mask of exactly that many ones, and `(1 << width) - 1` is the
all-ones value of a given width because subtracting one from a lone high bit
borrows all the way down

```python
def bitwise_complement(n: int) -> int:
    if n == 0:
        return 1
    return n ^ ((1 << n.bit_length()) - 1)


assert bitwise_complement(5) == 2
assert bitwise_complement(7) == 0
assert bitwise_complement(10) == 5
assert bitwise_complement(0) == 1
```

Zero is the degenerate case that needs its own line, because `bit_length()` is
`0` there, the mask comes out as `0`, and the answer would be `0` rather than the
`1` the problem specifies

## Counting Set Bits Without Visiting Every Position

[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) asks for the
**popcount**, the number of set bits in a value. The obvious approach is to test
each of the 32 positions with `(n >> i) & 1` and count the hits

```python
def hamming_weight_naive(n: int) -> int:
    count = 0
    for i in range(32):
        if (n >> i) & 1:
            count += 1
    return count


assert hamming_weight_naive(11) == 3
assert hamming_weight_naive(2**31) == 1
assert hamming_weight_naive(2**40) == 0
```

That last assert is the failure, and it is not a rounding issue. The number
`2**40` has exactly one set bit, at position 40, and the function returns `0`
because the loop only ever looks at positions 0 through 31. The `32` was a guess
about width, and Python integers have no width to guess at, so the moment an
input outgrows the guess the answer is silently wrong. Even inside 32 bits the
loop does 32 iterations to find the 3 set bits of `11`, doing work proportional
to the width instead of to the answer

What you want is a way to jump straight to the next set bit and skip the zeros.
The operation that does it is `n & (n - 1)`, which **clears the lowest set bit
and leaves every other bit alone**. The reason is borrowing. Subtracting one from
`n` turns the lowest set bit into a `0` and turns every zero below it into a `1`,
because the borrow propagates until it finds something to take from. Nothing
above the lowest set bit is touched. AND-ing the two together therefore keeps the
untouched high part, kills the lowest set bit since it is `1` in `n` and `0` in
`n - 1`, and kills everything below it since those were `0` in `n`

```text
n         = 1 0 1 1 0 0 0     (88)
n - 1     = 1 0 1 0 1 1 1     (87)
            . . . ^ ^ ^ ^     the borrow flipped the four marked ^, and the
                              three marked . were left alone
n & (n-1) = 1 0 1 0 0 0 0     (80), one fewer set bit than 88
```

Loop that until the value hits zero, and the number of iterations is the number
of set bits

```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(2**40) == 1
assert hamming_weight(0) == 0
```

> "Testing all 32 positions costs 32 steps whatever the input is, and it also
> assumes a width Python does not have. `n & (n - 1)` clears the lowest set bit,
> so looping until `n` is zero costs one iteration per set bit, which is `O(k)`
> for `k` set bits and correct at any width."

The mirror-image operation is `n & -n`, which **isolates** the lowest set bit
instead of clearing it, returning the power of two that bit is worth. It works
because `-n` is `~n + 1` from the previous section, so `-n` agrees with `n`
nowhere above the lowest set bit and agrees with it exactly there

```python
def lowest_set_bit(n: int) -> int:
    return n & -n


assert lowest_set_bit(12) == 4
assert lowest_set_bit(5) == 1
assert lowest_set_bit(0) == 0
```

Two easy problems fall straight out of clearing the lowest set bit. A positive
**power of two** has exactly one set bit by definition, since it is a single
power of two and nothing else, so clearing that one bit must leave zero. The
`n > 0` guard is doing real work rather than being defensive, because `0 & -1` is
also `0` and negative inputs pass the AND test too

```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0


assert is_power_of_two(16) is True
assert is_power_of_two(1) is True
assert is_power_of_two(3) is False
assert is_power_of_two(0) is False
assert is_power_of_two(-16) is False
```

A **power of four** is a power of two with one extra condition. The powers of
four are `1`, `4`, `16`, `64`, whose single bit sits at position 0, 2, 4, 6, so
the bit must be at an even position. A value whose only set bit is at position
`p` has `bit_length()` equal to `p + 1`, so an even position means an odd bit
length

```python
def is_power_of_four(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0 and n.bit_length() % 2 == 1


assert is_power_of_four(16) is True
assert is_power_of_four(1) is True
assert is_power_of_four(8) is False
assert is_power_of_four(5) is False
assert is_power_of_four(0) is False
```

## Reusing A Smaller Answer: [Counting Bits](https://leetcode.com/problems/counting-bits/)

The same question asked `n + 1` times at once changes the answer. Counting Bits
wants the popcount of every value from `0` through `n` inclusive, returned as one
`list[int]` of length `n + 1` where position `i` holds the number of set bits in
the integer `i`

Running `hamming_weight` on every value works and is `O(n * k)` for `k` set bits
per value, which is roughly `O(n log n)` because a value near `n` has about
`log2(n)` bits. Interviewers who ask this one usually want linear time and no
popcount call at all, which is the signal that the answers for smaller values are
supposed to be reused

The reuse comes from shifting. Dropping the last bit of `i` with `i >> 1` gives a
strictly smaller number whose answer is already computed, and the only bit lost
in the drop is the last one, which is `i & 1`. So the popcount of `i` is the
popcount of `i >> 1` plus one if `i` was odd. This is
[dynamic programming](../../11_dp/notes/01_dp_fundamentals.md) on a one-index
state, with a transition that reads a strictly earlier index

```text
i = 6   binary 110    i >> 1 = 3   binary 11    i & 1 = 0    2 + 0 = 2
i = 7   binary 111    i >> 1 = 3   binary 11    i & 1 = 1    2 + 1 = 3
```

> "Each value is its own half plus one final bit, so `ans[i] = ans[i >> 1] + (i & 1)`. Right-shifting always lands on a smaller index, so every value I read
> is already filled, and one left-to-right pass is enough."

1. Allocate `ans` with `n + 1` zeros, because the problem wants an entry for
   every value from `0` to `n` inclusive and the list is indexed by the value
2. Leave `ans[0]` at `0`, which is the base case, since zero has no set bits and
   there is no smaller value to derive it from
3. Walk `i` from `1` up to `n`, in increasing order, because the transition
   reads `ans[i >> 1]` and `i >> 1` is strictly less than `i` for every positive
   `i`, so increasing order guarantees the cell is already written
4. For each `i`, split it into everything except the last bit, which is `i >> 1`,
   and the last bit itself, which is `i & 1`. Those two parts are disjoint and
   together they are all of `i`, so their set bits add with no double counting
5. Write `ans[i] = ans[i >> 1] + (i & 1)`, which is one table lookup, one shift,
   one AND, and one addition, so each entry costs constant time
6. Return `ans` after the loop, with no post-processing, because every entry was
   finalised the moment it was written

```python
def count_bits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


assert count_bits(2) == [0, 1, 1]
assert count_bits(5) == [0, 1, 1, 2, 1, 2]
assert count_bits(0) == [0]
```

The loop order is the line to defend, since `range(1, n + 1)` going upward is what
makes every `ans[i >> 1]` a cell that has already been written. Walking downward
would read cells that are still zero and quietly return an all-wrong table rather
than crash

## Worked Example: [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Divide one integer by another and return the quotient truncated toward zero,
without using multiplication, division, or the modulo operator. Subtraction,
comparison, and the bit operators from this topic are all you get

**Input**:

- `dividend`, an `int`, the value being divided
- `divisor`, an `int`, the value dividing it, guaranteed non-zero
- Both are 32-bit signed integers, so each lies between `-2**31` and `2**31 - 1`
  inclusive, and either one may be negative

**Output**: an `int`, the quotient with the fractional part discarded rather than
rounded, so `7 / -3` is `-2` and not `-3`. If the true quotient does not fit in a
32-bit signed integer, return `2**31 - 1`, which happens for exactly one input
pair, `-2**31` divided by `-1`

The phrase that identifies the technique is the ban on `*` and `/`, which leaves
repeated subtraction as the only arithmetic that makes progress. Subtracting one
divisor at a time and counting the subtractions is correct and unusable, because
dividing `2**31 - 1` by `1` performs about two billion subtractions, making the
cost proportional to the answer rather than to the size of the input

Shifting fixes it. Since `chunk << 1` doubles a value, you can find the largest
doubled copy of the divisor that still fits inside what remains, subtract that
whole chunk in one step, and add the matching power of two to the quotient. Each
outer round removes at least half of what is left, so the number of rounds is
logarithmic rather than linear

> "Subtracting one divisor at a time is `O(quotient)`, which is two billion steps
> in the worst case. I will double the divisor while it still fits, subtract that
> chunk, and add the matching power of two to the quotient. That makes the number
> of rounds logarithmic in the quotient rather than linear in it."

1. Decide the sign of the answer once, at the very start, with
   `(dividend < 0) != (divisor < 0)`, because a quotient is negative exactly when
   the two operands disagree in sign. Take absolute values immediately afterwards
   so the loop never has to reason about signs again
2. Loop while the remaining value `a` is at least the divisor `b`, because once
   `a` is smaller than `b` no further whole divisor fits and everything left over
   is the discarded remainder
3. Inside each round, start `chunk` at `b` and `multiple` at `1`, which are the
   two numbers that move in lockstep, `chunk` holding a value and `multiple`
   holding how many copies of the original divisor that value is worth
4. Double both while the **doubled** chunk would still fit, testing
   `a >= chunk << 1` rather than `a >= chunk`. Testing the current value instead
   would accept a chunk larger than what remains and drive `a` negative
5. Subtract the surviving `chunk` from `a` in one step and add `multiple` to the
   quotient, which credits many divisors for a single subtraction and is the
   whole speed-up
6. Repeat from step 2 with the smaller `a`. Since the chunk removed was more than
   half of `a`, the value at least halves each round, which is the argument for
   the logarithmic round count
7. Apply the stored sign, then clamp the result into the 32-bit signed range with
   `max`/`min`, because `-2**31` divided by `-1` is `2**31`, one past the largest
   value the problem allows

```python
def divide(dividend: int, divisor: int) -> int:
    int_max, int_min = 2**31 - 1, -(2**31)
    negative = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    quotient = 0
    while a >= b:
        chunk, multiple = b, 1
        while a >= chunk << 1:
            chunk <<= 1
            multiple <<= 1
        a -= chunk
        quotient += multiple
    if negative:
        quotient = -quotient
    return max(int_min, min(int_max, quotient))


assert divide(78, 6) == 13
assert divide(10, 3) == 3
assert divide(7, -3) == -2
assert divide(0, 5) == 0
assert divide(-(2**31), -1) == 2**31 - 1
```

Tracing `78 / 6` shows where the work actually goes

```text
round 1   a = 78  chunk = 6  multiple = 1
          12 <= 78 ?  yes -> chunk = 12  multiple = 2
          24 <= 78 ?  yes -> chunk = 24  multiple = 4
          48 <= 78 ?  yes -> chunk = 48  multiple = 8
          96 <= 78 ?  NO, REJECTED, back off and use chunk = 48
          a = 78 - 48 = 30      quotient = 0 + 8 = 8

round 2   a = 30  chunk = 6  multiple = 1
          12 <= 30 ?  yes -> chunk = 12  multiple = 2
          24 <= 30 ?  yes -> chunk = 24  multiple = 4
          48 <= 30 ?  NO, REJECTED, back off and use chunk = 24
          a = 30 - 24 = 6       quotient = 8 + 4 = 12

round 3   a = 6   chunk = 6  multiple = 1
          12 <= 6  ?  NO, REJECTED immediately
          a = 6 - 6 = 0         quotient = 12 + 1 = 13
```

The rejected doublings are where the algorithm lives. In round 1 the inner loop
tests `96 <= 78`, refuses, and keeps the previous `chunk` of 48, which is exactly
why the guard is written on the doubled value. Round 3 rejects on its first test
and falls through to a plain single subtraction, which is the degenerate case
where the fast version does the same thing the naive one would

The quotient arrives as `8 + 4 + 1`, which is `1101` in binary, and that is not a
coincidence. Each round contributes one power of two, so the loop is writing the
answer's bits from the top down, exactly the way long division writes digits

- **Time Complexity:** `O((log q)²)` where `q` is the quotient, because the value
  at least halves each round giving `O(log q)` rounds, and each round restarts its
  doubling from the divisor instead of resuming where the last one stopped, so it
  redoes up to `O(log q)` doublings
- **Space Complexity:** `O(1)`, because the only storage is the four integers
  `a`, `chunk`, `multiple`, and `quotient`, and the quotient is accumulated in
  place rather than into any list

## Time and Space Complexity

Throughout, `w` is the number of bits in the value, which is 32 or 64 for a
problem that names a fixed width, and `k` is the number of set bits in the value

**Counting set bits in one value**

| Approach                                      | Time                                                                                                                                                                            | Space                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `n & (n - 1)` until zero                      | `O(k)`: each iteration removes exactly one set bit, so the loop runs once per set bit and never visits a zero bit                                                               | `O(1)`: two integers, one counter and the shrinking value |
| Testing all `w` positions with `(n >> i) & 1` | `O(w)`: the loop runs the full width regardless of the input, so a value with one set bit still costs 32 steps, and a hardcoded `w` is silently wrong for wider Python integers | `O(1)`: one counter and one loop index                    |

**Counting set bits for every value from 0 to n**

| Approach                                    | Time                                                                                                                   | Space                                                                                       |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `ans[i] = ans[i >> 1] + (i & 1)`            | `O(n)`: one constant-time transition per value, because the sub-answer is read from the table rather than recomputed   | `O(n)`: the output list of `n + 1` entries, which is the answer itself and not auxiliary    |
| Calling a popcount on each value separately | `O(n log n)`: `n` values, each costing up to `log2(n)` set-bit clears, since a value near `n` has about `log2(n)` bits | `O(n)`: the same output list, so the space is identical and only the time separates the two |

**Shift-based arithmetic**

| Operation                                   | Time                                                                                                                                                                                                                                    | Space                                                                            |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Divide by repeated doubling                 | `O((log q)²)`: where `q` is the quotient, since each outer round removes at least half of what remains giving `O(log q)` rounds, and each round restarts its doubling from the divisor rather than resuming, costing another `O(log q)` | `O(1)`: four integers, and the quotient is accumulated in place                  |
| Divide by subtracting one divisor at a time | `O(quotient)`: the loop count is the answer itself, so dividing `2**31 - 1` by `1` runs about two billion times and times out                                                                                                           | `O(1)`: a single counter, which is why the space bound never reveals the problem |
| Reversing `w` bits                          | `O(w)`: one iteration per bit position, and the width is fixed by the problem at 32 rather than derived from the value                                                                                                                  | `O(1)`: one accumulator holding the reversed value so far                        |

## Summary

- Every integer is a row of **bits**, where the bit at **position** `p` is worth
  `2**p` counted from the right starting at zero. A bit holding `1` is a **set
  bit**, and the rightmost position is the **least significant bit**
  - The reason to think this way is that the bitwise operators act on all the
    positions at once and never carry between columns, unlike `+`
- The four operators are **AND** (`&`) keeping a bit only where both operands
  have it, **OR** (`|`) keeping a bit where either has it, **XOR** (`^`) setting
  a bit exactly where the two operands differ, and **NOT** (`~`) flipping every
  bit of one operand
  - Because XOR marks disagreement, the popcount of `x ^ y` is the **Hamming
    distance**, the number of positions where the two values differ
  - `&` and `and` are different operators, and with `n = 4` the value of `n & 1`
    is `0` while `n and 1` is `1`, so a parity check written with `and` calls
    every non-zero number odd
- **Shifting** left by `k` multiplies by `2**k` and shifting right by `k` is floor
  division by `2**k`, because each bit moves to a place worth `2**k` times more or
  less. Shifting is how you do arithmetic when the problem bans `*` and `/`
  - `<<` and `>>` bind more loosely than `+`, so `1 << i + 1` means
    `1 << (i + 1)`, and every shift beside arithmetic needs parentheses
  - Reverse Bits uses both directions at once, shifting a bit out of the bottom
    of the input with `>>` and into the bottom of the result with `<<`, and the
    result must be shifted before the new bit is written into it
  - Divide Two Integers doubles the divisor while it still fits, subtracts that
    chunk, and adds the matching power of two to the quotient, turning
    `O(quotient)` subtractions into `O(log q)` rounds for a quotient `q`
- Negative values use **two's complement**, where `-x` is `~x + 1`, which gives
  the identity `~x == -x - 1` exactly rather than approximately
  - Python integers have unbounded width, so `~5` is `-6` and not `2`, and a
    problem that says "32-bit" needs that width imposed by hand
  - `>>` on a negative value fills from the top with the sign, so `-7 >> 1` is
    `-4`, staying floor division rather than becoming a large positive number
  - `int.bit_length()` gives the width the value actually needs, and
    `(1 << width) - 1` is the all-ones mask of that width, which is what
    complementing a number inside its own width requires
- `n & (n - 1)` **clears the lowest set bit**, because subtracting one flips that
  bit to `0` and every zero below it to `1` while leaving everything above
  untouched, so the AND keeps only the high part
  - Looping it until `n` is zero counts set bits in `O(k)` for `k` set bits,
    which beats testing all 32 positions and is correct at any width
  - `n & (n - 1) == 0` with `n > 0` tests for a **power of two**, since a power of
    two has exactly one set bit and clearing it must leave nothing
  - A **power of four** adds that the bit sits at an even position, which is the
    same statement as `n.bit_length()` being odd
- `n & -n` **isolates the lowest set bit** and returns the power of two it is
  worth, and it works because `-n` is `~n + 1`, so it matches `n` at the lowest
  set bit and disagrees everywhere above it
- Counting Bits reuses smaller answers with `ans[i] = ans[i >> 1] + (i & 1)`,
  because `i` splits into its own half and its last bit, and `i >> 1` is always a
  strictly smaller index that is already filled
  - Running a popcount on each value independently is `O(n log n)` and correct,
    so the reuse is a speed improvement rather than a correctness fix
- Three mistakes are worth guarding against specifically. Hardcoding a 32-bit
  width that Python does not have makes a wider input silently wrong, reaching
  for `~n` when the problem means "flip within this number's own width" returns a
  negative value, and dropping the `n > 0` guard on the power-of-two test lets
  `0` through, because `0 & -1` is also `0`

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Have I written the values out in binary and lined them up in columns?
Which operator matches the effect I want: keep both (&), merge (|), mark
  differences (^), or flip (~)?
Am I using & rather than and, so I am combining bits and not truth values?
Does the problem name a fixed width, and if so where do I impose it, since
  Python integers have no width of their own?
Can any input be negative, and have I checked what ~ and >> do to it?
Am I doing work proportional to the width when it could be proportional to
  the number of set bits?
Do I need to clear the lowest set bit (n & (n - 1)) or isolate it (n & -n)?
Is my power-of-two test guarded with n > 0, since 0 & -1 is also 0?
Is every shift parenthesised where it sits next to + or -?
Can I reuse the answer for a smaller value rather than recompute from scratch?
```
