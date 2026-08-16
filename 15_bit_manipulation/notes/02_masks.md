# Masks

A **mask** is an integer you use for its bit pattern rather than its numeric
value. The positions where the mask holds a 1 are the positions you intend to
touch, and the positions where it holds a 0 are the ones you intend to leave
exactly as they were. Combine a mask with one of the
[bitwise operators](01_bitwise_basics.md) and you get an instruction that reaches
precisely the positions you named and nowhere else

The closest thing you already know is a `set`. A set marks which items are in
play, and a mask marks the same thing with one bit per item, packed into a single
integer. You have in fact already built one:
[implicit-state BFS](../../10_graphs/notes/06_implicit_state_bfs.md) carried the
collected keys as `mask | (1 << i)` and tested for the full collection with
`mask == (1 << k) - 1`. Those two lines were masks used without the name. This
topic is that idea made general, and it is what the rest of the module is built
on

Think of a mask as a stencil laid over a number. The holes are the 1 bits, the
card is the 0 bits, and whatever you spray only lands where the holes are. The
smallest useful stencil has exactly one hole, and it is written `1 << i`, an
integer whose only set bit sits at position `i`

```text
bit index      7   6   5   4   3   2   1   0
x = 10         0   0   0   0   1   0   1   0
1 << 3         0   0   0   0   1   0   0   0
                               ^ this is the only column the mask marks
```

Positions are numbered from the right starting at zero, because bit `i` carries
the value `2**i`, so bit 0 is the ones column and bit 3 is the eights column

> This topic covers the four single-bit operations, masks that cover a whole
> field of bits, how to fake a fixed integer width in a language that has none,
> and the mask problems in this module's ladder

## Four Things You Do To One Bit

There are only four questions you can ask about a single position, and each one
has exactly one operator behind it

- **Test** it with `&`, because AND keeps a bit only where both sides have a 1,
  so ANDing against a one-hole stencil throws away every other position and
  leaves you looking at just the one you asked about
- **Set** it with `|`, because OR produces a 1 wherever either side has one, so a
  1 in the mask forces that position on while the 0s elsewhere cannot turn
  anything on
- **Clear** it with `&` against the flipped mask, since `~(1 << i)` is 1
  everywhere except position `i`, so the AND preserves every other column and
  kills that one
- **Toggle** it with `^`, because XOR gives 1 when the two sides disagree, so a 1
  in the mask flips whatever was there and a 0 leaves it untouched

```python
def is_set(x: int, i: int) -> bool:
    return (x >> i) & 1 == 1


def set_bit(x: int, i: int) -> int:
    return x | (1 << i)


def clear_bit(x: int, i: int) -> int:
    return x & ~(1 << i)


def toggle_bit(x: int, i: int) -> int:
    return x ^ (1 << i)


assert is_set(0b1010, 1) is True
assert is_set(0b1010, 2) is False
assert set_bit(0b1010, 2) == 0b1110
assert set_bit(0b1010, 1) == 0b1010
assert clear_bit(0b1010, 3) == 0b0010
assert clear_bit(0b1010, 0) == 0b1010
assert toggle_bit(toggle_bit(0b1010, 5), 5) == 0b1010
assert is_set(0, 0) is False and set_bit(0, 0) == 1
```

`set_bit(0b1010, 1)` returning the input unchanged is worth staring at. Setting a
bit that is already set is a no-op, and so is clearing a bit that is already
clear, which is why these operations are safe to apply blindly without first
checking the current state

```text
bit index      7   6   5   4   3   2   1   0
x = 10         0   0   0   0   1   0   1   0
mask 1 << 2    0   0   0   0   0   1   0   0
x | mask       0   0   0   0   1   1   1   0
                                   ^ flipped on, nothing else moved
```

`is_set` shifts the bit down to position 0 and reads it, rather than testing
`x & (1 << i)` and relying on the truthiness of the result. Both are correct, and
the shift version is the one to prefer because the expression `(x >> i) & 1`
evaluates to a clean `0` or `1` that you can add straight into a counter, which
is exactly what the flip-counting problem below needs

**Two precedence facts, both verified rather than assumed.** In Python `<<` binds
tighter than `&`, so `x & 1 << i` really does parse as `x & (1 << i)`, and `&`
binds tighter than `!=`, so `x & (1 << i) != 0` is the comparison you meant
rather than the C-style trap. Parenthesise anyway, since a reader on a whiteboard
should not have to recall a precedence table

The one that genuinely bites is `~`. Unary `~` binds tighter than `<<`, so
`~1 << 3` is `(~1) << 3`, which is `-16`, while `~(1 << 3)` is `-9`. Applied to
`0b1010`, the first gives `0` and quietly destroys the whole number, and the
second gives `0b0010`, which is the clear you wanted

## Masks Wider Than One Bit

A mask does not have to have one hole. The workhorse is `(1 << k) - 1`, which is
`k` ones in a row. It works because `1 << k` is a single 1 followed by `k` zeros,
and subtracting one borrows through every one of those zeros and turns them all
into ones

```text
x = 109        0   1   1   0   1   1   0   1
(1<<4)-1       0   0   0   0   1   1   1   1
x & that       0   0   0   0   1   1   0   1
```

That gives you the two moves you need for any packed integer. `x & ((1 << k) - 1)`
keeps the lowest `k` bits and discards the rest, and shifting first lets you pull
out a field that starts anywhere

```python
def low_bits(x: int, k: int) -> int:
    return x & ((1 << k) - 1)


def field(x: int, start: int, width: int) -> int:
    return (x >> start) & ((1 << width) - 1)


assert low_bits(0b1101101, 4) == 0b1101
assert low_bits(0b1101101, 0) == 0
assert field(0b1101101, 3, 3) == 0b101
assert field(0b1101101, 0, 1) == 1
```

`low_bits(x, 0)` returning `0` is the degenerate case that confirms the formula
rather than breaking it, because `(1 << 0) - 1` is `0`, a stencil with no holes,
and keeping zero bits should give you nothing

Reading a field is what byte-format problems are made of. UTF-8 encodes the
length of a multi-byte character in the leading 1 bits of its first byte, so
`0b110xxxxx` announces a two-byte character and `0b10xxxxxx` announces a
continuation byte. Counting those leading ones is a mask walking downward

```python
def leading_ones(byte: int) -> int:
    count = 0
    probe = 1 << 7
    while byte & probe:
        count += 1
        probe >>= 1
    return count


assert leading_ones(0b11110000) == 4
assert leading_ones(0b10000000) == 1
assert leading_ones(0b01111111) == 0
assert leading_ones(0) == 0
```

The loop stops at the first zero rather than counting every 1 in the byte,
because the format only cares about the unbroken run at the top. With that count
in hand, *UTF-8 Validation* is a state machine: a count of 0 is a plain ASCII
byte, a count of 1 is a continuation byte that is only legal when you are still
expecting one, and a count of 2, 3, or 4 starts a character that demands exactly
that many minus one continuations after it

## Faking A Fixed Width That Python Does Not Have

Every mask trick above assumed the number has some width. Python integers do not.
They grow as large as they need to and behave as though the sign extends
infinitely to the left, so `~5` prints `-6` rather than the `0b11111010` you would
see in a fixed 8-bit register. There is no top bit for a carry to fall off

Since the width is not supplied by the language, you supply it yourself by ANDing
against an all-ones mask of the width the problem cares about, which for interview
problems is almost always 32 bits

```python
MASK32 = 0xFFFFFFFF


def to_signed_32(x: int) -> int:
    return x - (1 << 32) if x >> 31 else x


assert to_signed_32(0xFFFFFFFF) == -1
assert to_signed_32(0x80000000) == -2147483648
assert to_signed_32(0x7FFFFFFF) == 2147483647
assert to_signed_32(0) == 0
assert to_signed_32(1) == 1
```

`x >> 31` reads the sign bit, and when it is set the value `x` is a
[two's complement](01_bitwise_basics.md) negative that Python is reading as a
large positive, so subtracting `2**32` moves it back onto the negative side of
the line. Nothing else in the number changes

> "Python integers are arbitrary precision, so bits never fall off the top. I am
> going to mask with `0xFFFFFFFF` after every step to simulate a 32-bit register,
> and convert back to a signed value at the end"

Say that out loud before you write the loop. An interviewer who has watched
candidates fight an infinite loop on this problem will recognise immediately that
you know where the trap is

## Why ANDing Every Number In The Range Dies

*Bitwise AND of Numbers Range* asks for `left & (left + 1) & ... & right`. The
direct reading of the problem is also the direct implementation

```python
result = left
for n in range(left, right + 1):
    result &= n
```

This is correct and unusable. The bounds are 32-bit integers, so a call like
`range_bitwise_and(1, 2147483647)` performs over two billion AND operations for
an answer that is a single number. The cost is `O(R - L)`, and the input is
allowed to make that gap the size of the whole integer range

The failure points straight at the fix. Two billion iterations produce one
32-bit answer, so almost every iteration is doing nothing new, and the question
worth asking is which bit could possibly survive that many ANDs

## The Shared Prefix Survives

A bit is 1 in the final answer only if it is 1 in **every** number of the range,
because a single 0 anywhere kills that column forever

Start with bit 0. If the range holds two or more numbers then it holds two
consecutive integers, and one of any two consecutive integers is even, so some
number in the range has bit 0 clear and the answer's bit 0 is 0. Now shift
everything right by one. The numbers `left >> 1` through `right >> 1` are exactly
the prefixes that appear in the range, and the same argument applies to them, so
you keep discarding the bottom bit until `left` and `right` finally meet. What
they agree on at that moment is the **common prefix**, and shifting it back into
position, with zeros filling everything you discarded, is the answer

```python
def range_bitwise_and(left: int, right: int) -> int:
    shifts = 0
    while left < right:
        left >>= 1
        right >>= 1
        shifts += 1
    return left << shifts


assert range_bitwise_and(5, 7) == 4
assert range_bitwise_and(12, 15) == 12
assert range_bitwise_and(0, 0) == 0
assert range_bitwise_and(1, 2147483647) == 0
```

The loop condition is `left < right` rather than `left != right`, which reads
more naturally given that the bounds only ever converge downward, and it makes
the equal-bounds call `range_bitwise_and(0, 0)` return immediately with zero
shifts

## Dry Run: Collapsing The Range 5 To 7

```text
bit index      3   2   1   0
5              0   1   0   1
6              0   1   1   0
7              0   1   1   1
AND of all     0   1   0   0
                           ^ set in 5 and in 7, cleared by 6
```

The rejected column is bit 0. Both endpoints have it set, since 5 and 7 are both
odd, so a candidate answer built by comparing only `left` and `right` would keep
it and return 5. It has to go, because 6 sits between them with that bit clear.
The loop discards it without ever looking at 6

```text
left=5 (101)  right=7 (111)  shifts=0   they differ, so bit 0 is discarded
left=2 ( 10)  right=3 ( 11)  shifts=1   they differ, so bit 1 is discarded
left=1 (  1)  right=1 (  1)  shifts=2   equal, stop
answer = 1 << 2 = 4 = 0b100
```

Two shifts, two discarded columns, and the surviving prefix `1` slides back to
bit 2. Compare that against the two billion iterations the direct loop would
have run on a wide range, and the improvement is the thing to state out loud

## Reconciling Bits Across Three Operands

*Minimum Flips to Make a OR b Equal to c* gives you three numbers and asks how
many single-bit flips in `a` and `b` are needed before `a | b` equals `c`. The
positions are independent of each other, because a flip at position `i` cannot
affect the OR at any other position, so the whole problem is one bit column
decided at a time

```text
bit index      3   2   1   0
a = 2          0   0   1   0
b = 6          0   1   1   0
c = 5          0   1   0   1
```

Walk the columns from the right and there are only two cases

- When `c` has a 1 there, `a | b` must produce a 1, so you need at least one of
  the two to be set. If either already is, the column is free, and if neither is,
  one flip fixes it
- When `c` has a 0 there, `a | b` must produce a 0, so **both** must be clear.
  Every set bit among the two costs its own flip, which is why this case can cost
  two

```python
def min_flips(a: int, b: int, c: int) -> int:
    flips = 0
    while a or b or c:
        if c & 1:
            if not (a & 1) and not (b & 1):
                flips += 1
        else:
            flips += (a & 1) + (b & 1)
        a >>= 1
        b >>= 1
        c >>= 1
    return flips


assert min_flips(2, 6, 5) == 3
assert min_flips(4, 2, 7) == 1
assert min_flips(1, 2, 3) == 0
assert min_flips(0, 0, 0) == 0
```

The loop runs `while a or b or c` rather than for a fixed 32 rounds, so it stops
as soon as all three have been fully consumed. Stopping when only `a` is
exhausted would be a bug, because `c` may still carry set bits at higher
positions that `a` and `b` have to be flipped up to match

In the trace above, bit 0 needs one flip since `c` wants a 1 and neither operand
has one, bit 1 costs two flips since `c` wants a 0 and both operands are set, and
bit 2 is free since `c` wants a 1 and `b` already supplies it, for a total of
three

## Codes That Differ By Exactly One Bit

A **Gray code** sequence lists all `2**n` values of `n` bits in an order where
each value differs from the one before it in exactly one bit position, and the
last wraps back to the first the same way. Ordinary counting does not have this
property, since stepping from 3 to 4 changes `011` to `100`, which is three
positions at once

That is the clue to the construction. Incrementing a number flips a whole run of
trailing ones to zeros and turns the next zero into a one, so the damage is
always a contiguous suffix. XORing a number with a copy of itself shifted right
by one collapses that suffix to a single change, because each output bit compares
neighbouring input bits and only the boundary of the run disagrees

```text
i = 0   i = 000   i >> 1 = 000   i ^ (i >> 1) = 000  = 0
i = 1   i = 001   i >> 1 = 000   i ^ (i >> 1) = 001  = 1
i = 2   i = 010   i >> 1 = 001   i ^ (i >> 1) = 011  = 3
i = 3   i = 011   i >> 1 = 001   i ^ (i >> 1) = 010  = 2
i = 4   i = 100   i >> 1 = 010   i ^ (i >> 1) = 110  = 6
i = 5   i = 101   i >> 1 = 010   i ^ (i >> 1) = 111  = 7
i = 6   i = 110   i >> 1 = 011   i ^ (i >> 1) = 101  = 5
i = 7   i = 111   i >> 1 = 011   i ^ (i >> 1) = 100  = 4
```

Read the output column downward and every consecutive pair differs in one place,
including the wrap from `100` back to `000`

```python
def gray_code(n: int) -> list[int]:
    return [i ^ (i >> 1) for i in range(1 << n)]


sequence = gray_code(4)
assert gray_code(2) == [0, 1, 3, 2]
assert gray_code(1) == [0, 1]
assert gray_code(0) == [0]
assert sorted(sequence) == list(range(16))
assert all(bin(sequence[i] ^ sequence[i - 1]).count("1") == 1 for i in range(len(sequence)))
```

The last assert is the property itself rather than a spot check, and it covers
the wrap because index `-1` reaches the final element on the first iteration.
`gray_code(0)` returning `[0]` is the degenerate case, since `1 << 0` is 1 and a
zero-bit code has exactly one value

## Worked Example: [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

Add two integers and return the sum, without using `+` or `-` anywhere in the
solution. The whole problem is rebuilding what an adder circuit does, out of the
bitwise operators

**Input**: `a` and `b`, two `int` values that each fit in a signed 32-bit
integer, so either may be negative and the true sum also fits in 32 bits

**Output**: an `int`, the ordinary arithmetic sum of `a` and `b`, signed, so
`get_sum(-2, 3)` must return `1` rather than an unsigned bit pattern

**Recognizing it**: "without using the operator" is the phrase, and it always
means the operator has to be rebuilt from its parts. Grade-school addition
already tells you what those parts are, because adding two digits produces a
digit plus a carry into the next column. In binary the digit and the carry are
each one operator. `a ^ b` gives every column's sum while pretending no carry
exists, since XOR is 1 exactly when the two bits differ, which is the correct
answer for `0 + 1` and `1 + 0` and also for `1 + 1` where the column result is
indeed 0. `a & b` marks the columns where both bits are 1, which are exactly the
columns that generate a carry, and that carry belongs one position to the left,
hence `(a & b) << 1`

> "XOR gives me the sum with the carries dropped, and AND shifted left gives me
> the carries alone. If I feed those two back in as the new operands and repeat,
> the carries march leftward and eventually run out, and that is when the XOR
> alone is the answer"

Therefore,

1. Mask both operands with `0xFFFFFFFF` before the loop starts, which reduces a
   negative Python integer to the 32-bit two's complement pattern that a real
   register would hold. Without this the sign extension is infinite and a carry
   coming out of a negative number never runs out
2. Compute `carry = ((a & b) << 1) & MASK32`, which finds every column where both
   operands have a 1, moves those carries one position left where they are owed,
   and drops anything shifted past bit 31, because a carry out of the top of a
   32-bit register is discarded by the hardware and must be discarded here too
3. Compute the new `a` as `(a ^ b) & MASK32`, which is the sum of the two numbers
   as it would be if carrying were not a thing. This is a partial answer that is
   correct in every column where the two operands did not both hold a 1
4. Set `b` to that carry, so the next round adds the outstanding carries into the
   partial sum. The two quantities are being re-fed as a fresh addition problem,
   which is the same reduction repeated on smaller and smaller carry patterns
5. Loop `while b`, since `b` holding zero means there are no carries left to
   place, at which point `a` is the finished sum. The loop terminates because
   every round shifts the carry at least one position left, so after at most 32
   rounds the mask has erased it
6. Convert the result back to a signed value at the end. If bit 31 is set the
   pattern represents a negative number, so subtract `2**32` to land on the
   correct negative integer, and otherwise return `a` unchanged
7. Note that step 6 uses a subtraction, which the problem bans. If the
   interviewer holds you to the letter of the rule, replace that one branch with
   `~(a ^ MASK32)`, which flips the low 32 bits and then complements the result,
   landing on the same signed value through pure bit operations

```python
MASK32 = 0xFFFFFFFF


def get_sum(a: int, b: int) -> int:
    a &= MASK32
    b &= MASK32
    while b:
        carry = ((a & b) << 1) & MASK32
        a = (a ^ b) & MASK32
        b = carry
    return a if a >> 31 == 0 else a - (1 << 32)


assert get_sum(1, 2) == 3
assert get_sum(2, 3) == 5
assert get_sum(-1, 1) == 0
assert get_sum(-2, 3) == 1
assert get_sum(-1, -1) == -2
assert get_sum(0, 0) == 0
```

Tracing `get_sum(3, 5)` shows why the loop condition is `while b` and not
anything else

```text
round 0   a=00000011  b=00000101   xor=00000110   carry=00000010
round 1   a=00000110  b=00000010   xor=00000100   carry=00000100
round 2   a=00000100  b=00000100   xor=00000000   carry=00001000
round 3   a=00000000  b=00001000   xor=00001000   carry=00000000
round 4   a=00001000  b=00000000   -> done, answer 8
```

Round 2 is the step that rejects the tempting shortcut. The XOR comes out as
`00000000`, so a loop that stopped when the partial sum went to zero, or that
returned the XOR as soon as it looked settled, would answer 0 for `3 + 5`. The
entire answer is sitting in the carry at that moment, and only `while b` waits
for it

The negative case is where the 32-bit mask earns its place. Adding `-2` and `3`
runs 31 rounds, because `-2` is all ones except bit 0, so the carry has to walk
the full width of the register before `& MASK32` finally discards it off the top.
Drop the mask and that carry has nowhere to fall off, so the loop never ends

- **Time Complexity:** `O(1)`, because the carry advances at least one bit
  position per round and the mask erases it past bit 31, so no input can force
  more than 32 rounds of constant work
- **Space Complexity:** `O(1)`, because the loop rewrites `a`, `b`, and one carry
  variable in place and allocates nothing that grows with the input

## Time and Space Complexity

Let `w` be the width in bits of the values involved, which is 32 for every
problem in this module, and let `n` be the number of input items where the input
is a list

**Mask primitives**

| Operation                               | Time                                                                                                       | Space                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Test, set, clear, or toggle one bit     | `O(1)`: a shift and one bitwise operation on values that fit in a machine word                             | `O(1)`: the result replaces the input and nothing is allocated |
| Build `(1 << k) - 1` or extract a field | `O(1)`: a shift, a subtraction, and an AND, none of which depend on how many bits the mask ends up holding | `O(1)`: one integer                                            |
| Walk every bit position of one value    | `O(w)`: one round per position, and `w` is 32 here rather than a function of the input                     | `O(1)`: a counter and a probe mask                             |

**The problems in this section**

| Approach                                            | Time                                                                                                                            | Space                                                                                          |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| *Sum of Two Integers* by carry propagation          | `O(w)`: each round pushes the carry one position left, so it is gone after at most 32 rounds                                    | `O(1)`: three integers rewritten in place                                                      |
| *Bitwise AND of Numbers Range* by shared prefix     | `O(w)`: one shift per bit of the bounds, so at most 32 iterations regardless of how wide the range is                           | `O(1)`: two bounds and a shift counter                                                         |
| *Bitwise AND of Numbers Range* by ANDing each value | `O(R - L)`: one AND per number in the range, which reaches two billion iterations on `[1, 2147483647]` and times out            | `O(1)`: the space is fine, which is exactly why this one is easy to submit and be surprised by |
| *Minimum Flips* column by column                    | `O(w)`: one round per bit position until all three operands are consumed                                                        | `O(1)`: a flip counter and the three shifted operands                                          |
| *Gray Code* by `i ^ (i >> 1)`                       | `O(2**n)`: one XOR and one shift per value, and the sequence has `2**n` values by definition                                    | `O(2**n)`: the returned list is the output, and no scratch structure is built beside it        |
| *UTF-8 Validation* by leading-bit masks             | `O(n)`: one pass over `n` bytes, each costing at most 8 probe steps because a byte has 8 bits, so the per-byte work is constant | `O(1)`: a counter of how many continuation bytes are still expected                            |

## Summary

- A **mask** is an integer used as a stencil rather than as a number, where the 1
  bits mark the positions you intend to act on and the 0 bits mark the positions
  you intend to preserve. Pairing a mask with an operator is what lets you edit
  one column of a number and leave the rest alone
  - `1 << i` is the single-position mask, and `(1 << k) - 1` is `k` ones in a
    row, because `1 << k` is a one followed by `k` zeros and subtracting one
    borrows through all of them
- The four single-bit operations are testing with `(x >> i) & 1`, setting with
  `x | (1 << i)`, clearing with `x & ~(1 << i)`, and toggling with
  `x ^ (1 << i)`. Setting a bit that is already set and clearing one that is
  already clear both leave the number unchanged, so none of them need a
  guard first
  - The one that goes wrong in practice is the clear, because `~1 << i` is
    `(~1) << i` and wipes out low bits that should have survived, so the
    parentheses in `~(1 << i)` are load-bearing
- Pulling a field out of a packed integer is `(x >> start) & ((1 << width) - 1)`,
  which shifts the field down to position 0 and then keeps only as many bits as
  the field is wide. Byte-format problems such as *UTF-8 Validation* are this one
  line applied to the leading bits of each byte
- Python integers are arbitrary precision, so there is no top bit for a carry to
  fall off and `~5` is `-6` rather than a fixed-width pattern. Any problem that
  simulates a register has to supply the width itself by ANDing with
  `0xFFFFFFFF` after every step, then subtracting `2**32` at the end when bit 31
  is set
  - Forgetting the mask on a problem like *Sum of Two Integers* does not produce
    a wrong answer, it produces an infinite loop on negative inputs, since the
    carry keeps finding new positions to move into
- *Sum of Two Integers* rebuilds addition from `a ^ b` for the carry-free sum and
  `(a & b) << 1` for the carries, feeding both back in until the carry is empty.
  The loop must run `while b`, because the partial sum passes through zero on the
  way and stopping there returns the wrong answer
- *Bitwise AND of Numbers Range* is the shared binary prefix of the two bounds
  with zeros below it, found by shifting both bounds right until they are equal
  and then shifting the survivor back. Any bit below that point is cleared by
  some number inside the range, even when both endpoints have it set
  - The 5 to 7 case is the one to remember, since 5 and 7 are both odd and the
    answer is still 4, because 6 sits between them
- **Gray code** is an ordering of all `n`-bit values where neighbours differ in
  exactly one position, generated by `i ^ (i >> 1)`. It works because
  incrementing flips a contiguous run of trailing bits, and XORing against the
  shifted copy collapses that run down to the single boundary change
- Every one of these runs in `O(w)` time and `O(1)` space, where `w` is 32, which
  is the reason the technique exists. The two exceptions are *Gray Code*, which
  is `O(2**n)` because its output has that many values, and *UTF-8 Validation*,
  which is `O(n)` in the number of bytes

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Am I testing, setting, clearing, or toggling, and which operator does that one?
Does 1 << i line up with the position I actually mean, counting from 0 at the right?
Did I write ~(1 << i) rather than ~1 << i for the clear?
Does this problem simulate a fixed width, and did I say the 0xFFFFFFFF plan aloud?
Can a carry or a shift run off the top, and does my mask discard it?
Does the answer need converting back to a signed value at the end?
Is my loop bound a fixed 32 rounds, or a condition on the values still being non-zero?
Can I stop early, or does a partial result pass through zero before it is finished?
Do the bit positions decide independently, so I can handle one column at a time?
Is a per-bit loop O(32) here, or am I accidentally looping over the value range?
What does the degenerate input do: zero, equal bounds, or a single-element list?
```
