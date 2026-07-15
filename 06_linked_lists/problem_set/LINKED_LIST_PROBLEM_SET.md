# Linked Lists Problem Set

## Goal

Build linked list intuition across the core pointer-manipulation
techniques — single-pass traversal, fast/slow pointers, in-place reversal,
merge/split, and restructuring — then use each technique to solve the medium
and hard linked list problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one linked list
technique. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function in
that section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Traversal

`traversal_problems.py` — single-pass pointer walks: reverse, merge, and
unlink nodes with a dummy head.

### 1. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

- solves: `reverse_list`
- Pattern: walk the list flipping each `next` pointer.

### 2. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- solves: `merge_two_lists`
- Pattern: weave two lists with a dummy head.

### 3. [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

- solves: `delete_duplicates`
- Pattern: skip a node whose value equals the next.

### 4. [Delete Node In A Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

- solves: `delete_node`
- Pattern: copy the next node's value, then unlink it.

### 5. [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

- solves: `remove_elements`
- Pattern: dummy head plus a previous pointer to unlink matches.

### 6. [Intersection Of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

- solves: `get_intersection_node`
- Pattern: two pointers that switch lists to align lengths.

### 7. [Design Linked List](https://leetcode.com/problems/design-linked-list/)

- solves: `MyLinkedList`
- Pattern: implement get, insert, and delete on a from-scratch list.

### 8. [Convert Binary Number In A Linked List To Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

- solves: `get_decimal_value`
- Pattern: single pass building the value with shift-and-add.

## Fast And Slow Pointers

`fast_slow_problems.py` — two-speed pointers to find the middle, detect
cycles, and reach the nth-from-end node in one pass.

### 9. [Middle Of The Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

- solves: `middle_node`
- Pattern: slow moves one step, fast moves two.

### 10. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

- solves: `has_cycle`
- Pattern: fast catches slow if a cycle exists.

### 11. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

- solves: `detect_cycle`
- Pattern: after the meeting point, walk from head to the cycle start.

### 12. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

- solves: `is_palindrome`
- Pattern: find the middle, reverse the second half, compare.

### 13. [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

- solves: `remove_nth_from_end`
- Pattern: gap of `n` between two pointers.

### 14. [Delete The Middle Node Of A Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

- solves: `delete_middle`
- Pattern: slow/fast to find the middle, keep a trailing pointer to unlink it.

## Reversal

`reversal_problems.py` — in-place pointer reversal of sublists and
fixed-size groups.

### 15. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

- solves: `reverse_between`
- Pattern: reverse only the sublist between two positions.

### 16. [Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

- solves: `swap_pairs`
- Pattern: reverse in fixed groups of two.

### 17. [Reverse Nodes In K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

- solves: `reverse_k_group`
- Pattern: reverse fixed-size groups, leave the remainder.

### 18. [Maximum Twin Sum Of A Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

- solves: `twin_sum`
- Pattern: reverse the second half, then pair it against the first half.

### 19. [Swapping Nodes In A Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

- solves: `swap_nodes`
- Pattern: two pointers a gap of k apart to reach both ends.

## Merge And Split

`merge_split_problems.py` — combine, divide, or arithmetically process
lists.

### 20. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

- solves: `add_two_numbers`
- Pattern: digit-by-digit addition with a carry.

### 21. [Partition List](https://leetcode.com/problems/partition-list/)

- solves: `partition`
- Pattern: build two lists, then splice them.

### 22. [Sort List](https://leetcode.com/problems/sort-list/)

- solves: `sort_list`
- Pattern: merge sort using slow/fast to split.

### 23. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- solves: `merge_k_lists`
- Pattern: min-heap or pairwise merge.

### 24. [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

- solves: `add_two_numbers_ii`
- Pattern: most-significant-digit first, so use stacks or reverse.

### 25. [Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/)

- solves: `merge_in_between`
- Pattern: cut a node range and splice another list in by index.

## Restructure

`restructure_problems.py` — rearrange nodes into a new ordering.

### 26. [Reorder List](https://leetcode.com/problems/reorder-list/)

- solves: `reorder_list`
- Pattern: split, reverse the second half, weave.

### 27. [Rotate List](https://leetcode.com/problems/rotate-list/)

- solves: `rotate_right`
- Pattern: close into a ring, then reopen at the new head.

### 28. [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

- solves: `odd_even_list`
- Pattern: thread odd and even indices into two chains.

### 29. [Split Linked List In Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

- solves: `split_list_to_parts`
- Pattern: size each part, then cut.

### 30. [Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/)

- solves: `remove_nodes`
- Pattern: reverse, drop nodes below the running max, reverse back.

## Hards And Extensions

`advanced_problems.py` — linked list hards and follow-ups: duplicate runs,
random/child pointers, and doubly-linked-list-backed caches.

### 31. [Remove Duplicates From Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

- solves: `delete_duplicates_ii`
- Pattern: dummy head, skip every node in a duplicate run.

### 32. [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

- solves: `copy_random_list`
- Pattern: map old nodes to clones, then wire pointers.

### 33. [Flatten A Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

- solves: `flatten`
- Pattern: splice each child list inline using a stack.

### 34. [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)

- solves: `next_larger_nodes`
- Pattern: monotonic stack over the values in one pass.

### 35. [Reverse Nodes In Even Length Groups](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/)

- solves: `reverse_even_length_groups`
- Pattern: walk growing groups, reverse only the even-length ones.
  </content>
  </invoke>
