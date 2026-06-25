# Problem 2: Count Valid Routes

Source: [Advent of Code 2025 - Day 11: Reactor](https://adventofcode.com/2025/day/11)

You are given a list of route descriptions. Each description contains one name, followed by the names that can be reached directly from it.

Count how many distinct routes from `"svr"` to `"out"` pass through both
`"dac"` and `"fft"`. They may appear in either order.

Two paths are distinct if their sequences of nodes are different.

## Examples

### Example 1

```python
Input:
routes = [
    "svr: aaa bbb",
    "aaa: fft",
    "fft: ccc",
    "bbb: tty",
    "tty: ccc",
    "ccc: ddd eee",
    "ddd: hub",
    "hub: fff",
    "eee: dac",
    "dac: fff",
    "fff: ggg hhh",
    "ggg: out",
    "hhh: out",
]

Output:
2

Explanation:
There are eight paths from "svr" to "out", but only two visit both "dac" and
"fft".
```

### Example 2

```python
Input:
routes = [
    "svr: dac",
    "dac: fft",
    "fft: out",
]

Output:
1
```

### Example 3

```python
Input:
routes = [
    "svr: dac fft",
    "dac: out",
    "fft: out",
]

Output:
0

Explanation:
Each route visits only one required name.
```

## Constraints

```text
1 <= len(routes) <= 10^4
Each route description has the format "name: next1 next2 ..."
Names are non-empty lowercase strings
The route descriptions do not contain cycles
"svr", "out", "dac", and "fft" are present
The answer fits in a signed 64-bit integer
```
