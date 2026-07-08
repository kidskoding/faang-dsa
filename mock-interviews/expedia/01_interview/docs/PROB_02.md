# Basic Calculator III (Follow Up of Previous Problem)

Source: [LeetCode 772](https://leetcode.com/problems/basic-calculator-iii/)

Follow up to Problem 1. Now the expression can also contain **parentheses**,
nested arbitrarily deep, in addition to `+`, `-`, `*`, and `/`.

Given a string `s` representing a valid arithmetic expression, evaluate it and
return the result. The expression contains non-negative integers, the operators
`+ - * /`, parentheses `(` `)`, and spaces. Integer division truncates toward
zero.

## Examples

### Example 1

```python
Input:  s = "1+1"
Output: 2
```

### Example 2

```python
Input:  s = "6-4/2"
Output: 4
```

### Example 3

```python
Input:  s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

## Constraints

```text
1 <= s.length <= 10^4
s consists of digits, '+', '-', '*', '/', '(', ')', and ' '
s is a valid expression
All intermediate values are in the range [-2^31, 2^31 - 1]
Integer division truncates toward zero
```
