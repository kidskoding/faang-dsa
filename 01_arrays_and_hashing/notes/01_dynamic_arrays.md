# Dynamic Arrays

## Pattern

A dynamic array stores values in contiguous index order and grows when it runs out of capacity.

In Python, `list` behaves like a dynamic array.

## Intuition

Arrays are good when you need:

- fast access by index
- scanning left to right
- in-place swaps
- building answer lists
- prefix or suffix information

The tradeoff is that inserting or deleting from the middle forces elements to shift.

## How It Works

A dynamic array tracks two different ideas:

```text
size = number of actual elements
capacity = amount of allocated space
```

When size reaches capacity, the array allocates a larger block and copies old values into it.

That copy is expensive when it happens, but it does not happen every append.

## Template

```text
arr = []
for value in input:
    arr.append(value)
```

For in-place updates:

```text
for i in range(len(arr)):
    arr[i] = transformed value
```

## Example

Appending four values might look like:

```text
capacity 1: [10]
capacity 2: [10, 20]
capacity 4: [10, 20, 30, 40]
```

The resize copies old values, then future appends are cheap again.

## Complexity

```text
index access: O(1)
append: amortized O(1)
insert/delete middle: O(n)
scan: O(n)
```

Amortized means the average cost over many appends is `O(1)`, even though one resize can cost `O(n)`.

## Pitfalls

- Forgetting middle insert/delete shifts elements.
- Mutating a list while iterating over it in a way that changes indices.
- Confusing output list space with auxiliary space.
- Using repeated string concatenation when a list plus join would be cleaner.

## Interview Checklist

Before coding, make sure you can answer:

```text
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
