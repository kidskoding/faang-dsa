# Linked Lists Problem Set

## Goal

Build linked list intuition from the ground up, then use that foundation to solve the medium and hard pointer-manipulation problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the linked list basics you should be able to do without thinking too hard.

### 1. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

- Pattern: walk the list flipping each `next` pointer.

### 2. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- Pattern: weave two lists with a dummy head.

### 3. [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

- Pattern: skip a node whose value equals the next.

### 4. [Delete Node In A Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

- Pattern: copy the next node's value, then unlink it.

### 5. [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

- Pattern: dummy head plus a previous pointer to unlink matches.

### 6. [Intersection Of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

- Pattern: two pointers that switch lists to align lengths.

## Fast And Slow Pointers

These use the two-speed pointer trick to find structure in one pass.

### 7. [Middle Of The Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

- Pattern: slow moves one step, fast moves two.

### 8. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

- Pattern: fast catches slow if a cycle exists.

### 9. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

- Pattern: after the meeting point, walk from head to the cycle start.

### 10. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

- Pattern: find the middle, reverse the second half, compare.

### 11. [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

- Pattern: gap of `n` between two pointers.

## Reversal

These are the in-place pointer-reversal mediums.

### 12. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

- Pattern: reverse only the sublist between two positions.

### 13. [Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

- Pattern: reverse in fixed groups of two.

### 14. [Reverse Nodes In K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

- Pattern: reverse fixed-size groups, leave the remainder.

## Merge And Split

These combine, divide, or arithmetically process lists.

### 15. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

- Pattern: digit-by-digit addition with a carry.

### 16. [Partition List](https://leetcode.com/problems/partition-list/)

- Pattern: build two lists, then splice them.

### 17. [Sort List](https://leetcode.com/problems/sort-list/)

- Pattern: merge sort using slow/fast to split.

### 18. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- Pattern: min-heap or pairwise merge.

## Restructure

These rearrange nodes into a new ordering.

### 19. [Reorder List](https://leetcode.com/problems/reorder-list/)

- Pattern: split, reverse the second half, weave.

### 20. [Rotate List](https://leetcode.com/problems/rotate-list/)

- Pattern: close into a ring, then reopen at the new head.

### 21. [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

- Pattern: thread odd and even indices into two chains.

### 22. [Split Linked List In Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

- Pattern: size each part, then cut.

## Hards And Extensions

These are the linked list follow-ups that push beyond the standard medium set.

### 23. [Remove Duplicates From Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

- Pattern: dummy head, skip every node in a duplicate run.

### 24. [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

- Pattern: map old nodes to clones, then wire pointers.

### 25. [Flatten A Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

- Pattern: splice each child list inline using a stack.

### 26. [LRU Cache](https://leetcode.com/problems/lru-cache/)

- Pattern: hash map plus a doubly linked list for O(1) eviction.

## Recommended Order

If you want the shortest path to linked list fluency, do them in this order:

```text
1. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
2. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
3. [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
4. [Middle Of The Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
5. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
6. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
7. [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
8. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
9. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
10. [Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
11. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
12. [Reorder List](https://leetcode.com/problems/reorder-list/)
13. [Sort List](https://leetcode.com/problems/sort-list/)
14. [Reverse Nodes In K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
15. [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
16. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
17. [LRU Cache](https://leetcode.com/problems/lru-cache/)
```
