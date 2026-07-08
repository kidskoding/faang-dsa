# Breaking the Cycle

**Difficulty:** Medium

Closest LeetCode: [142 - Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
(cycle detection; here you extend it to collect every node on the loop). Base
detection is [141 - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/).

## Description

All the clues that lead us in circles are false evidence we need to purge!
Given the head of a linked list `evidence`, clean up the evidence list by
identifying any false clues.

Write a function `collect_false_evidence()` that returns an array containing all
values that are part of any cycle in `evidence`. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables
and provide a rationale for why you believe your solution has the stated time
and space complexity.

## Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def collect_false_evidence(evidence):
    pass
```

## Examples

### Example 1

```
Input:  Linked list with 4 clues where the 4th clue points to the 2nd clue
        clue1 -> clue2 -> clue3 -> clue4 -> clue2

Output: ['The stolen goods are at an abandoned warehouse',
         'The mayor is accepting bribes',
         'They dumped their disguise in the lake']
```

### Example 2

```
Input:  Linked list with no cycle
        clue5 -> clue6 -> clue7

Output: []
```
