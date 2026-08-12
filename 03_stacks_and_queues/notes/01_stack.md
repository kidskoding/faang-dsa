# Stacks

A **stack** is a data structure where items are added and removed at the same
end, called the **top**. The item added most recently is therefore the first one
to come back out. This rule is called **last-in, first-out (LIFO)**.

Think of a pile of plates. You put a clean plate on top and take the top plate
when you need one. Reaching a plate lower in the pile means removing everything
above it first.

A stack supports three basic operations:

- **push** adds an item to the top
- **pop** removes and returns the top item
- **peek** (or `top`) reads the top item without removing it

```text
push 4       push 9       push 2       pop -> 2

                           | 2 |
              | 9 |        | 9 |         | 9 |
  | 4 |       | 4 |        | 4 |         | 4 |
  +---+       +---+        +---+         +---+
```

In Python, a `list` already provides the right operations. `append` pushes,
`pop()` pops, and `stack[-1]` peeks. All three touch the right end of the list,
so they take `O(1)` amortized time as covered in
[dynamic arrays](../../01_arrays_and_hashing/notes/01_dynamic_arrays.md).

```python
stack: list[int] = []
stack.append(4)
stack.append(9)
top = stack[-1]  # 9
removed = stack.pop()  # 9
```

Do not use `pop(0)` for a stack. It removes from the wrong end and shifts every
remaining item, so it costs `O(n)` instead of `O(1)`.

## When To Use A Stack

Stacks fit problems where the **newest unresolved item must be handled next**.
That usually appears in one of these forms:

- The input is nested, as with brackets, encoded strings, expressions, or file
  paths. The innermost section opens last and must close first
- Values wait for something later to resolve them, as operands wait for an
  operator or opening brackets wait for a closer
- An operation must be undone in reverse order, as with browser history or an
  editor's undo feature
- A problem asks you to simulate pushes and pops, or repeatedly compare an
  arriving item with the most recent survivor

If the **oldest** waiting item must be handled next, use a
[queue](02_queue_and_deque.md) instead. The quickest interview check is to ask,
“Do I need the newest unfinished item or the oldest waiting item?”

## Why Counting Open Brackets Is Not Enough

For one type of parenthesis, a counter almost works: add one for `(`, subtract
one for `)`, reject if the count becomes negative, and accept if it finishes at
zero. With several bracket types, however, a count forgets which opener is on
the inside.

```text
s = "([)]"

'('  count=1
'['  count=2
')'  count=1
']'  count=0   <- the counts balance, but the pairs cross
```

The `)` cannot close while `[` is the newest unmatched opener. A stack remembers
both the bracket type and the order, which is exactly the information the
counter lost.

```python
def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

The dictionary is keyed by closing brackets because the closer is what arrives
when a lookup is needed. `not stack` guards an unmatched closer such as `")"`,
and Python stops before calling `pop()` on the empty list. The final
`return not stack` rejects unmatched openers such as `"(("`.

```text
s = "()[)]"

'('  push                         stack=['(']
')'  pop '('; it matches          stack=[]
'['  push                         stack=['[']
')'  pop '['; wanted '('          REJECT
```

That rejected closer is the important branch. The stack does not merely say
that something is open. It says that `[` is the only opener the next closer is
allowed to match.

## Saving A Job While A Nested Job Runs

Bracket matching stores one pending token. Parsing a nested expression often
needs to store the entire **unfinished state** of the outer job.

For example, `"3[a2[c]]"` decodes to `"accaccacc"`. At each `[`, the string
built so far and the repeat count are both unfinished, so they are pushed
together. The inner section then starts with fresh state. At `]`, the saved
state is restored and combined with the completed inner result.

```python
def decode_string(s: str) -> str:
    stack: list[tuple[str, int]] = []
    current = ""
    count = 0
    for ch in s:
        if ch.isdigit():
            count = count * 10 + int(ch)
        elif ch == "[":
            stack.append((current, count))
            current = ""
            count = 0
        elif ch == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat
        else:
            current += ch
    return current
```

`count = count * 10 + int(ch)` matters because repeat counts may have several
digits. Resetting `current` matters because the outer text must not be repeated
as part of the inner section.

```text
s = "2[ab3[c]]"

'2['   save ('', 2)          current=''       stack=[('', 2)]
'ab'                          current='ab'     stack=[('', 2)]
'3['   save ('ab', 3)        current=''       stack=[('', 2), ('ab', 3)]
'c]'   restore ('ab', 3)     current='abccc'  stack=[('', 2)]
']'    restore ('', 2)       current='abcccabccc'
```

At the second `[`, `"ab"` disappears from the working variable but is not lost.
It is parked on the stack while the nested `c` section runs. Basic Calculator
uses the same idea with a running result and sign, while Number Of Atoms parks a
map of element counts.

**Basic Calculator** reads a multi-digit number with
`number = number * 10 + int(ch)`. When `+` or `-` arrives, it applies the previous
sign with `result += sign * number`, then clears `number` and remembers the new
sign. A `(` suspends the result and sign from before the parentheses. A `)` first
finishes the number inside, then multiplies that subtotal by the saved sign and
adds the saved result.

```python
def calculate(expression: str) -> int:
    stack: list[int] = []
    result = number = 0
    sign = 1

    for ch in expression:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch in "+-":
            result += sign * number
            number = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = number = 0
            sign = 1
        elif ch == ")":
            result += sign * number
            number = 0
            result *= stack.pop()  # sign before '('
            result += stack.pop()  # result before '('

    return result + sign * number
```

The sign is pushed after the result, so it comes back first. On `"1-(2+3)"`, the
inner subtotal 5 is multiplied by `-1` and then added to the saved result 1,
giving `-4`. Reversing those two pushes restores the wrong facts into the wrong
roles.

**Number Of Atoms** changes the saved state from integers to count maps. An
uppercase letter plus its following lowercase letters form one atom token, and
the digits after that token form its count. `(` starts a fresh map. At `)`, parse
the multiplier, pop the completed inner map, multiply every count, and merge it
into the map below.

```python
def count_of_atoms(formula: str) -> str:
    stack: list[dict[str, int]] = [{}]
    i = 0

    while i < len(formula):
        if formula[i] == "(":
            stack.append({})
            i += 1
        elif formula[i] == ")":
            i += 1
            start = i
            while i < len(formula) and formula[i].isdigit():
                i += 1
            multiplier = int(formula[start:i] or "1")
            group = stack.pop()
            for atom, count in group.items():
                stack[-1][atom] = stack[-1].get(atom, 0) + count * multiplier
        else:
            start = i
            i += 1
            while i < len(formula) and formula[i].islower():
                i += 1
            atom = formula[start:i]

            start = i
            while i < len(formula) and formula[i].isdigit():
                i += 1
            count = int(formula[start:i] or "1")
            stack[-1][atom] = stack[-1].get(atom, 0) + count

    counts = stack[0]
    return "".join(
        atom + (str(counts[atom]) if counts[atom] > 1 else "")
        for atom in sorted(counts)
    )
```

For `"Mg(OH)2"`, the inner map becomes `{'O': 1, 'H': 1}`. Closing the group
multiplies it to `{'O': 2, 'H': 2}` and merges those counts beside `Mg`. Sorting
the final atom names produces the required `"H2MgO2"` output.

## Decide What Each Stack Entry Must Remember

The operations hardly change between stack problems. The main design decision
is what one stack entry stores.

**Store values** when later tokens consume earlier values. Reverse Polish
Notation puts operands on the stack, then pops the right operand before the left
operand whenever an operator arrives.

```python
def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            stack.append(int(left / right))
    return stack[-1]
```

The pop order is load-bearing. Swapping `left` and `right` still passes addition
and multiplication but silently reverses subtraction and division. Basic
Calculator II makes a different parsing choice: it resolves multiplication and
division immediately, while signed addition terms wait on the stack for a final
sum.

**Store a pair** when two facts must be restored together. Min Stack stores the
minimum seen at every depth beside the value. A single `minimum` variable cannot
recover the previous minimum after the current minimum is popped.

```python
class MinStack:
    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []

    def push(self, value: int) -> None:
        minimum = value if not self.stack else min(value, self.stack[-1][1])
        self.stack.append((value, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]
```

Pairs also compress repeated state. Remove Adjacent Duplicates II stores
`(character, count)`, Stock Span later stores `(price, span)`, and a frequency
stack keeps a separate stack for each frequency so ties still resolve by recency.

Maximum Frequency Stack makes that last idea concrete. `freq[value]` records the
value's current frequency, `groups[f]` is a stack of values at frequency `f` in
arrival order, and `max_freq` points at the only group `pop` may use. When that
group becomes empty, decrementing `max_freq` exposes the next non-empty group.

```python
class FreqStack:
    def __init__(self) -> None:
        self.freq: dict[int, int] = {}
        self.groups: dict[int, list[int]] = {}
        self.max_freq = 0

    def push(self, value: int) -> None:
        frequency = self.freq.get(value, 0) + 1
        self.freq[value] = frequency
        self.groups.setdefault(frequency, []).append(value)
        self.max_freq = max(self.max_freq, frequency)

    def pop(self) -> int:
        value = self.groups[self.max_freq].pop()
        self.freq[value] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return value
```

Values tied at `max_freq` come from the same list, so its normal LIFO pop returns
the most recent tied value without comparing timestamps.

**Store indices** when the answer depends on a position or distance. Minimum
Remove To Make Valid Parentheses needs to delete specific characters, Longest
Valid Parentheses measures a span, and the next note's
[monotonic stacks](03_monotonic_stack.md) use indices to recover distances and
boundaries.

Longest Valid Parentheses starts its index stack with `-1`, a sentinel boundary
just before the string. An unmatched `)` replaces that boundary with its own
index. After a successful match, the current valid suffix begins one position
after the boundary now on top, so its length is `i - stack[-1]`.

```python
def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    best = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # unmatched ')' becomes the new boundary
            else:
                best = max(best, i - stack[-1])

    return best
```

On `")()())"`, index 0 is an unmatched boundary. The matches ending at indices
2 and 4 measure `2 - 0 = 2` and `4 - 0 = 4`. Index 5 is unmatched, so it becomes
the next boundary rather than contributing a length.

Some problems use the stack as the result under construction. Simplify Path
pushes directory names and pops on `..`; Remove Adjacent Duplicates pushes
characters and pops equal neighbors. Validate Stack Sequences is more literal:
simulate each requested push, then greedily pop while the top matches the next
required output.

## Worked Example: [Minimum Remove To Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

You are given a string of lowercase letters and parentheses. Remove the fewest
parentheses needed to make it valid, keeping all letters and the order of every
remaining character. More than one valid result may exist.

This is bracket matching with one important change: the answer is a string, not
a boolean. Therefore, the stack must remember **which positions** are unmatched,
not merely which bracket character appeared.

An unmatched `)` is known immediately because no opener is waiting for it. An
unmatched `(` is known only after the scan, because a matching closer might still
appear later. Copy the string to a list, blank invalid positions without shifting
the remaining indices, then join the characters at the end.

> “I’ll keep the indices of unmatched opening parentheses. A closing parenthesis
> either consumes the newest opener or, if none exists, marks itself for removal.
> After the scan, the indices still on the stack are exactly the openers that
> never found a closer.”

```python
def min_remove_to_make_valid(s: str) -> str:
    chars = list(s)
    open_indices: list[int] = []

    for i, ch in enumerate(chars):
        if ch == "(":
            open_indices.append(i)
        elif ch == ")":
            if open_indices:
                open_indices.pop()
            else:
                chars[i] = ""

    for i in open_indices:
        chars[i] = ""

    return "".join(chars)
```

- **Time Complexity:** `O(n)` for a string of length `n`, because the scan, the
  cleanup of at most `n` unmatched indices, and the final join are all linear
- **Space Complexity:** `O(n)`, because the character copy and a string of all
  `(` can each occupy linear space

Trace `s = "a)b(c)d("`:

```text
i=0  'a'   keep                         open=[]
i=1  ')'   no opener -> blank it        open=[]       REJECTED CLOSER
i=2  'b'   keep                         open=[]
i=3  '('   push index 3                 open=[3]
i=4  'c'   keep                         open=[3]
i=5  ')'   pop index 3; pair matched    open=[]
i=6  'd'   keep                         open=[]
i=7  '('   push index 7                 open=[7]
end        index 7 never closed -> blank it

result = "ab(c)d"
```

Deleting from the list during the scan would shift later indices and make the
stored positions wrong. Blanking first preserves every index until matching is
finished.

## Time and Space Complexity

Let `n` be the number of input items.

| Approach        | Time                                                              | Space                                                                            |
| --------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Stack scan      | `O(n)`: every item is pushed at most once and popped at most once | `O(n)`: an input with nothing resolved can leave all `n` items on the stack      |
| Bracket counter | `O(n)`: it makes one pass over the input                          | `O(1)`: it stores one integer, but it is incorrect when bracket types must match |

A loop that pops inside a loop that pushes is not automatically `O(n²)`. If each
item can enter once and leave once, the total number of stack operations is
linear. This one-push, one-pop argument is the standard
[amortized analysis](../../00_fundamentals/notes/03_time_and_space_complexity.md)
for stack problems.

## Summary

- A **stack** adds and removes at the same end, called the top, so it follows
  **LIFO: Last In First Out**
  - In Python, use `list.append`, `list.pop()`, and `stack[-1]`; do not use
    `pop(0)`, because removing from the front shifts the remaining values
- Reach for a stack when the newest unresolved item must be handled next, which
  commonly appears as nesting, matching, parsing, evaluation, undo, or simulation
- A counter cannot validate several bracket types because it remembers how many
  openers exist but forgets their types and nesting order
  - Guard every pop against an empty stack, and check for leftover entries after
    the scan when they represent unfinished input
- Nested parsers push the unfinished outer state, clear the working state for the
  inner section, and restore the outer state when the section closes
- Decide what one entry must remember before coding: a value for evaluation, an
  index for positions and spans, or a tuple when several facts change together
- A stack scan is `O(n)` time when each item is pushed once and popped at most
  once, and it uses `O(n)` space when every item can remain pending

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Does the newest unresolved item need to be handled next, or the oldest?
What exactly belongs in one entry: a value, an index, or several facts?
What event causes a push, and what event causes a pop?
Can a closer or operator arrive when the stack is empty?
Do entries left at the end mean failure, or are they part of the answer?
If the input is nested, what outer state must be saved and restored?
If I pop two operands, which one is the left operand?
Am I mutating a sequence in a way that shifts indices I still need?
Can I justify linear time by counting one push and one pop per item?
```
