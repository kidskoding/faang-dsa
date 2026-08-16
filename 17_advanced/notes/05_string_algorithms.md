# String Matching: KMP, Z, And Rolling Hashes

Every algorithm in this topic answers one question: **where does one string appear
inside another?** The string being searched for is the **pattern**, the string
being searched through is the **text**, and an **occurrence** is a starting index
in the text where the pattern's characters line up exactly

The whole topic rests on one small idea about a single string, so it is worth
learning that idea before any searching happens. Take a string and look at its
**proper prefixes**, which are the pieces you get by chopping off the end without
chopping off everything, and its **proper suffixes**, which are the pieces you get
by chopping off the front the same way. "Proper" just means you are not allowed to
keep the whole string

```text
s = "aabaaab"

proper prefixes    a   aa   aab   aaba   aabaa   aabaaa
proper suffixes    b   ab   aab   aaab   baaab   abaaab
```

A string that shows up in **both** lists is called a **border** of `s`. Here
exactly one string qualifies, which is `"aab"`, since it is both the first three
characters and the last three. A border is a piece of the string that the string
both starts with and ends with

Borders are what make fast matching possible, because a border is the part of a
partial match you are allowed to keep when the match breaks. Most strings have
tiny borders or none at all, and a few have long ones

```text
"abab"   longest border "ab"     length 2
"aaaa"   longest border "aaa"    length 3
"abcd"   no border at all        length 0
"level"  longest border "l"      length 1
```

The rest of this topic builds a table of borders, uses it to search a text in
linear time, and then reads several other answers straight off the same table

## How These Problems Are Disguised

Interview problems in this family rarely say "implement KMP". They tend to say

- "return the index of the first occurrence of `needle` in `haystack`"
- "return the longest prefix of `s` that is also a suffix of `s`, excluding `s`
  itself"
- "does this string consist of one substring repeated some number of times?"
- "how many copies of `a` must you concatenate before `b` becomes a substring?"
- "add the fewest characters to the front of `s` to make it a palindrome"

Two of those never mention searching at all, and that is the tell worth
memorizing. **Any question about a prefix that is also a suffix, about a repeating
block, or about a palindromic prefix is a border question**, and the border table
is the tool built for it

What this family is *not*: problems about which characters a string contains
rather than in which order, which are
[frequency map](../../01_arrays_and_hashing/notes/02_hashing.md) work, and
problems about a set of many different patterns, where a
[trie](../../14_tries/notes/01_trie_basics.md) beats anything here. In production
you would call `haystack.find(needle)`, and the interviewer asking you to search a
string is asking you to write what `find` does

## Why Restarting At The Next Character Wastes Everything

The obvious way to search is to line the pattern up at index 0 of the text,
compare left to right, and on any mismatch shift the pattern one position right
and start comparing again from the pattern's first character. It is correct, and
its cost is `O(n * m)` for a text of length `n` and a pattern of length `m`,
because each of the `n` starting positions can compare up to `m` characters

The killer input is a text and pattern that agree for a long stretch before
disagreeing. Searching `"a" * 10000 + "b"` for `"a" * 100 + "b"` makes the naive
loop perform **1,000,001 character comparisons**, since nearly every start
position matches a hundred `a` characters and then fails on the last one. The
algorithm below finds the same answer in **20,100 comparisons**

The reason for the waste is visible on a much smaller input. Search
`"ababababc"` for `"ababc"`

```text
text     a  b  a  b  a  b  a  b  c
pattern  a  b  a  b  c
                     ^ mismatch: text has 'a' at index 4, pattern wants 'c'
```

At the moment of that mismatch you know something specific and valuable, which is
that `text[0..3]` is exactly `"abab"`, because you just compared all four of those
characters yourself. The naive fix throws that away, slides the pattern one step
right, and re-reads `text[1]` from scratch

Look at what the matched part `"abab"` contains. Its longest border is `"ab"`,
which means `"abab"` both starts and ends with `"ab"`. The last two characters you
matched, `text[2..3]`, are therefore `"ab"`, which is also the pattern's first two
characters. So the pattern can slide two positions to the right, its first two
characters already known to match, and comparison can resume at `text[4]` against
`pattern[2]`

```text
text     a  b  a  b  a  b  a  b  c
pattern        a  b  a  b  c
                     ^ resume here, comparing text[4] against pattern[2]
```

The text pointer never moved backward. That is the whole algorithm, and it is
called **KMP**, after Knuth, Morris and Pratt. The only thing it needs is, for
every prefix of the pattern, the length of that prefix's longest border, which is
exactly what to fall back to when a match breaks at that point

## The Failure Table Of Borders

The table is a list of `m` integers, conventionally called `lps` for **longest
proper prefix which is also a suffix**, and it is also called the **failure
function** because it says where to fail back to. The contract is one sentence

> `lps[i]` is the length of the longest border of `pattern[0..i]`, the prefix that
> ends at index `i`

The table is built on the **pattern alone** and never looks at the text, which is
why it can be reused across many searches

Building it is the same algorithm searching for the pattern inside itself. Walk
`i` forward through the pattern while `length` tracks how long a border you
currently have. If `pattern[i]` extends that border, `length` grows by one. If it
does not, you cannot give up entirely, because a shorter border might still
extend, and the shorter border of `pattern[0..length-1]` is sitting in
`lps[length - 1]` already

```python
def build_lps(pattern: str) -> list[int]:
    """lps[i] = length of the longest border of pattern[0..i]."""
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # fall back to the next shorter border
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length
    return lps


assert build_lps("aabaaab") == [0, 1, 0, 1, 2, 2, 3]
assert build_lps("ababc") == [0, 0, 1, 2, 0]
assert build_lps("aaaa") == [0, 1, 2, 3]
assert build_lps("abcd") == [0, 0, 0, 0]
assert build_lps("") == []
```

**The four lines that carry it**:

- `range(1, len(pattern))` starts at 1, never 0, because `lps[0]` is always 0
  since a one-character string has no proper prefix to be a border
- `length = lps[length - 1]` is the line everyone gets wrong, and it is the
  recursion of the whole idea. Having a border of length `length` that failed to
  extend, the next candidate is not `length - 1` but the longest border *of that
  border*, which `lps` has already recorded
  - Writing `length -= 1` instead compiles, runs, and produces wrong tables,
    because it tries prefixes that were never suffixes in the first place
- `while` rather than `if`, because one fallback may also fail and you may have to
  drop through several border lengths before either one extends or `length`
  reaches 0
- `if pattern[i] == pattern[length]` sits **outside** the `while`, so the case
  where `length` fell all the way to 0 and `pattern[i]` still does not match
  `pattern[0]` correctly leaves `lps[i] = 0`

The loop looks quadratic because of the nested `while`, and it is `O(m)`. The
counting argument is the same one that justifies the
[monotonic stack](../../03_stacks_and_queues/notes/03_monotonic_stack.md): the
`for` loop increases `length` at most once per iteration, so `length` gains at
most `m` over the whole run, and every `while` iteration strictly decreases it.
Total decreases cannot exceed total increases, so the inner loop runs at most `m`
times across the entire build

## Dry Run: Building The Table For "aabaaab"

Seven characters, so seven entries, with `lps[0] = 0` free

```text
pattern   a  a  b  a  a  a  b
index     0  1  2  3  4  5  6

i=1  'a' vs pattern[0]='a'   match        length=1   lps=[0,1,_,_,_,_,_]
i=2  'b' vs pattern[1]='a'   MISMATCH     fall back: length = lps[0] = 0
     'b' vs pattern[0]='a'   still no     length=0   lps=[0,1,0,_,_,_,_]
i=3  'a' vs pattern[0]='a'   match        length=1   lps=[0,1,0,1,_,_,_]
i=4  'a' vs pattern[1]='a'   match        length=2   lps=[0,1,0,1,2,_,_]
i=5  'a' vs pattern[2]='b'   MISMATCH     fall back: length = lps[1] = 1
     'a' vs pattern[1]='a'   match        length=2   lps=[0,1,0,1,2,2,_]
i=6  'b' vs pattern[2]='b'   match        length=3   lps=[0,1,0,1,2,2,3]
```

The step at `i = 5` is the one to study, because it is the only place the fallback
does real work. The running border was `"aa"` and the next character `'a'` failed
to extend it into `"aab"`. Giving up would have been wrong, since `"aabaaa"` does
have a border, namely `"aa"`. The fallback dropped `length` from 2 to `lps[1] = 1`,
the longest border of `"aa"`, and from there `'a'` matched `pattern[1]` and pushed
`length` straight back up to 2

The rejection at `i = 2` shows the other outcome. The border died completely, the
`while` ran `length` down to 0, and the character still did not match
`pattern[0]`, so the entry stayed 0. A string can lose its border entirely and
grow a new one later, which is exactly what `"aabaaab"` does

The final entry, `lps[6] = 3`, says the longest border of the whole string is 3
characters long, and those characters are `"aab"`. That single number answers two
of the workbook problems on its own, which is the next section

## Searching Without Rewinding The Text

With the table built, the search is a single pass with two pointers, `i` walking
the text and `j` holding how much of the pattern currently matches. On a mismatch,
`j` falls back through `lps` exactly as `length` did during the build, and `i`
never moves backward

```python
def kmp_search(text: str, pattern: str) -> int:
    """Index of the first occurrence of pattern in text, or -1."""
    if not pattern:
        return 0
    lps = build_lps(pattern)
    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]  # keep the border, discard the rest
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1


assert kmp_search("ababababc", "ababc") == 4
assert kmp_search("sadbutsad", "sad") == 0
assert kmp_search("leetcode", "leeto") == -1
assert kmp_search("aaa", "") == 0
assert kmp_search("", "a") == -1
```

**What differs from the table build**, which is almost nothing:

- The comparison is `ch != pattern[j]` rather than `pattern[i] != pattern[length]`,
  because one string is now the text instead of the pattern again
- `if not pattern: return 0` is the empty-pattern contract, and it has to come
  first because `pattern[j]` would raise on an empty pattern. Interviewers do pass
  the empty needle
- `return i - j + 1` recovers the start index, since `j` characters matched ending
  at `i`, so the match began `j - 1` positions earlier
- To find **every** occurrence rather than the first, replace the `return` with
  recording `i - j + 1` and then setting `j = lps[j - 1]`, which slides the pattern
  by its own border and lets overlapping matches be found

The bug worth naming is putting `i` back. Any version that writes
`i = i - j + 1` on a mismatch has reinvented the naive scan with extra steps, and
it is easy to do by accident when converting a nested-loop solution

## Dry Run: Searching "ababababc" For "ababc"

The pattern's table, from the same builder, is `[0, 0, 1, 2, 0]`

```text
i=0  'a' vs pattern[0]='a'   match           j=1
i=1  'b' vs pattern[1]='b'   match           j=2
i=2  'a' vs pattern[2]='a'   match           j=3
i=3  'b' vs pattern[3]='b'   match           j=4
i=4  'a' vs pattern[4]='c'   MISMATCH        j = lps[3] = 2
     'a' vs pattern[2]='a'   match           j=3
i=5  'b' vs pattern[3]='b'   match           j=4
i=6  'a' vs pattern[4]='c'   MISMATCH        j = lps[3] = 2
     'a' vs pattern[2]='a'   match           j=3
i=7  'b' vs pattern[3]='b'   match           j=4
i=8  'c' vs pattern[4]='c'   match           j=5 == m, so return 8 - 5 + 1 = 4
```

The answer is index 4, and `"ababababc"[4:9]` is `"ababc"`

The two rejected steps at `i = 4` and `i = 6` are the algorithm. Both times four
characters had matched, the fifth failed, and `j` dropped to 2 rather than to 0.
Dropping to 0 would have been correct but slow, since it would re-read characters
already known. Dropping to 2 keeps the claim that `text[i-2..i-1]` equals
`pattern[0..1]`, which the border of `"abab"` guarantees

Notice what did **not** happen at those steps. The value of `i` was 4 both before
and after the fallback, so no text character was read twice. Nine text characters
were read exactly once each, and the extra work was two table lookups

## Reading Answers Straight Off The Table

Two of the workbook problems never search anything, and both are one line once the
table exists

**Longest Happy Prefix** asks for the longest prefix of `s` that is also a suffix
of `s`, excluding `s` itself, which is the definition of the longest border. That
number is `lps[-1]`, so the answer is the slice it describes

```python
def longest_prefix(s: str) -> str:
    return s[: build_lps(s)[-1]] if s else ""


assert longest_prefix("level") == "l"
assert longest_prefix("ababab") == "abab"
assert longest_prefix("leetcodeleet") == "leet"
assert longest_prefix("a") == ""
assert longest_prefix("") == ""
```

**Repeated Substring Pattern** asks whether `s` is some block repeated two or more
times, and it is the same table read differently. Define the **period** of a
string as a shift `p` such that `s[i] == s[i + p]` everywhere both indices are
valid. A border of length `b` says exactly that `s[i] == s[i + n - b]` for every
valid `i`, because the first `b` characters and the last `b` characters agree
position by position, so `p = n - b` is a period, and the longest border gives the
smallest one

A string is a repeated block precisely when its smallest period divides its
length, because then the first `p` characters tile the string evenly

```python
def repeated_substring_pattern(s: str) -> bool:
    n = len(s)
    if n < 2:
        return False
    border = build_lps(s)[-1]
    return border > 0 and n % (n - border) == 0


assert repeated_substring_pattern("abab") is True
assert repeated_substring_pattern("aba") is False
assert repeated_substring_pattern("abcabcabcabc") is True
assert repeated_substring_pattern("a") is False
```

The `border > 0` guard is not decoration. A string with no border at all, such as
`"abc"`, has `border = 0`, so `n - border` is `n`, and `n % n` is 0, which would
report `True` for a string that repeats exactly once. Dropping that guard is the
standard bug in this problem

Checking the numbers by hand: `"abab"` has `lps[-1] = 2`, so the period is
`4 - 2 = 2`, and `4 % 2 == 0`, so it repeats. `"aba"` has `lps[-1] = 1`, so the
period is `3 - 1 = 2`, and `3 % 2 == 1`, so it does not. `"abcabcabcabc"` has
`lps[-1] = 9`, so the period is `12 - 9 = 3`, and `12 % 3 == 0`

## Gluing Two Strings With A Separator

**Shortest Palindrome** asks you to add the fewest characters to the *front* of
`s` so the result is a palindrome. Whatever you add gets mirrored from the tail,
so the characters you do not have to add are exactly the longest **palindromic
prefix** of `s`. Find that prefix, take everything after it, reverse it, and stick
it on the front

The trick is turning "longest palindromic prefix of `s`" into a border question. A
prefix of `s` is a palindrome exactly when it equals its own reverse, and the
reverse of a prefix of `s` is a suffix of `reversed(s)`. So build the string
`s + separator + reversed(s)` and ask for its longest border, which is the longest
string that is both a prefix of `s` and a suffix of `reversed(s)`

The separator has to be a character that appears in neither half, because without
it the border is free to run past the middle and report nonsense. For `s = "aa"`
the glued string without a separator is `"aaaa"`, whose longest border is `"aaa"`,
which is longer than `s` itself and therefore not a prefix of `s` at all

```python
def shortest_palindrome(s: str) -> str:
    if not s:
        return ""
    combined = s + "#" + s[::-1]
    palindromic_prefix = build_lps(combined)[-1]
    return s[palindromic_prefix:][::-1] + s


assert shortest_palindrome("aacecaaa") == "aaacecaaa"
assert shortest_palindrome("abcd") == "dcbabcd"
assert shortest_palindrome("a") == "a"
assert shortest_palindrome("") == ""
```

For `"aacecaaa"` the glued string is `"aacecaaa#aaacecaa"`, and the last table
entry is 7. So the first seven characters, `"aacecaa"`, form the longest
palindromic prefix, the leftover is the single `"a"` at the end, and reversing
that and prepending it gives `"aaacecaaa"`. For `"abcd"` no prefix longer than
`"a"` is a palindrome, so the table entry is 1 and the whole tail `"bcd"` comes
back reversed

The pattern generalizes past this one problem. **Concatenating two strings around
a separator and taking the longest border answers "what is the longest prefix of
`X` that is also a suffix of `Y`"**, and a surprising number of string problems
are that question wearing a costume

## The Z Array, Which Looks Forward Instead Of Backward

The **Z array** is the other standard table over a string, and it stores the same
kind of information pointed the other way

> `z[i]` is the length of the longest substring starting at index `i` that is also
> a prefix of the whole string

So `lps[i]` looks backward from `i` and asks how much of a prefix ends here, while
`z[i]` looks forward from `i` and asks how much of a prefix starts here. Position
0 is conventionally the whole length, since the string is trivially its own prefix

```text
s = "aabaaab"
z   7  1  0  2  3  1  0
       ^        ^
       |        z[4]=3 because "aab" starts at index 4 and is a prefix
       z[1]=1 because "a" starts at index 1 but "aa" does not continue
```

Computing it naively is `O(n²)`, since each position could scan the whole string.
The linear version keeps the rightmost match window found so far, written
`[left, right)`, where `s[left..right-1]` is known to equal a prefix. When `i`
falls inside that window, the characters from `i` to `right` have already been
seen at position `i - left`, so `z[i - left]` gives a free lower bound and only
the characters past `right` need real comparison

```python
def z_array(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    if n == 0:
        return z
    z[0] = n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])  # reuse, capped at the window edge
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


assert z_array("aabaaab") == [7, 1, 0, 2, 3, 1, 0]
assert z_array("aabxaabyaab") == [11, 1, 0, 0, 3, 1, 0, 0, 3, 1, 0]
assert z_array("abcd") == [4, 0, 0, 0]
assert z_array("") == []
```

**The one line to defend** is the `min(right - i, z[i - left])`. Taking
`z[i - left]` alone is wrong whenever it would reach past `right`, because
everything past `right` is unverified territory and the copied value would be a
guess. Capping at `right - i` keeps the claim to the part actually confirmed, and
the `while` then extends it honestly

Searching with a Z array uses the same separator trick as Shortest Palindrome.
Build `z` over `pattern + separator + text` and any position whose value equals
`len(pattern)` is an occurrence, offset by the pattern and separator lengths

```python
def z_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    m = len(pattern)
    z = z_array(pattern + "\x00" + text)
    for i in range(m + 1, len(z)):
        if z[i] == m:
            return i - m - 1
    return -1


assert z_search("ababababc", "ababc") == 4
assert z_search("sadbutsad", "sad") == 0
assert z_search("leetcode", "leeto") == -1
assert z_search("", "a") == -1
```

Z and KMP solve the same problems at the same cost, so knowing one well beats
knowing both badly. KMP is the one to master, because its table is what Longest
Happy Prefix, Repeated Substring Pattern, and every period question want directly.
Z earns its place when the question is naturally "how far does the prefix reach
from here", and its glued-string search costs `O(n + m)` extra space where KMP
costs `O(m)`

## Rabin-Karp, Which Compares Numbers Instead Of Characters

There is a completely different way to make matching fast: turn every window of
the text into a number, and compare numbers instead of characters. Treat a
length-`m` window as a base-`B` numeral whose digits are the character codes,
taken modulo a large prime `M` so the value stays bounded

```text
hash("abc") = (ord('a')*B^2 + ord('b')*B^1 + ord('c')*B^0) mod M
```

The payoff is that sliding the window one step right does not require rebuilding
the number. Subtract the leading digit's contribution, multiply by the base to
shift everything left, and add the new trailing digit, which is three arithmetic
operations rather than `m` character comparisons. A hash maintained this way is a
**rolling hash**

Equal hashes are only a **candidate** match, because two different strings can
collide onto the same value, so a hit has to be confirmed against the real
substring. That confirmation is what makes the worst case `O(n * m)`, since an
adversarial input can force a verification at every position

```python
def rabin_karp(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    base, mod = 256, (1 << 61) - 1
    high = pow(base, m - 1, mod)  # weight of the leading character, computed once
    pattern_hash = window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    for start in range(n - m + 1):
        if window_hash == pattern_hash and text[start : start + m] == pattern:
            return start
        if start + m < n:
            window_hash = (window_hash - ord(text[start]) * high) % mod
            window_hash = (window_hash * base + ord(text[start + m])) % mod
    return -1


assert rabin_karp("ababababc", "ababc") == 4
assert rabin_karp("sadbutsad", "sad") == 0
assert rabin_karp("leetcode", "leeto") == -1
assert rabin_karp("", "a") == -1
assert rabin_karp("abc", "") == 0
```

**Three details that decide whether it works**:

- `high = pow(base, m - 1, mod)` is computed once outside the loop, because
  recomputing it per window would put an `O(log m)` factor back into every step
  that the rolling hash exists to remove
- `text[start : start + m] == pattern` is the collision check, and deleting it
  turns a correct algorithm into one that is usually right, which is worse. Say
  out loud that you are verifying, since it is the detail interviewers probe
- `% mod` after both halves of the roll keeps the value bounded. Python integers
  never overflow, so it looks optional here and is not, both because the numbers
  would grow without limit and because the interviewer is checking whether you
  know it matters in a fixed-width language

Reach for Rabin-Karp over KMP when you are comparing **many** equal-length pieces
rather than searching for one pattern, since hashes go into a set and each
comparison stays `O(1)`. Searching for several patterns of the same length at
once, deduplicating substrings, and binary-searching on length to find the longest
repeated substring are all shaped that way. For a single pattern KMP is simpler
and has no collision story to defend

## Worked Example: [Repeated String Match](https://leetcode.com/problems/repeated-string-match/)

You are given two strings `a` and `b`, and you may write `a` out repeatedly, end
to end. Return the smallest number of copies that makes `b` a substring of the
result, or `-1` when no number of copies ever works

**Input**: `a` and `b`, both of type `str`, each consisting of lowercase English
letters, with `1 <= len(a) <= 10^4` and `1 <= len(b) <= 10^4`

**Output**: an `int`, the minimum count `k` such that `b` is a substring of `a`
repeated `k` times, and `-1` if no such `k` exists. The count is a number of
copies, not a length, so `a = "abcd"` and `b = "cdabcdab"` gives `3` rather
than `12`

**The approach**: this is a substring search in disguise, since "is `b` a
substring of `a * k`" is exactly `kmp_search(a * k, b) != -1`. The part that needs
thought is which values of `k` to test, because trying every `k` up to some guess
would rebuild and re-search a string that keeps growing, and the naive
character-by-character search inside it would be `O(len(a) * len(b))` per attempt

Only two values of `k` can ever be the answer. If `b` occurs at all, its
occurrence starts at some offset inside the first copy of `a`, and that offset is
at most `len(a) - 1`. From there you need `len(b)` more characters, so the total
length required is at most `len(a) - 1 + len(b)`, which fits in one more copy than
the bare minimum

> "The floor is `ceil(len(b) / len(a))` copies, because anything shorter cannot
> physically contain `b`. The ceiling is one copy more than that, because a match
> starts at most `len(a) - 1` characters into the first copy, so one extra copy
> covers every possible starting offset. That means I test exactly two candidates
> and never search a growing string"

Therefore,

1. Compute `copies = ceil(len(b) / len(a))` as the smallest number of copies whose
   total length is at least `len(b)`, because a shorter string cannot contain `b`
   at all and testing it would be wasted work. In Python `-(-x // y)` gives the
   ceiling with integer arithmetic and no float rounding risk
2. Build `a * copies` and run `kmp_search` on it looking for `b`. This is the
   cheapest candidate, so if it hits, that count is the answer and nothing else
   needs testing
3. If it misses, build `a * (copies + 1)` and search again. This is the only other
   candidate, because a match that failed to fit in `copies` copies must have
   started partway into the first copy, and one extra copy supplies every
   character such a match could still need
4. If that misses too, return `-1`. No larger `k` can help, since any occurrence in
   a longer repetition would be an occurrence of the same characters at the same
   offset within the first copy, and step 3 already covered every such offset
5. Use `kmp_search` rather than Python's `in`, since the interviewer asking this
   question is asking about the search, and KMP keeps each attempt linear in the
   length of the repeated string rather than quadratic

```python
def repeated_string_match(a: str, b: str) -> int:
    copies = -(-len(b) // len(a))  # ceiling division
    if kmp_search(a * copies, b) != -1:
        return copies
    if kmp_search(a * (copies + 1), b) != -1:
        return copies + 1
    return -1


assert repeated_string_match("abcd", "cdabcdab") == 3
assert repeated_string_match("a", "aa") == 2
assert repeated_string_match("abc", "abc") == 1
assert repeated_string_match("aa", "a") == 1
assert repeated_string_match("abc", "wxyz") == -1
```

Walking the first case by hand: `a = "abcd"` and `b = "cdabcdab"`, so
`copies = ceil(8 / 4) = 2` and the first candidate is `"abcdabcd"`, eight
characters long. `b` is not inside it, because `b` starts at offset 2 and would
need to run to offset 10. That rejected attempt is what forces the second, over
`"abcdabcdabcd"`, where `b` appears at index 2, so the answer is 3

- **Time Complexity:** `O(len(a) + len(b))`, because both candidates have length at
  most `len(a) + len(b) + len(a)`, and KMP is linear in the text plus the pattern,
  so the whole thing is two linear passes over strings of that size
- **Space Complexity:** `O(len(a) + len(b))`, dominated by materializing `a * k`
  as an actual string, with the `lps` table adding only `O(len(b))` on top

## Time and Space Complexity

Throughout, `n` is the length of the text being searched and `m` is the length of
the pattern

**Single-pattern search**

| Approach                     | Time                                                                                                                                                                        | Space                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Naive restart at every index | `O(n * m)`: each of the `n` start positions compares up to `m` characters before failing, and long agreeing runs make that the real cost rather than the worst case         | `O(1)`: two index variables and nothing else, which is why the failure is invisible in a space analysis                 |
| KMP                          | `O(n + m)`: `O(m)` to build the table plus `O(n)` for the scan, since the text pointer only moves forward and the fallbacks are bounded by the matches that paid for them   | `O(m)`: the `lps` table holds one integer per pattern character, and the text is never copied                           |
| Z algorithm                  | `O(n + m)`: one linear pass over the glued string `pattern + separator + text`, whose length is `n + m + 1`                                                                 | `O(n + m)`: the glued string and its Z array both span text and pattern together, which is strictly more than KMP needs |
| Rabin-Karp                   | `O(n + m)` expected: each window rolls in `O(1)` and verification is rare, but `O(n * m)` worst case when hashes collide at every position and each hit is verified in full | `O(1)`: one running hash, one pattern hash, and one precomputed weight, with no table                                   |

**Building the tables**

| Structure           | Time                                                                                                                                                                                                    | Space                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `lps` failure table | `O(m)` amortized across the loop: `length` rises at most once per index so at most `m` times total, and every fallback strictly lowers it, so the nested `while` cannot run more than `m` times overall | `O(m)`: one integer per character, returned to the caller and reusable across many searches |
| Z array             | `O(n)` amortized: the window's right edge only ever moves right, so every character it passes is compared once and the reused values inside the window cost nothing                                     | `O(n)`: one integer per character of the string it was built over                           |

**The workbook problems, all of which run one table build**

| Problem                    | Time                                                                                               | Space                                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Longest Happy Prefix       | `O(n)`: one table build over the whole string, then a slice of the prefix it names                 | `O(n)`: the table, plus `O(n)` for the returned slice, which is output rather than auxiliary              |
| Repeated Substring Pattern | `O(n)`: one table build, then a single modulo on the last entry                                    | `O(n)`: the table alone, since the answer is a boolean                                                    |
| Shortest Palindrome        | `O(n)`: one table build over `s + "#" + reversed(s)`, a string of length `2n + 1`, so still linear | `O(n)`: the glued string and its table are both about `2n` long, and the reversal allocates one more copy |

## Summary

- A **border** of a string is a piece that is both a proper prefix and a proper
  suffix, so `"aab"` is the longest border of `"aabaaab"` because those are its
  first three and its last three characters. Every algorithm in this topic is
  built on borders, and any interview question about a prefix that is also a
  suffix, a repeating block, or a palindromic prefix is a border question wearing
  a costume
- The naive search restarts at the next text index after every mismatch, which is
  `O(n * m)` and dies on inputs that agree for a long stretch before disagreeing.
  Searching `"a" * 10000 + "b"` for `"a" * 100 + "b"` costs it 1,000,001 character
  comparisons where KMP costs 20,100
  - The waste is that it discards a partial match it already paid to verify, when
    the border of that match is still known to line up
- The **failure table**, written `lps`, holds at index `i` the length of the
  longest border of `pattern[0..i]`, and it is built on the pattern alone with no
  reference to any text, so one build can serve many searches
  - The fallback line is `length = lps[length - 1]`, never `length -= 1`, because
    when a border fails to extend the next candidate is the longest border *of
    that border*, which the table already recorded
  - It has to be a `while` and not an `if`, since one fallback can also fail and
    several border lengths may be discarded before one extends or `length` hits 0
- **KMP** searches with two pointers where `i` walks the text and `j` counts
  matched pattern characters, and on a mismatch only `j` falls back through `lps`
  while `i` never moves backward. Building the table is `O(m)` and the scan is
  `O(n)`, giving `O(n + m)` time and `O(m)` space
  - The `O(m)` build survives its nested `while` by the same counting argument as
    a monotonic stack, since `length` gains at most `m` in total and each inner
    iteration strictly spends some of it
  - To collect every occurrence instead of the first, set `j = lps[j - 1]` after
    recording a hit, which slides by the border and catches overlaps
- Two problems are answered by the table's last entry with no search at all.
  **Longest Happy Prefix** is the slice `s[:lps[-1]]` by definition, and
  **Repeated Substring Pattern** is `n % (n - lps[-1]) == 0` because a border of
  length `b` is the same statement as a period of `n - b`, and a string tiles
  evenly exactly when its smallest period divides its length
  - The `lps[-1] > 0` guard is required, since a borderless string has period `n`,
    and `n % n == 0` would wrongly report that it repeats
- Gluing two strings around a **separator** that appears in neither and taking the
  longest border answers "what is the longest prefix of `X` that is also a suffix
  of `Y`". **Shortest Palindrome** is that trick with `Y = reversed(s)`, which
  finds the longest palindromic prefix, and the leftover tail reversed onto the
  front is the answer
  - Omitting the separator lets the border run past the middle, so `s = "aa"`
    reports a border of `"aaa"` that is longer than `s` itself
- The **Z array** stores at index `i` how far the prefix of the string reaches
  starting from `i`, which is the same information as `lps` pointed forward rather
  than backward. It runs in `O(n)` by reusing values inside the rightmost verified
  window, capped with `min(right - i, z[i - left])` so no claim is made about
  characters past `right`
  - Searching with it means building `z` over `pattern + separator + text` and
    looking for entries equal to `len(pattern)`, which costs `O(n + m)` space
    against KMP's `O(m)`, so KMP is the one to master
- **Rabin-Karp** hashes each length-`m` window as a base-`B` numeral modulo a large
  prime, and rolls that hash one step in `O(1)` by subtracting the leading
  character's weight, multiplying by the base, and adding the new one. It is
  `O(n + m)` expected and `O(1)` space, but `O(n * m)` worst case, since equal
  hashes are only candidates and every hit must be verified against the real
  substring
  - Prefer it when comparing **many** equal-length pieces, such as several
    patterns at once or a binary search on substring length, since hashes drop
    into a set for `O(1)` comparison. For one pattern, KMP is simpler and has no
    collision story to defend
- The mistakes that actually happen are moving the text pointer backward on a
  mismatch, which silently rebuilds the naive scan, and writing `length -= 1`
  instead of `length = lps[length - 1]`, which produces a table that looks
  plausible and is wrong
  - Two more are quiet in the same way. Skipping the substring verification after
    a Rabin-Karp hash hit gives an algorithm that is usually correct, and dropping
    the separator from a glued string lets a border cross the join

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is this really a search, or is it a border/period question with no text at all?
Can I define a border out loud, and give the borders of a short string on demand?
Can I raise the naive O(n*m) restart and name the input that kills it?
Does lps[i] mean the longest border of the prefix ending at i, and can I say it?
Is my fallback length = lps[length - 1], and never length -= 1?
Is the fallback a while loop, so several border lengths can be discarded in a row?
Does the text pointer ever move backward, and can I confirm out loud that it does not?
Do I handle an empty pattern before indexing pattern[j]?
Do I need the first occurrence, or all of them with j = lps[j - 1] after each hit?
For a period question: did I guard lps[-1] > 0 before the modulo?
For a glued string: is my separator guaranteed absent from both halves?
For Rabin-Karp: do I verify the real substring after a hash hit, and say why?
Am I searching one pattern (KMP) or comparing many windows (rolling hash)?
Can I volunteer O(n + m) time and O(m) space, and name which part is which?
```
