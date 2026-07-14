# KMP, Z Algorithm, And Rabin-Karp

## Pattern

Advanced string algorithms avoid rechecking characters after partial matches.

## Intuition

They precompute how much prefix information can be reused.

## How It Works

Use when repeated pattern matching must be linear.

## Template

```text
build prefix table
scan text using table to skip fallback comparisons
```

## Example

KMP matches a pattern in text without moving the text pointer backward.

## Complexity

```text
Time O(n+m)
Space O(m)
```

## Pitfalls

- Trying to memorize without understanding prefix reuse.
- Using advanced string algorithms when simple hash/trie is enough.
- Off-by-one prefix table bugs.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I building a prefix/failure table (KMP) or a Z-array, and what does each entry mean?
Why does the text pointer never move backward, only the pattern pointer via the fallback table?
On a mismatch, how does the table tell me how much matched prefix I can safely reuse?
Is the table built on the pattern alone, or on pattern+separator+text (Z-algorithm)?
Would a simpler hash-based or built-in substring check meet the requirement instead?
```

______________________________________________________________________

# Rabin-Karp And Rolling Hash

## Pattern

Compare fixed-length windows by a number, not character by character. Turn each
length-`m` window into a hash so a window comparison is O(1) instead of O(m).

## Intuition

Treat a window as a base-`B` number mod a large prime. Sliding one step right
drops the leftmost character and appends a new one — both are arithmetic, so the
next hash comes from the old one in O(1) instead of rebuilding it.

## How It Works

```text
hash("abc") = (a*B^2 + b*B^1 + c*B^0) mod M
slide by one:
  remove leading digit:  h = (h - a*B^(m-1)) mod M
  shift left:            h = (h * B) mod M
  add new trailing digit: h = (h + d) mod M
```

Equal hashes are a *candidate* match — a hash collision is possible, so verify
the actual substring on a hit (or use double hashing / a huge prime to make
collisions negligible).

## Template

```text
precompute B^(m-1) mod M
roll the hash across the text, one window at a time
on a hash hit, confirm the real substring equals the pattern
```

## When To Reach For It Over KMP

- Multiple patterns of the same length searched at once (hash them into a set).
- Comparing/deduping many equal-length substrings (e.g. distinct substrings).
- Binary-search-on-length problems: check "does any length-`L` substring repeat?"
  in O(n) per length with a hash set — the core of Longest Duplicate Substring.

## Complexity

```text
Time  O(n + m) average, O(n*m) worst case (all hashes collide)
Space O(1) for single-pattern search, O(k) if storing seen hashes
```

## Pitfalls

- Forgetting to take mod at every step → integer overflow in fixed-width langs
  (Python bigints hide this, but interviewers expect the mod).
- Treating equal hashes as a guaranteed match — always verify, or double-hash.
- A small modulus or base → frequent collisions and O(n*m) blowup.
- Recomputing `B^(m-1)` inside the loop instead of once up front.

## Interview Checklist

```text
What are my base B and modulus M, and why a large prime for M?
How do I add/remove one character from the rolling hash in O(1)?
On a hash match, do I verify the real substring (collision safety)?
Would double hashing (two independent moduli) remove my collision risk?
Is this a "search one pattern" job (KMP is simpler) or a "compare many windows" job (Rabin-Karp wins)?
```
