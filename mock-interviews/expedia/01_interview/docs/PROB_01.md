# Basic Calculator II

Source: [LeetCode 227](https://leetcode.com/problems/basic-calculator-ii/)

Given a string `s` representing a valid arithmetic expression, evaluate it and
return the result.

The expression contains only non-negative integers and the operators `+`, `-`,
`*`, and `/`, separated by spaces. There are no parentheses. Integer division
truncates toward zero.

## Examples

### Example 1

```python
Input:  s = "3+2*2"
Output: 7
```

### Example 2

```python
Input:  s = " 3/2 "
Output: 1
```

### Example 3

```python
Input:  s = " 3+5 / 2 "
Output: 5
```

## Constraints

```text
1 <= s.length <= 3 * 10^5
s consists of integers and operators (+, -, *, /) separated by spaces
s represents a valid expression
All integers are in the range [0, 2^31 - 1]
The answer is guaranteed to fit in a 32-bit integer
Integer division truncates toward zero
```

