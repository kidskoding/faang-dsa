# Modular Arithmetic

Dividing 17 by 5 gives two separate facts, and ordinary division throws one of
them away. The **quotient** is 3, because five fits into seventeen three whole
times. The **remainder** is 2, because after taking those three fives out, two is
what is left standing. Python hands you the quotient with `//` and the remainder
with `%`, and `divmod(17, 5)` hands you both at once as `(3, 2)`

**Modular arithmetic** is what you get when you keep only the remainder and throw
the quotient away. Fix a **modulus** `m`, and every integer collapses onto one of
exactly `m` values, `0` through `m - 1`, called its **residue** modulo `m`. Two
numbers that land on the same residue are treated as the same number

```text
m = 5

value      0   1   2   3   4   5   6   7   8   9  10  11  12
value % 5  0   1   2   3   4   0   1   2   3   4   0   1   2
           ^                   ^                   ^
           these three all collapse onto residue 0
```

A clock is the version everybody already owns. A clock face has modulus 12, so
adding five hours to ten o'clock gives three rather than fifteen, because 15 and 3
have the same remainder when divided by 12. Nothing was lost that the clock cared
about, since the clock only tracks the residue and lets the quotient — how many
times round you went — fall on the floor

That single move, keeping the remainder and discarding the quotient, is doing
three different jobs in interview problems. It **wraps** an index back into range,
which you already used as `% capacity` in the
[ring buffer](../../03_stacks_and_queues/notes/02_queue_and_deque.md). It **peels
one digit at a time** off a number, which is most of this module's number section.
And it **keeps a running total small** while a computation that would otherwise
explode is in flight. This topic covers the last two, plus the fast exponentiation
that mod-heavy problems are built on

## Peeling Digits Off A Number Without Turning It Into A String

The digits of a base-10 number are exactly its remainders. `n % 10` is the last
digit, because writing `n` as `10 * q + r` is the same statement as saying `r` is
what sits in the ones place. Then `n // 10` is that same number with the last
digit deleted, because dividing by 10 shifts every remaining digit one place
right. `divmod` gives you both in one call, which is why it is the natural shape
for this loop

```python
def reverse_digits(n: int) -> int:
    result = 0
    while n > 0:
        n, digit = divmod(n, 10)
        result = result * 10 + digit
    return result


assert reverse_digits(1234) == 4321
assert reverse_digits(1200) == 21
assert reverse_digits(7) == 7
assert reverse_digits(0) == 0
```

The two halves of the loop mirror each other, and that is the thing to see. `%`
reads a digit off the right end of `n`, while `result * 10 + digit` writes a digit
onto the right end of `result`. Reading destroys the source from the right and
writing builds the answer from the right, so the number comes out reversed for
free. `reverse_digits(1200) == 21` is not a bug, since leading zeroes do not exist
in a number, and an interviewer will ask about that case specifically

The same loop with a real constraint attached is
[Reverse Integer](https://leetcode.com/problems/reverse-integer/), where the
answer must fit in a signed 32-bit integer and you return `0` when it does not.
Python integers grow as large as memory allows, so nothing overflows on its own,
which means the check has to be written by hand

```python
INT_MIN, INT_MAX = -(2**31), 2**31 - 1


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    n, result = abs(x), 0
    while n > 0:
        n, digit = divmod(n, 10)
        result = result * 10 + digit
    result *= sign
    return 0 if result < INT_MIN or result > INT_MAX else result


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
assert reverse(1534236469) == 0
assert reverse(0) == 0
```

Pulling the sign off with `abs` before the loop is worth doing deliberately rather
than letting negatives run through `divmod`, for reasons the next section makes
concrete. Stripping the sign first means the loop only ever sees a non-negative
number, which is the case every language agrees on

> "I will take the sign off first and reverse the magnitude, because `%` on a
> negative number is one of the few places Python and C disagree, and I would
> rather not depend on which one the grader is running"

[Palindrome Number](https://leetcode.com/problems/palindrome-number/) uses the
same peel with one refinement. Reversing the whole number works, but you only need
half of it, and stopping halfway avoids building a value that could overflow in a
language that has a fixed integer width. Peel from the right and grow the reversed
half until the reversed half catches up with what is left

```python
def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        x, digit = divmod(x, 10)
        reversed_half = reversed_half * 10 + digit
    return x == reversed_half or x == reversed_half // 10


assert is_palindrome(121) is True
assert is_palindrome(1221) is True
assert is_palindrome(-121) is False
assert is_palindrome(10) is False
assert is_palindrome(0) is True
```

Two lines carry the whole thing. The guard rejects any number ending in `0` except
`0` itself, because a trailing zero would have to match a leading zero and numbers
do not have leading zeroes. The final `or` handles odd lengths, since a number like
`121` leaves `x == 1` and `reversed_half == 12`, and the middle digit belongs to
nobody, so `reversed_half // 10` drops it before comparing

The digit peel is also the engine behind
[Plus One](https://leetcode.com/problems/plus-one/),
[Add Strings](https://leetcode.com/problems/add-strings/), and
[Multiply Strings](https://leetcode.com/problems/multiply-strings/), except those
hand you the digits already separated and ask you to do the carrying yourself. A
carry is exactly a `divmod` by 10 in the other direction, where `total % 10` is the
digit you write and `total // 10` is what you pass left.
[Happy Number](https://leetcode.com/problems/happy-number/) peels digits to build
each next value and then needs to notice it is going round in a loop, which is the
[fast and slow pointer](../../06_linked_lists/notes/02_fast_slow.md) cycle test
applied to a sequence of numbers rather than a list of nodes

## The Same Peel In Base 26, And The Off-By-One It Hides

Nothing in that loop cares that the base is 10. Replace every 10 with `b` and you
convert to base `b`, because "the last digit in base `b`" and "the remainder modulo
`b`" are two names for one quantity. Spreadsheet columns run A, B, ..., Z, AA, AB,
which looks like base 26 with A as the digit for one

Reading a column title is the easy direction, since it is Horner's rule with 26
where a decimal reader would use 10

```python
def title_to_number(column_title: str) -> int:
    number = 0
    for letter in column_title:
        number = number * 26 + (ord(letter) - ord("A") + 1)
    return number


assert title_to_number("A") == 1
assert title_to_number("AB") == 28
assert title_to_number("ZY") == 701
assert title_to_number("FXSHRXW") == 2147483647
```

Now write the inverse the obvious way, peeling with `divmod(column_number, 26)` and
mapping remainder `r` to `chr(ord("A") + r)`. It produces `"BA"` for column 26,
which should be `"Z"`

The reason is worth pinning down, because it is the single hardest line in
[Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/).
Real base 26 has digits `0` through `25`, so a two-digit number starts at 26.
Spreadsheet columns have digits `1` through `26` with no zero at all, so `Z` is 26
and `AA` is 27. A numbering system with no zero is called **bijective base 26**,
and `divmod` does not know about it: `divmod(26, 26)` returns `(1, 0)`, giving
remainder 0, which has no letter, and a leftover quotient of 1, which then prints
another letter

Subtracting one before each `divmod` shifts the range `1..26` down onto `0..25`,
which is the range `divmod` actually produces

```text
column   26      before shift  divmod(26, 26) = (1, 0)   -> remainder 0, no letter
         26      after  shift  divmod(25, 26) = (0, 25)  -> remainder 25 -> "Z", done
```

```python
def convert_to_title(column_number: int) -> str:
    letters: list[str] = []
    while column_number > 0:
        column_number -= 1
        column_number, remainder = divmod(column_number, 26)
        letters.append(chr(ord("A") + remainder))
    return "".join(reversed(letters))


assert convert_to_title(1) == "A"
assert convert_to_title(26) == "Z"
assert convert_to_title(28) == "AB"
assert convert_to_title(701) == "ZY"
assert convert_to_title(2147483647) == "FXSHRXW"
```

The `-= 1` sits **inside** the loop rather than before it, because every position
needs the shift, not just the last one. Letters are collected right to left and
reversed at the end, which is the same `list` append and join used for
[serialization](../../07_trees/notes/07_serialization.md) and for the same reason,
since repeated string concatenation copies the whole string each time

## Why You Can Take The Remainder Early

Plenty of counting problems end with "return the answer modulo `10^9 + 7`", and
the naive reading is to compute the real answer and take its remainder at the very
end. That is the idea to kill, because it is the one whose failure hands you the
rule

Try it on `2000!`, a number this note actually measured: it has **5736 digits**.
Python will compute it, but a 5736-digit multiplication is not a constant-time
operation, so a loop that is supposed to be `O(n)` quietly becomes something much
worse as the numbers grow. In C++ or Java the same code is not slow, it is wrong,
because a 64-bit integer silently wraps around and the digits you get back are
garbage with no error raised

The repair is that `%` distributes over addition and multiplication, so you may
take the remainder at every step instead of once at the end

```text
(a + b) % m  ==  ((a % m) + (b % m)) % m
(a * b) % m  ==  ((a % m) * (b % m)) % m
```

Both hold for the same reason. Write `a = q1 * m + r1` and `b = q2 * m + r2`. Then
`a * b = (q1 * q2 * m + q1 * r2 + q2 * r1) * m + r1 * r2`, and every term except
`r1 * r2` carries a visible factor of `m`, so every one of them contributes
remainder 0. Only the product of the remainders survives, which is exactly what the
identity claims

```python
import math

MOD = 10**9 + 7


def factorial_mod(n: int, modulus: int = MOD) -> int:
    result = 1
    for k in range(2, n + 1):
        result = result * k % modulus
    return result


assert factorial_mod(0) == 1
assert factorial_mod(1) == 1
assert factorial_mod(5) == 120
assert factorial_mod(2000) == math.factorial(2000) % MOD
```

`result` never exceeds `modulus` at the top of any iteration, so `result * k` stays
small no matter how large `n` grows, and that is the entire point of writing the
`%` inside the loop instead of after it. Note that `*` and `%` have equal
precedence in Python and group left to right, so `result * k % modulus` already
means `(result * k) % modulus`

**The one operation that does not distribute is division.** Taking remainders first
and then dividing gives a different answer, as `(10 // 5) % 3` is `2` while
`((10 % 3) // (5 % 3)) % 3` is `0`. Dividing under a modulus means multiplying by
a **modular inverse** instead, and when `m` is prime — which is why `10^9 + 7` was
chosen — the inverse of `b` is `pow(b, m - 2, m)`. That is a follow-up rather than
a core skill, but knowing the phrase and that one-liner is worth more than it costs

## Where Negative Remainders Bite

Languages disagree about what `-7 % 3` means, and the disagreement traces back to
how each one rounds division. Python floors, so `-7 // 3` is `-3` and the remainder
comes out `2`, which keeps the sign of the **divisor**. C, C++, Java, and Go
truncate toward zero, so their `-7 / 3` is `-2` and their remainder is `-1`, which
keeps the sign of the **dividend**

```python
import math

assert -7 % 3 == 2  # Python floors, so the sign follows the divisor
assert -7 // 3 == -3  # floor division rounds down, never toward zero
assert int(-7 / 3) == -2  # truncation toward zero, which is C's and Java's rule
assert math.fmod(-7, 3) == -1.0  # the C-style remainder, if you ever need it
assert -7 % -3 == -1  # a negative divisor gives a negative remainder
assert 7 % -3 == -2  # and a positive dividend does not change that
```

Python's behaviour is the more useful one for indexing, because `-1 % n` is `n - 1`
and a pointer that steps off the left end wraps to the right end with no branch.
The `MyCircularDeque` insert in the
[ring buffer note](../../03_stacks_and_queues/notes/02_queue_and_deque.md) relies
on exactly that

It is the wrong behaviour when you actually want digits of a negative number, since
`-123 % 10` is `7` rather than `3`, which is why `reverse` above strips the sign
before the loop rather than after. The general habit is to normalize with
`value % m` once, so a value that might be negative lands back in `0..m-1` before
you use it as an index or a bucket key

## Squaring Instead Of Multiplying n Times

Raising `x` to the power `n` by multiplying `n` times is `O(n)`, and `n` in
[Pow(x, n)](https://leetcode.com/problems/powx-n/) runs across the full signed
32-bit range, so that loop can be asked to run over two billion times. That is the
naive idea, and its failure points straight at the fix

The fix comes from noticing that `x^10` does not need ten multiplications, because
`x^10 = (x^5)^2` and `x^5 = x * (x^2)^2`. Squaring doubles the exponent for the
price of one multiplication, so instead of climbing to `n` one step at a time you
can reach it by doubling, which takes about `log2(n)` steps

Turning that into a loop is the digit peel from the top of this topic, run in base
2\. Write `n` in binary, and `x^n` is the product of `x^(2^i)` over exactly the
positions where `n` has a 1 bit, because that is what binary notation says `n` is.
So keep a `base` that squares every iteration, walking `x`, `x^2`, `x^4`, `x^8`,
and multiply it into the running `result` only when the current bit is set

```python
def pow_mod(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base %= modulus
    while exponent > 0:
        exponent, bit = divmod(exponent, 2)
        if bit:
            result = result * base % modulus
        base = base * base % modulus
    return result


assert pow_mod(3, 13, 1000) == 323
assert pow_mod(2, 10, 1000) == 24
assert pow_mod(5, 0, 7) == 1
assert pow_mod(7, 1, 7) == 0
```

`divmod(exponent, 2)` is doing two things in one line, handing back the low bit as
`bit` and the shifted-down exponent as the new `exponent`, which is the same read
and shift as `divmod(n, 10)` with the base changed. The equivalent bitwise spelling
is `bit = exponent & 1` followed by `exponent >>= 1`, covered in
[bitwise basics](../../15_bit_manipulation/notes/01_bitwise_basics.md), and either
is fine to write as long as you can say which bit you are testing

Both multiplications carry their own `% modulus`, which is the previous section's
rule applied twice. The one on `base` matters more than it looks, because `base` is
squared on every iteration and would otherwise be the value that grows out of
control. Dropping it leaves a function that still returns the right answer in
Python and overflows in every other language

## Dry Run: pow_mod(3, 13, 1000)

Thirteen in binary is `1101`, so the answer should be `x^8 * x^4 * x^1` with the
`x^2` term left out. Every number below came out of running the function

```text
start   result=1  base=3  exponent=13

step 1  bit=1  MULTIPLY  result = 1 * 3 % 1000 = 3      base 3 -> 9      exponent -> 6
step 2  bit=0  SKIPPED   result stays 3                 base 9 -> 81     exponent -> 3
step 3  bit=1  MULTIPLY  result = 3 * 81 % 1000 = 243   base 81 -> 561   exponent -> 1
step 4  bit=1  MULTIPLY  result = 243 * 561 % 1000 = 323  base 561 -> 721  exponent -> 0
```

Step 2 is the one to look at. The `base` still squared from 9 to 81, because the
ladder of powers has to keep climbing whether or not this rung is used, but nothing
was multiplied into `result`. That skipped rung is the `2` in `13 = 8 + 4 + 1`,
which is missing from the sum, so its power has to be missing from the product

Step 3 also shows the modulus doing real work. The true `base` there is `3^8`,
which is `6561`, and `% 1000` cut it down to `561` before it was ever multiplied by
anything. Four rounds happened in total, seven multiplications between them,
against the thirteen the naive loop would have done, and against roughly
thirty-one rounds for an exponent near two billion

The final `result` is `323`. Checking it directly, `3^13` is `1594323`, whose last
three digits are `323`

## When The Remainder Is The Entire Answer

Sometimes the residue is not a step in the computation, it *is* the answer, because
the problem has a period and every position inside one period behaves the same way

[Nim Game](https://leetcode.com/problems/nim-game/) is the cleanest example. You
and an opponent alternately remove one, two, or three stones, and whoever takes the
last stone wins. Work up from the bottom: with 1, 2, or 3 stones you just take them
all and win. With 4 you are lost, because every move you can make leaves 1, 2, or 3
for the opponent, and they then win. With 5, 6, or 7 you win by leaving exactly 4.
With 8 you are lost again, for the same reason 4 was lost. The losing positions are
the multiples of 4, so the entire solution is one remainder test

```python
def can_win_nim(n: int) -> bool:
    return n % 4 != 0


assert can_win_nim(1) is True
assert can_win_nim(3) is True
assert can_win_nim(4) is False
assert can_win_nim(7) is True
assert can_win_nim(8) is False
```

The other place a residue is the whole answer is
[Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/),
and it comes with a trap named **modulo bias**. Two rolls of `rand7` build a
uniform number in `1..49` with `(rand7() - 1) * 7 + rand7()`, and it is tempting to
finish with `% 10`. That is not uniform, because 49 does not divide evenly into ten
buckets. Counting where `1..49` lands, nine residues collect five values each and
one collects only four, so one output is measurably rarer than the rest

```text
roll in 1..49, bucket = (roll - 1) % 10
bucket    0  1  2  3  4  5  6  7  8  9
count     5  5  5  5  5  5  5  5  5  4     <- biased, 49 is not a multiple of 10

roll in 1..40 only
count     4  4  4  4  4  4  4  4  4  4     <- uniform, 40 is a multiple of 10
```

The fix is **rejection sampling**, which means throwing away the rolls that spoil
the divisibility and rolling again. Discard anything above 40, and the survivors
are uniform over a range that 10 divides exactly

```python
import random


def rand7() -> int:
    return random.randint(1, 7)


def rand10() -> int:
    while True:
        roll = (rand7() - 1) * 7 + rand7()
        if roll <= 40:
            return (roll - 1) % 10 + 1


random.seed(0)
draws = [rand10() for _ in range(2000)]
assert set(draws) == set(range(1, 11))
assert min(draws) == 1 and max(draws) == 10
```

The `- 1` and `+ 1` around the `%` are the same 1-indexing shift as the Excel
column conversion, since `%` produces `0..9` and the problem wants `1..10`

## Counting Multiples Without Visiting Them

[Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
asks how many zeroes `n!` ends with, and computing `n!` is the wrong move for the
reason the factorial section already gave. A trailing zero is a factor of 10, which
is a factor of 2 paired with a factor of 5, and 2s are far more plentiful than 5s in
a factorial, so the count of 5s is the binding constraint

Every fifth number contributes a 5, every twenty-fifth contributes a second one,
and so on, so `n // 5 + n // 25 + n // 125 + ...` counts them without ever
enumerating anything

```python
def trailing_zeroes(n: int) -> int:
    count, power = 0, 5
    while power <= n:
        count += n // power
        power *= 5
    return count


assert trailing_zeroes(0) == 0
assert trailing_zeroes(3) == 0
assert trailing_zeroes(5) == 1
assert trailing_zeroes(30) == 7
assert trailing_zeroes(100) == 24
```

Note that `30 // 25` is `1` and not `0`, and that single extra count is what makes
`30!` end in seven zeroes rather than six. The `while power <= n` condition is what
stops the loop, since once the power of 5 exceeds `n` every later term is 0

[Count Primes](https://leetcode.com/problems/count-primes/) is the same instinct
inverted. Testing each number for divisibility one at a time repeats work, so
instead of asking "does anything divide `k`", walk each prime and cross off its
multiples, which is the **sieve of Eratosthenes**

```python
def count_primes(n: int) -> int:
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
    return sum(is_prime)


assert count_primes(10) == 4
assert count_primes(0) == 0
assert count_primes(2) == 0
assert count_primes(100) == 25
```

Two bounds make it fast, and both are worth stating aloud. The outer loop stops at
`sqrt(n)` because any composite below `n` has a factor no larger than its own square
root, so it was already crossed off by then. The inner loop starts at `p * p` rather
than `2 * p` because every smaller multiple of `p` has a factor below `p` and was
crossed off by that smaller prime first

Three problems in this section of the workbook lean on machinery that other modules
own rather than on remainders.
[Sqrt(x)](https://leetcode.com/problems/sqrtx/) is
[binary search on the answer](../../05_binary_search/notes/04_search_on_answer.md),
[Perfect Squares](https://leetcode.com/problems/perfect-squares/) is a
[one-dimensional DP](../../11_dp/notes/02_1d_dp.md) over the remaining value,
[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) is a
[three-way merge](../../08_heaps/notes/04_k_way_merge.md) of the multiples of 2, 3,
and 5, and [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) is a
[greedy](../../12_greedy_algorithms/notes/01_greedy_fundamentals.md) subtraction
down a value table

## Worked Example: [Pow(x, n)](https://leetcode.com/problems/powx-n/)

Compute `x` raised to the power `n` without calling the language's own power
operator. The exponent can be negative, which means the answer is a reciprocal

**Input**:

- `x`, a `float` base
- `n`, an `int` exponent that fits in the signed 32-bit range, so it can be as low
  as `-2^31` and as high as `2^31 - 1`, and it can be negative or zero

**Output**: a single `float`, the value of `x^n`. When `n` is negative the answer
is `1 / x^|n|`, so a result smaller than 1 is expected rather than an error, and
`n == 0` returns `1.0` for every base

The phrase that identifies the technique is the exponent's range. An exponent
allowed to reach `2^31 - 1` is a signal that the intended solution is
logarithmic in `n`, because a loop multiplying `x` by itself `n` times would run
over two billion iterations for a single test case

The idea is the one derived above. Squaring doubles the exponent for one
multiplication, so read `n` in binary and multiply in the squared base only at the
positions where `n` has a 1 bit

> "I will handle the negative exponent up front by replacing `x` with `1 / x` and
> `n` with `-n`, so the loop only ever sees a non-negative exponent. Then I will
> square the base each round and fold it into the answer when the current bit of
> the exponent is set, which is `O(log n)` multiplications"

Therefore,

1. Normalize the sign first. If `n` is negative, replace `x` with `1 / x` and `n`
   with `-n`, because `x^(-n)` and `(1/x)^n` are the same value, and doing this once
   at the top means the rest of the function never has to think about signs
2. Start `result` at `1.0`, which is the multiplicative identity, so the case
   `n == 0` falls out of the loop never running rather than needing its own branch
3. Loop while `n` is greater than zero, and each round split `n` with
   `divmod(n, 2)` into the new `n` and the low bit, which is the digit peel from
   earlier with the base set to 2
4. When that bit is 1, multiply the current `x` into `result`, because `x` at that
   moment holds `x^(2^i)` for the position `i` you are looking at, and binary
   notation says `n` is the sum of exactly those powers of two
5. Square `x` at the end of every round, whether or not the bit was used, since the
   ladder of `x`, `x^2`, `x^4`, `x^8` has to keep climbing for the later positions
   to be correct
6. Return `result` once `n` reaches zero, which happens after about `log2(n)`
   rounds because each `divmod` halves the exponent

```python
def my_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n > 0:
        n, bit = divmod(n, 2)
        if bit:
            result *= x
        x *= x
    return result


assert my_pow(2.0, 10) == 1024.0
assert my_pow(2.0, 0) == 1.0
assert my_pow(2.0, -2) == 0.25
assert abs(my_pow(2.1, 3) - 9.261) < 1e-9
assert my_pow(1.0, -(2**31)) == 1.0
```

Tracing `my_pow(2.0, 10)`, where 10 in binary is `1010`, so only two of the four
rounds contribute

```text
start   result=1.0  x=2.0  n=10

round 1  bit=0  SKIPPED   result stays 1.0     x 2.0 -> 4.0        n -> 5
round 2  bit=1  MULTIPLY  result = 4.0         x 4.0 -> 16.0       n -> 2
round 3  bit=0  SKIPPED   result stays 4.0     x 16.0 -> 256.0     n -> 1
round 4  bit=1  MULTIPLY  result = 1024.0      x 256.0 -> 65536.0  n -> 0
```

The two skipped rounds are the algorithm working rather than idling, since
`10 = 8 + 2` leaves out the `1` and `4` terms, and those are exactly rounds 1 and 3.
Round 4 also squares `x` up to `65536.0` immediately before the loop exits, which
is one wasted multiplication and is not worth a branch to avoid

`my_pow(1.0, -(2**31))` is the edge case to volunteer. Negating `-2^31` gives
`2^31`, which does not fit back into a signed 32-bit integer, so in C++ or Java that
line is undefined behaviour and the standard fix is to widen to a 64-bit type first.
Python integers have no fixed width, so the negation is simply correct here, and
saying that out loud is a cheap way to show you know where the language boundary is.
Also worth naming is that `my_pow(2.1, 3)` returns `9.261000000000001` rather than
`9.261`, because repeated float multiplication accumulates rounding error, which is
why the assert above compares within a tolerance instead of using `==`

- **Time Complexity:** `O(log n)`, because `divmod(n, 2)` halves the exponent every
  round, so the loop runs about `log2(n)` times and does a constant number of
  multiplications per round
- **Space Complexity:** `O(1)`, because the iterative version keeps only `result`,
  `x`, and `n`, and allocates nothing that grows with `n`. The recursive
  divide-and-conquer version of the same algorithm is `O(log n)` instead, since the
  call stack goes that deep

## Time and Space Complexity

Throughout, `n` is the numeric value being processed, `d` is its number of digits
which is about `log10(n)`, and `m` is the modulus

**Digit and base conversion**

| Approach                                          | Time                                                                                                           | Space                                                                                                              |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `divmod` peel, as in `reverse` or `is_palindrome` | `O(d)`: one iteration removes one digit, and `d` is about `log10(n)`, so it is logarithmic in the value        | `O(1)`: two integers are updated in place, and no list or string is built                                          |
| Converting to a string and reversing it           | `O(d)`: the same asymptotic cost, since it still touches every digit once                                      | `O(d)`: the string is a real allocation, and an interviewer asking for constant space is asking you to reject this |
| `convert_to_title` bijective base 26              | `O(L)`: where `L` is the number of output letters, about `log26(n)`, since each round emits exactly one letter | `O(L)`: the letters are collected in a list before being joined                                                    |

**Exponentiation, and accumulating under a modulus**

| Approach                                     | Time                                                                                                                                 | Space                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Binary exponentiation, `my_pow` or `pow_mod` | `O(log n)`: the exponent halves every round, so an exponent near `2^31` costs about 31 rounds                                        | `O(1)` iterative: three variables. `O(log n)` recursive, because the call stack is one frame per halving  |
| Multiplying `n` times                        | `O(n)`: one multiplication per unit of exponent, which is two billion iterations at the top of the 32-bit range                      | `O(1)`: the space was never the problem here, which is why the naive version looks acceptable until timed |
| `factorial_mod`, modding inside the loop     | `O(n)` multiplications, each on a number below `m`, so each one is genuinely constant time                                           | `O(1)`: one accumulator that never exceeds `m`                                                            |
| Multiplying out first, modding at the end    | `O(n)` multiplications on numbers that keep growing, so each one costs more than the last, and it is wrong in a fixed-width language | `O(n log n)` bits for the full product, since `n!` has about that many digits                             |

**Counting problems in this section**

| Approach                             | Time                                                                                                                                      | Space                                                                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `trailing_zeroes` by powers of 5     | `O(log n)` base 5: `power` multiplies by 5 each round and the loop stops once it passes `n`                                               | `O(1)`: a counter and a running power of 5                                                   |
| `count_primes` sieve                 | `O(n log log n)`: each prime `p` crosses off about `n / p` entries, and the sum of `1/p` over primes below `n` grows like `log log n`     | `O(n)`: one boolean per candidate below `n`, which is the memory cost you trade the time for |
| Testing each number for divisibility | `O(n * sqrt(n))`: trial division up to the square root of every candidate, repeating work the sieve does once                             | `O(1)`: no table, which is the only thing it wins on                                         |
| `rand10` rejection sampling          | `O(1)` expected: each attempt uses two `rand7` calls and succeeds with probability `40/49`, so the expected number of attempts is `49/40` | `O(1)`: nothing is stored between attempts                                                   |

The `rand10` row is the one to be careful with, since it has no worst-case bound at
all. A run of unlucky rolls can loop arbitrarily many times, so the honest statement
is expected constant time, and saying "expected" out loud is the difference between
a right answer and a right answer you can defend

## Summary

- The **modulus** operation `a % m` keeps the remainder after removing as many whole
  copies of `m` as fit, and throws away the quotient that `//` would have given you.
  Every integer collapses onto one of `m` **residues**, `0` through `m - 1`
  - `divmod(a, m)` returns the quotient and the remainder together, which is the
    natural shape for any loop that consumes a number one digit at a time
- The digits of a number are its remainders, so `n % 10` is the last digit and
  `n // 10` is the number with that digit deleted. Looping on `divmod(n, 10)` reads
  a number right to left without ever converting it to a string, which is what
  Reverse Integer, Palindrome Number, and Happy Number are all built on
  - Building the answer with `result = result * 10 + digit` writes digits onto the
    right end while the peel reads them off the right end, so the output comes out
    reversed unless you deliberately stop halfway
- Changing the 10 to any other base converts to that base, since "last digit in base
  `b`" and "remainder modulo `b`" are the same quantity. Excel columns are
  **bijective base 26**, having digits 1 through 26 and no zero, so the conversion
  needs `column_number -= 1` inside the loop on every round
  - Without that shift, `divmod(26, 26)` gives remainder 0, which maps to no letter,
    and column 26 prints as `BA` instead of `Z`
- `%` distributes over addition and multiplication, so `(a * b) % m` equals
  `((a % m) * (b % m)) % m`, which is why you may take the remainder after every
  step instead of once at the end. The proof is that expanding `a = q1*m + r1` and
  `b = q2*m + r2` leaves every term except `r1 * r2` carrying a factor of `m`
  - Do it inside the loop. Computing the full value first is slow in Python, because
    `2000!` has 5736 digits and big multiplications are not constant time, and is
    silently wrong in C++ or Java, because a 64-bit integer wraps with no error
  - Division does **not** distribute, so dividing under a modulus means multiplying
    by a **modular inverse**, which is `pow(b, m - 2, m)` when `m` is prime. That
    primality is why competitive problems specify `10^9 + 7`
- Python's `%` takes the sign of the divisor, so `-7 % 3` is `2`, while C, C++,
  Java, and Go truncate toward zero and return `-1` instead
  - The Python behaviour is what makes `-1 % n == n - 1`, which is a free wraparound
    for an index stepping off the left end of a circular buffer
  - It is the wrong behaviour for digit extraction, since `-123 % 10` is `7`, so
    strip the sign with `abs` before any digit loop
- **Binary exponentiation** computes `x^n` in `O(log n)` multiplications by squaring
  the base each round and folding it into the answer only where `n` has a 1 bit,
  which is the digit peel run in base 2. `pow(base, exp, mod)` is Python's built-in
  version and does the modding internally
  - The rounds where the bit is 0 still square the base, because the ladder of `x`,
    `x^2`, `x^4` must keep climbing for the later positions to be right
  - For a negative exponent, replace `x` with `1 / x` and `n` with `-n` once at the
    top. Negating `-2^31` is safe in Python and is undefined behaviour in C++, which
    is the edge case to name out loud
- Some problems are answered by the residue alone, because the situation repeats with
  a fixed period. Nim Game is `n % 4 != 0`, found by working up from the bottom and
  noticing that every multiple of 4 hands the opponent a winning position
- **Modulo bias** is the trap when `%` is used to generate randomness. Reducing a
  uniform value from `1..49` with `% 10` gives nine outcomes five ways each and one
  outcome only four ways, so the fix is **rejection sampling**: discard rolls above
  40 and reduce only what is left, since 10 divides 40 exactly
  - The cost is `O(1)` **expected** rather than worst case, because an unlucky run of
    rejections can loop any number of times
- Counting multiples beats visiting them. `n // 5 + n // 25 + n // 125 + ...` counts
  the factors of 5 in `n!` without building `n!`, and the **sieve of Eratosthenes**
  crosses off multiples from `p * p` upward instead of testing each number for
  divisibility, giving `O(n log log n)` time for `O(n)` space

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Do I want the remainder (%), the quotient (//), or both at once (divmod)?
Am I peeling digits with divmod(n, 10), or wastefully converting to a string?
Could the input be negative, and did I strip the sign before the digit loop?
Does my language's % follow the divisor's sign (Python) or the dividend's (C, Java)?
Is the modulus applied after every add and multiply, or only at the very end?
Is the base a bijective numbering with no zero digit, needing a -= 1 each round?
Does the exponent range hint that the intended answer is O(log n), not O(n)?
In binary exponentiation, am I squaring the base even on the rounds I skip?
Am I dividing under a modulus, which needs a modular inverse rather than //?
If I am reducing a random value with %, does the range divide evenly, or is it biased?
Would this overflow in C++ or Java even though Python survives it?
Can I state the cost in terms of the number of digits, not the value?
```
