# GCD and LCM

A **divisor** of a number is a number that goes into it exactly, with nothing
left over. The divisors of 12 are 1, 2, 3, 4, 6, and 12, and you can check any
candidate `d` with `n % d == 0`. A **common divisor** of two numbers is a number
that is a divisor of both, and the **greatest common divisor**, written
**gcd(a, b)**, is the largest of those

The other direction is the mirror image. A **multiple** of a number is what you
get by scaling it up a whole number of times, so the multiples of 4 are 4, 8, 12,
16, and so on forever. A **common multiple** of two numbers is a number that both
divide, and the **least common multiple**, written **lcm(a, b)**, is the smallest
positive one

The names describe them completely. "Divisor" means it divides, "common" means it
does so for both numbers, and "greatest" picks the biggest. Read that way you can
reconstruct either definition from its name months later, which matters because
interviewers say "gcd" and expect you to know instantly which direction it points

The picture worth holding onto is tiling. Lay two rulers of length `a` and `b`
side by side and try to pave each one exactly with tiles of a single size:

```text
a = 12   |----|----|----|----|----|----|----|----|----|----|----|----|
b =  8   |----|----|----|----|----|----|----|----|

tile of 4    12 = 4 + 4 + 4       8 = 4 + 4          both paved exactly
tile of 5    12 = 5 + 5 + 2       8 = 5 + 3          leftover on both
tile of 8     8 = 8               12 = 8 + 4         leftover on a

gcd(12, 8) = 4    the largest tile that paves both with nothing left over
lcm(12, 8) = 24   the first length that a run of 12s and a run of 8s both hit
```

Two numbers whose only common divisor is 1 are **coprime**, so `gcd(a, b) == 1`
is the way you test "these two share no factor". That single line is how problems
about reduced fractions, non-overlapping cycles, and irreducible ratios get
phrased in code

## Where Divisor Questions Hide

The word "gcd" almost never appears in the problem statement. What appears
instead is one of these:

- The **largest repeated block** that builds both of two things, as in the
  longest string that both `"ABCABC"` and `"ABC"` are made of by repetition
- **Two cycles lining up**, as in two lights blinking every `a` and every `b`
  seconds and you want the next moment they blink together, which is `lcm(a, b)`
- **Reducing a ratio to lowest terms**, since dividing both parts by their gcd is
  exactly what "lowest terms" means
- **Counting things shared by two numbers**, as in how many numbers divide both
  `a` and `b`
- **Reachable amounts** from repeatedly adding and subtracting two fixed
  quantities, which is the two-jugs family and is `gcd` in disguise

What this is *not*: any question about the **prime factors** themselves. "Count
the primes below `n`" wants a sieve, and "factor this number" wants trial
division up to `sqrt(n)`. The gcd is fast precisely because it never finds a
single factor of either input

## Why Hunting For The Answer Is Too Slow

The definition suggests its own algorithm. The gcd is at most `min(a, b)`,
because a divisor of a number cannot exceed it, so count downward from there and
return the first candidate that divides both:

```python
def gcd_scan(a: int, b: int) -> int:
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d
    return 0


assert gcd_scan(48, 18) == 6
assert gcd_scan(13, 7) == 1
assert gcd_scan(9, 9) == 9
assert gcd_scan(1, 1) == 1
```

This is correct, and it is unusable at interview input sizes. The loop runs once
per candidate, so its cost is `O(min(a, b))`, which is linear **in the value of
the input rather than in its length**. A pair of nine-digit numbers takes on the
order of a billion iterations even though the input is eighteen characters long

The failure is specific and it points somewhere. The scan works by guessing the
answer and checking it, and there are far too many things to guess. Nothing in
that loop uses the relationship between `a` and `b` at all, since the two numbers
are only ever consulted separately inside the `if`

## Shrinking The Numbers Instead

Stop looking for the answer and start making the problem smaller while keeping
the answer identical

Suppose `d` divides both `a` and `b`. Then `a = d * x` and `b = d * y` for whole
numbers `x` and `y`, so `a - b = d * (x - y)`, which means `d` divides `a - b`
too. The argument runs backwards just as well, because if `d` divides `b` and
`a - b` then it divides their sum, which is `a`. So the pair `(a, b)` and the
pair `(b, a - b)` have **exactly the same set of common divisors**, and therefore
the same greatest one:

```text
gcd(a, b) == gcd(b, a - b)
```

That already replaces one number with a smaller one for free. It is still slow
when the two numbers are far apart, because `gcd(1000000, 1)` would subtract 1 a
million times. But subtracting `b` over and over until you drop below `b` is just
the definition of the remainder, so a single `a % b` collapses that entire run of
subtractions into one operation:

```text
gcd(a, b) == gcd(b, a % b)
```

That is **Euclid's algorithm**. The base case is `gcd(a, 0) == a`, because every
number divides 0 exactly (`0 = d * 0` for any `d`), so the common divisors of `a`
and `0` are just the divisors of `a`, the largest of which is `a` itself

> "The common divisors of `a` and `b` are the same as the common divisors of `b`
> and `a % b`, because anything dividing two numbers also divides their
> difference. So I can keep replacing the pair with a smaller pair until the
> second one hits zero, and read the answer off the first."

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    return a if b == 0 else gcd_recursive(b, a % b)


assert gcd(48, 18) == 6
assert gcd(18, 48) == 6
assert gcd(13, 7) == 1
assert gcd(100, 25) == 25
assert gcd(9, 0) == 9
assert gcd(0, 0) == 0
assert gcd_recursive(48, 18) == 6
assert gcd_recursive(7, 13) == 1
assert gcd_recursive(0, 0) == 0
```

**Three things about those four lines**:

- `a, b = b, a % b` is a simultaneous assignment, so both new values are computed
  from the old pair before either is written. Splitting it into two statements
  overwrites `a` first and then feeds the wrong value into `a % b`
- The loop condition is `while b`, not `while b > 0` or `while a % b`, since the
  algorithm stops exactly when the second slot reaches zero and `while b` reads
  as "while there is still a remainder to fold in"
- Arguments in the wrong order cost one extra iteration and nothing else. With
  `a = 18` and `b = 48`, the first step produces `(48, 18 % 48)`, and `18 % 48`
  is 18, so the pair comes out as `(48, 18)` and the numbers have swapped
  themselves into the right order

**Why it terminates**: `a % b` is always strictly less than `b` for positive `b`,
so the second slot shrinks on every pass through a sequence of non-negative
integers, and a strictly decreasing sequence of non-negative integers has to
reach 0

**Why it is fast**: for `a >= b > 0` the value of `a % b` is always less than
`a / 2`. If `b <= a / 2` then `a % b < b <= a / 2` because a remainder is smaller
than what you divided by. If instead `b > a / 2` then `b` fits into `a` exactly
once, so `a % b = a - b < a / 2`. Either way, two steps into the loop the larger
of the two values has at least halved, which gives `O(log min(a, b))` iterations.
Running the loop on `1000000007` and `998244353` takes 9 steps, and the worst
case for a given size is a pair of consecutive Fibonacci numbers, where 832040
and 514229 take 28

Python ships this as `math.gcd`, which accepts any number of arguments and is
what you should call in an interview once you have shown you can write the loop

## Dry Run: Scanning Versus Euclid on gcd(48, 18)

The downward scan tests every candidate from 18 to 6, which is 13 tests, and
rejects the first 12 of them:

```text
d = 18   48 % 18 = 12   REJECTED, does not divide 48
d = 17   48 % 17 = 14   REJECTED
d = 16   48 % 16 =  0   18 % 16 = 2   REJECTED, divides 48 but not 18
d = 15   48 % 15 =  3   REJECTED
d = 14   48 % 14 =  6   REJECTED
d = 13   48 % 13 =  9   REJECTED
d = 12   48 % 12 =  0   18 % 12 = 6   REJECTED, divides 48 but not 18
d = 11   48 % 11 =  4   REJECTED
d = 10   48 % 10 =  8   REJECTED
d =  9   48 %  9 =  3   REJECTED
d =  8   48 %  8 =  0   18 %  8 = 2   REJECTED, divides 48 but not 18
d =  7   48 %  7 =  6   REJECTED
d =  6   48 %  6 =  0   18 %  6 = 0   ACCEPTED -> 6
```

The three rejections worth staring at are `d = 16`, `d = 12`, and `d = 8`. Each
one divides 48 cleanly, so half the test passes, and each is thrown away because
18 leaves a remainder. That is the work the scan cannot avoid, since it has no
way to use one number to narrow the search for the other

Euclid does the same job in three steps and never guesses anything:

```text
(a, b) = (48, 18)    48 % 18 = 12    ->  (18, 12)
(a, b) = (18, 12)    18 % 12 =  6    ->  (12,  6)
(a, b) = (12,  6)    12 %  6 =  0    ->  ( 6,  0)
b == 0, so return a = 6
```

Notice that 12 shows up in both traces and means opposite things. In the scan it
was a rejected candidate, and in Euclid it is a legitimate intermediate value of
the pair. Euclid never claims 12 is the answer, it only claims that
`gcd(48, 18)` and `gcd(18, 12)` are the same number

## Getting LCM From GCD

There is no separate algorithm for the least common multiple, because it falls
out of the gcd:

```text
gcd(a, b) * lcm(a, b) == a * b
```

The reason is easiest to see one prime at a time. If some prime appears `i` times
inside `a` and `j` times inside `b`, then it appears `min(i, j)` times in the gcd
(that is all both can supply) and `max(i, j)` times in the lcm (that is what both
need to divide it). Since `min(i, j) + max(i, j) == i + j`, which is how many
times the prime appears in `a * b`, the two sides match on every prime and
therefore match overall

Rearranged, `lcm(a, b) == a * b // gcd(a, b)`. Write it with the division first:

```python
def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b


assert lcm(4, 6) == 12
assert lcm(12, 8) == 24
assert lcm(7, 13) == 91
assert lcm(9, 9) == 9
assert lcm(5, 0) == 0
assert 12 * 8 == gcd(12, 8) * lcm(12, 8)
```

**Why `a // gcd(a, b) * b` and not `a * b // gcd(a, b)`**: the two are equal in
value, because the gcd divides `a` exactly so the early division leaves no
fraction behind, but they differ in the size of the intermediate. The second form
builds the full product `a * b` first, which overflows a 64-bit integer in Java
or C++ for inputs that are individually fine. Python integers grow without limit
so it will not actually break here, and you should still write the safe form and
say why, because "how would this behave in a fixed-width language" is a standard
follow-up

**Why the zero guard**: `lcm(a, 0)` is 0 by definition since 0 is a multiple of
everything, but the formula would divide by `gcd(a, 0) == a`, which is itself 0
when `a` is 0 as well. The guard is one line and removes the crash

Python also ships `math.lcm`, with the same multi-argument behaviour as
`math.gcd`

## Folding Over A Whole List

The gcd of three numbers is `gcd(gcd(a, b), c)`, because a number divides all
three exactly when it divides the first two and the third, so grouping the
arguments does not change which divisors qualify. That makes the gcd foldable,
and you can run it across a list with a single accumulator:

```python
def gcd_all(nums: list[int]) -> int:
    result = 0
    for value in nums:
        result = gcd(result, value)
        if result == 1:
            return 1
    return result


assert gcd_all([4, 6, 8]) == 2
assert gcd_all([12, 18, 30]) == 6
assert gcd_all([3, 5]) == 1
assert gcd_all([7]) == 7
assert gcd_all([]) == 0
```

Seeding `result` at 0 rather than at `nums[0]` is the detail to defend. Since
`gcd(0, x) == x`, zero is the **identity element** for gcd, so the first
iteration simply loads the first value and the empty list falls out correctly
without a special case. The early `return 1` is worth keeping because the gcd can
only ever shrink as you fold, so once it reaches 1 nothing later can raise it

**The near-miss to watch for**: *Find Greatest Common Divisor of Array* asks for
the gcd of the smallest and largest element, which is **not** the gcd of the
whole array. On `[4, 6, 8]` the array's gcd is 2, while `gcd(min, max)` is
`gcd(4, 8)`, which is 4. Read the statement rather than pattern-matching on the
title:

```python
def find_gcd(nums: list[int]) -> int:
    return gcd(min(nums), max(nums))


assert find_gcd([2, 5, 6, 9, 10]) == 2
assert find_gcd([7, 5, 6, 8, 3]) == 1
assert find_gcd([3, 3]) == 3
```

The same folding idea covers *Smallest Even Multiple*, which is asking for
`lcm(n, 2)` in words. Since 2 is prime, `n` either already contains it or does
not, so the answer is `n` when `n` is even and `2 * n` otherwise:

```python
def smallest_even_multiple(n: int) -> int:
    return n if n % 2 == 0 else 2 * n


assert smallest_even_multiple(5) == 10
assert smallest_even_multiple(6) == 6
assert smallest_even_multiple(1) == 2
assert all(smallest_even_multiple(n) == lcm(n, 2) for n in range(1, 200))
```

## Counting Everything Two Numbers Share

*Number of Common Factors* asks how many numbers divide both `a` and `b`. The
whole problem collapses on one fact: **the common divisors of `a` and `b` are
exactly the divisors of `gcd(a, b)`**. One direction is immediate, since the gcd
divides both numbers, so anything dividing the gcd divides both as well. The
other direction is the property that gives the gcd its name, because every common
divisor divides the greatest one rather than merely being smaller than it

So the question is really "how many divisors does `g` have", which you answer by
trial division up to `sqrt(g)`, pairing each small divisor `i` with its partner
`g // i`:

```python
def common_factors(a: int, b: int) -> int:
    g = gcd(a, b)
    count = 0
    i = 1
    while i * i <= g:
        if g % i == 0:
            count += 1 if i == g // i else 2
        i += 1
    return count


assert common_factors(12, 6) == 4
assert common_factors(25, 30) == 2
assert common_factors(1, 1) == 1
assert common_factors(36, 36) == 9
```

The `i == g // i` branch is the one people drop. When `g` is a perfect square its
square root pairs with itself, so `36` finds `6 * 6` and must count 6 once rather
than twice. Without that branch `common_factors(36, 36)` returns 10 instead of the
correct 9, since the divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, and 36

## Repeated Blocks, Measured In Lengths

*Greatest Common Divisor of Strings* wants the longest string `t` such that both
inputs are `t` repeated some whole number of times. The lengths make the gcd
appear: if `t` repeats to fill a string of length `n`, then `len(t)` divides `n`,
so a `t` that works for both inputs has a length that divides both lengths, and
the longest one has length `gcd(len(str1), len(str2))`

That fixes the length but not whether such a `t` exists at all. The test is a
single comparison:

```python
def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[: gcd(len(str1), len(str2))]


assert gcd_of_strings("ABCABC", "ABC") == "ABC"
assert gcd_of_strings("ABABAB", "ABAB") == "AB"
assert gcd_of_strings("LEET", "CODE") == ""
assert gcd_of_strings("A", "A") == "A"
```

If both strings really are copies of one block, then gluing them in either order
lays down the same sequence of blocks, so `str1 + str2` and `str2 + str1` must be
identical. `"ABABAB" + "ABAB"` and `"ABAB" + "ABABAB"` both give `"ABABABABAB"`,
which is five copies of `"AB"`. `"LEET" + "CODE"` gives `"LEETCODE"` while
`"CODE" + "LEET"` gives `"CODELEET"`, so no block exists and the answer is the
empty string. The converse also holds, which is the part you assert rather than
prove at a whiteboard: two strings commute under concatenation only when they are
powers of a common block

Once the test passes, the answer is just the first `gcd` characters of either
input, because that prefix is the block

## Reducing A Fraction Before You Print It

*Fraction To Recurring Decimal* is the one problem in this family where the gcd
is the supporting act. You are given a numerator and a denominator and must
print the exact decimal, wrapping any repeating part in parentheses, so `1/6`
becomes `"0.1(6)"`

The gcd does two small jobs. It reduces the fraction, which shrinks the
denominator and therefore the number of digits you have to generate, and it makes
the output canonical. The real machinery is long division: at each step you
multiply the remainder by 10, take the quotient as the next digit, and keep the
new remainder. **A remainder you have seen before produces the identical digit
and the identical next remainder, so the digits from that point on repeat
forever.** Recording each remainder in a
[hash map](../../01_arrays_and_hashing/notes/02_hashing.md) alongside the
position of the digit it produced turns cycle detection into one lookup, and the
stored position is exactly where the opening parenthesis goes

```python
def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    sign = "-" if (numerator < 0) != (denominator < 0) else ""
    n, d = abs(numerator), abs(denominator)
    g = gcd(n, d)
    n, d = n // g, d // g
    whole, remainder = divmod(n, d)
    if remainder == 0:
        return sign + str(whole)
    digits: list[str] = []
    seen: dict[int, int] = {}
    while remainder and remainder not in seen:
        seen[remainder] = len(digits)
        quotient, remainder = divmod(remainder * 10, d)
        digits.append(str(quotient))
    if remainder:
        start = seen[remainder]
        fraction = "".join(digits[:start]) + "(" + "".join(digits[start:]) + ")"
    else:
        fraction = "".join(digits)
    return f"{sign}{whole}.{fraction}"


assert fraction_to_decimal(1, 2) == "0.5"
assert fraction_to_decimal(2, 1) == "2"
assert fraction_to_decimal(4, 333) == "0.(012)"
assert fraction_to_decimal(1, 6) == "0.1(6)"
assert fraction_to_decimal(-50, 8) == "-6.25"
assert fraction_to_decimal(7, -12) == "-0.58(3)"
assert fraction_to_decimal(0, 5) == "0"
```

The sign is pulled out before anything else and the two magnitudes are made
positive, because `divmod` on a negative numerator rounds toward negative
infinity and would hand you a whole part of `-7` where you wanted `-6`. Once the
sign is a separate string, the arithmetic below it only ever sees positive
numbers

Tracing `1/6` shows why the map is keyed on the remainder rather than on the
digit:

```text
remainder 1   not seen, record at position 0   1 * 10 = 10   10 // 6 = 1   new remainder 4
remainder 4   not seen, record at position 1   4 * 10 = 40   40 // 6 = 6   new remainder 4
remainder 4   ALREADY SEEN at position 1       loop stops, no digit emitted

digits = ['1', '6'],  cycle starts at position 1  ->  "0.1(6)"
```

The third line is the step that gets rejected rather than executed. The loop
condition fails before another digit is appended, which matters because appending
first and checking afterwards would emit a spurious `6` and give `"0.1(66)"`.
Keying on the digit would also fail here, since digits repeat all the time
without the expansion being periodic, and only a repeated remainder proves the
whole future has repeated

The loop is guaranteed to end, because every remainder lies in `1` through
`d - 1`, so after at most `d - 1` new remainders one must recur or one must hit
zero

## Worked Example: [Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/)

You have two jugs with fixed capacities and an unlimited water supply. You may
fill a jug to the top, empty a jug completely, or pour one jug into the other
until either the source runs out or the destination is full. The question is
whether you can end up with exactly a target amount of water in the jugs

**Input**: three non-negative integers, `jug1_capacity` and `jug2_capacity` for how
much each jug holds, and `target` for the amount you are trying to measure out.
The target is not bounded by the jug sizes in the statement, so it may well ask
for more water than the two jugs can hold between them

**Output**: a `bool`, `True` when some finite sequence of fill, empty, and pour
operations leaves exactly `target` units of water in the two jugs **combined**,
and `False` when no sequence does. Note that the water may be split across both
jugs, so you are asked about the total on the table rather than about the
contents of one jug

The phrase that identifies the technique is "add and remove two fixed quantities
repeatedly", because that is exactly the setting where gcd governs what is
reachable. The naive reading is a
[breadth-first search over states](../../10_graphs/notes/06_implicit_state_bfs.md),
where a state is the pair of current contents and the six operations are the
edges. That is correct and it is far too slow, because the state space has
`jug1_capacity * jug2_capacity` entries, and for million-scale capacities that is
a trillion states

The way out is to find a property that every reachable state shares. Let
`g = gcd(jug1_capacity, jug2_capacity)`. Both jugs start empty, and 0 is a
multiple of `g`. Filling sets a jug to its capacity, which is a multiple of `g`
by definition. Emptying sets it to 0. Pouring moves water between two amounts
that are already multiples of `g`, and adding or subtracting multiples of `g`
gives another multiple of `g`. So **every jug's contents, at every moment, is a
multiple of `g`**, and so is the total. A target that is not a multiple of `g`
can never be produced

The converse is **Bezout's identity**, which says that for any `a` and `b` there
are whole numbers `x` and `y` with `a * x + b * y = gcd(a, b)`, and those
coefficients are realised physically by repeatedly filling one jug and pouring it
into the other. That makes every multiple of `g` reachable, as long as it fits

> "Every operation keeps both jugs at a multiple of `gcd(a, b)`, so the total is
> always a multiple of it too. Bezout's identity says every multiple of the gcd
> is reachable, so the answer is just: does the target fit in the two jugs, and
> is it a multiple of the gcd?"

Therefore,

1. Reject any `target` larger than `jug1_capacity + jug2_capacity` immediately,
   since that is all the water the two jugs can hold at once and no sequence of
   operations creates storage that is not there
2. Compute `g = gcd(jug1_capacity, jug2_capacity)` with Euclid, which is
   `O(log min(a, b))` and is the only real work in the solution
3. Convince yourself of the invariant before writing the return, because this is
   the step the interviewer will push on. Every reachable amount in either jug is
   a multiple of `g`, since the three operations only ever set a jug to `0`, set
   it to a capacity, or move a whole-number multiple of `g` from one to the other
4. Handle `g == 0`, which happens only when both capacities are 0. There is
   nowhere to put water, so the answer is `True` exactly when the target is 0.
   The guard also prevents a division by zero in the next step
5. Return `target % g == 0`. A remainder of 0 means the target is a multiple of
   the gcd, which by Bezout is reachable, and any other remainder means it sits
   between two reachable amounts
6. Sanity-check the answer on the classic instance out loud. With jugs of 3 and 5
   and a target of 4, the gcd is 1, every integer is a multiple of 1, and 4 is at
   most 8, so the answer is `True`, which matches the well-known solution of
   filling the 5, pouring into the 3, and repeating

```python
def can_measure_water(jug1_capacity: int, jug2_capacity: int, target: int) -> bool:
    if target > jug1_capacity + jug2_capacity:
        return False
    g = gcd(jug1_capacity, jug2_capacity)
    if g == 0:
        return target == 0
    return target % g == 0


assert can_measure_water(3, 5, 4) is True
assert can_measure_water(2, 6, 5) is False
assert can_measure_water(1, 2, 3) is True
assert can_measure_water(3, 5, 9) is False
assert can_measure_water(4, 6, 2) is True
assert can_measure_water(4, 6, 3) is False
assert can_measure_water(0, 0, 0) is True
```

The two `(4, 6, ...)` cases are the pair to talk through. Their gcd is 2, so
every reachable total is even. A target of 2 passes both tests and is reachable,
while a target of 3 fits comfortably inside the jugs and is still impossible,
because no sequence of fills, empties, and pours of even amounts can leave an odd
total behind. The capacity check alone would have wrongly accepted it

- **Time Complexity**: `O(log min(a, b))`, where `a` and `b` are the two
  capacities, because the only loop is Euclid and its second argument at least
  halves every two steps, while the two comparisons around it are constant time
- **Space Complexity**: `O(1)`, because Euclid rebinds two integers in place and
  the function allocates nothing that grows with the inputs

## Time and Space Complexity

Below, `a` and `b` are the two input values, `n` is the number of elements in a
list, `M` is the largest value in that list, `g` is `gcd(a, b)`, and `d` is a
reduced denominator

| Approach                                      | Time                                                                                                                                                                                           | Space                                                                                                                                |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Scanning candidates downward from `min(a, b)` | `O(min(a, b))`: one modulo test per candidate, and the count of candidates grows with the *value* of the input rather than its digit length, so nine-digit inputs mean roughly a billion tests | `O(1)`: a single loop variable, which is exactly why this version looks harmless in a code review                                    |
| Euclid, iterative                             | `O(log min(a, b))`: `a % b` is always below `a / 2`, so the larger value at least halves every two steps, and the worst case is consecutive Fibonacci numbers                                  | `O(1)`: two integers rebound in place, with no stack and no allocation                                                               |
| Euclid, recursive                             | `O(log min(a, b))`: identical arithmetic, one call per iteration of the loop                                                                                                                   | `O(log min(a, b))`: one stack frame per step, which is the only reason to prefer the loop                                            |
| `lcm(a, b)` as `a // gcd(a, b) * b`           | `O(log min(a, b))`: the gcd dominates, since the division and multiplication around it are single operations                                                                                   | `O(1)`: three integers, and dividing before multiplying also keeps the intermediate value small enough for fixed-width integer types |

| Application                                | Time                                                                                                                                                          | Space                                                                                                        |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Folding gcd across a list                  | `O(n log M)`: `n - 1` gcd calls, each bounded by the largest value `M` present, and often far cheaper because the running gcd shrinks fast                    | `O(1)`: one accumulator, since the fold never stores the intermediate results                                |
| Counting the common factors of `a` and `b` | `O(log min(a, b) + sqrt(g))`: Euclid first, then trial division up to `sqrt(g)` pairing each divisor with its partner                                         | `O(1)`: a counter and a loop index, because divisors are counted rather than collected                       |
| GCD of strings, on lengths `n1` and `n2`   | `O(n1 + n2)`: building and comparing the two concatenations dominates, since the gcd on the two lengths is logarithmic and disappears next to it              | `O(n1 + n2)`: the two concatenated copies are materialised before being compared                             |
| Fraction to recurring decimal              | `O(d)`: each loop pass consumes one distinct remainder, and remainders live in `1` through `d - 1`, so at most `d - 1` digits are produced before one repeats | `O(d)`: the `seen` map and the digit list each hold one entry per emitted digit, bounded by the same `d - 1` |

## Summary

- The **greatest common divisor** `gcd(a, b)` is the largest number that divides
  both `a` and `b` with no remainder, and the **least common multiple**
  `lcm(a, b)` is the smallest positive number that both of them divide
  - The tiling picture is the one to keep: the gcd is the largest tile that paves
    both lengths exactly, and the lcm is the first length that runs of both tiles
    reach together
  - Two numbers with `gcd(a, b) == 1` are **coprime**, which is how "share no
    common factor" and "already in lowest terms" get written in code
- Problems want a gcd whenever they mention the largest repeated block that
  builds two things, the moment two repeating cycles line up again, a ratio
  reduced to lowest terms, or amounts reachable by repeatedly adding and
  removing two fixed quantities
  - It is not a factoring question. A sieve counts primes and trial division
    factors a number, whereas the gcd is fast precisely because it never finds a
    single factor of either input
- Scanning candidates downward from `min(a, b)` is correct and costs
  `O(min(a, b))`, which is linear in the *value* rather than the digit length, so
  a pair of nine-digit numbers takes about a billion tests
  - The reason it is hopeless is that it guesses the answer and checks it, never
    using how `a` and `b` relate to each other
- **Euclid's algorithm** replaces the pair `(a, b)` with `(b, a % b)` until the
  second slot hits zero, then returns the first. It is correct because anything
  dividing `a` and `b` also divides `a - b`, so both pairs have the identical set
  of common divisors, and `a % b` is just a long run of those subtractions done
  at once
  - The base case is `gcd(a, 0) == a`, because every number divides 0, which also
    makes 0 the identity element and lets a fold over a list start at 0
  - It runs in `O(log min(a, b))` because `a % b` is always under `a / 2`, so the
    larger value at least halves every two steps. The worst case is consecutive
    Fibonacci numbers, and the pair 832040 and 514229 takes 28 steps
- The lcm has no algorithm of its own, since `gcd(a, b) * lcm(a, b) == a * b`,
  which holds because a prime appearing `i` times in `a` and `j` times in `b`
  appears `min(i, j)` times in the gcd and `max(i, j)` times in the lcm
  - Write it as `a // gcd(a, b) * b` with the division first. The division is
    exact so the value is unchanged, but the intermediate never reaches `a * b`,
    which is what overflows a 64-bit integer in Java or C++
  - Guard the zero case separately, since `lcm(a, 0)` is 0 and the formula would
    otherwise divide by `gcd(0, 0)`, which is 0
- The common divisors of `a` and `b` are exactly the divisors of `gcd(a, b)`, so
  counting shared factors means counting the divisors of `g` by trial division up
  to `sqrt(g)`, pairing each `i` with `g // i` and counting a perfect square's
  root only once
- Two strings are built from a common repeated block only when
  `str1 + str2 == str2 + str1`, and when they are, the block is the first
  `gcd(len(str1), len(str2))` characters of either one
- Reaching an exact amount with two jugs is `target <= a + b` together with
  `target % gcd(a, b) == 0`, because every operation keeps both jugs at multiples
  of the gcd and **Bezout's identity** makes every such multiple reachable
  - `gcd(4, 6) == 2` is the case to remember, since a target of 3 fits inside the
    jugs and is still impossible, so the capacity check alone is not enough
- The mistake that costs the most is reaching for prime factorization when the
  question only ever needed a gcd, which turns a nine-step loop into a
  `O(sqrt(a))` factor hunt with bookkeeping attached

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is the question asking for a divisor of both numbers (gcd) or a multiple of both (lcm)?
Can I state why gcd(a, b) == gcd(b, a % b), in terms of common divisors of the difference?
What does my gcd return when one argument is 0, and is gcd(0, 0) == 0 acceptable here?
Am I writing lcm as a // gcd(a, b) * b, dividing before multiplying, and can I say why?
Have I guarded lcm against a zero argument before the division runs?
Do I need the gcd of more than two values, and am I folding with an accumulator seeded at 0?
Does the problem want the gcd of the whole array, or only of two chosen elements like min and max?
If I need the count of shared factors, am I counting divisors of the gcd and handling perfect squares once?
For a reachability question, have I checked both that the target fits and that it is a multiple of the gcd?
Can I state the complexity as O(log min(a, b)) and justify the halving argument out loud?
```
