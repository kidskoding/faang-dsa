# Roman To Integer

Roman numerals are written using the following symbols:

```text
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

Given a string `s` representing a valid Roman numeral, return its integer value.

Roman numerals are usually read from left to right by adding symbol values. In
some cases, a smaller symbol appears before a larger symbol to represent
subtraction.

The subtractive cases are:

```text
I before V or X
X before L or C
C before D or M
```

Example 1:
Input:
s = "III"
Output: 3

Example 2:
Input:
s = "LVIII"
Output: 58
Explanation:
L = 50, V = 5, and III = 3.

Example 3:
Input:
s = "MCMXCIV"
Output: 1994
Explanation:
M = 1000, CM = 900, XC = 90, and IV = 4.

Constraints:
1 \<= len(s) \<= 15
s contains only the characters I, V, X, L, C, D, and M
s is guaranteed to be a valid Roman numeral in the range [1, 3999]
