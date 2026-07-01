# BST

## Pattern

A binary search tree is a binary tree with ordering constraints.

For every node:

```text
all values in left subtree  < node.val
all values in right subtree > node.val
```

The constraint applies to the entire subtree, not just direct children.

## Intuition

BST problems are faster because the ordering tells you which side matters.

For search, insert, and LCA, you can often move left or right without exploring both sides.

For validation, you must track the allowed range from ancestors.

## Template: Search

```text
function search(node, target):
    if node is None:
        return None

    if target < node.val:
        return search(node.left, target)
    if target > node.val:
        return search(node.right, target)
    return node
```

## Template: Validate With Bounds

```text
function valid(node, low, high):
    if node is None:
        return true

    if node.val <= low or node.val >= high:
        return false

    return valid(node.left, low, node.val) and valid(node.right, node.val, high)
```

This catches violations from ancestors.

## Template: Inorder Sorted Order

```text
inorder(left)
visit node
inorder(right)
```

For a valid BST, inorder traversal produces values in sorted order.

That is the key idea behind kth-smallest.

## Insert Mental Model

Insertion descends until it finds an empty spot.

The recursive call returns the subtree root, so assign it back:

```text
root.left = insert(root.left, val)
root.right = insert(root.right, val)
```

If the subtree was empty, the returned value is the new node.

## Delete Mental Model

Delete has three structural cases:

```text
no children: return None
one child: return that child
two children: replace value with inorder successor, then delete successor
```

The inorder successor is the minimum node in the right subtree.

## Complexity

Balanced BST:

```text
Time: O(log n)
Space: O(log n)
```

Skewed BST:

```text
Time: O(n)
Space: O(n)
```

## Pitfalls

- Checking only direct children in Validate BST.
- Forgetting ancestor bounds.
- Forgetting to assign recursive insert/delete results.
- Handling duplicates inconsistently.
- Replacing a deleted node with the successor but not removing the successor from its old spot.

## Interview Checklist

Before coding, make sure you can answer:

```text
Can this problem be solved by moving only left or right, or does it require exploring both sides?
For validation, am I checking the full ancestor range, not just the immediate parent?
Am I reassigning the recursive result back to `.left`/`.right` in insert/delete?
For delete with two children, which node replaces the deleted value, and how is it removed from its old spot?
Why does the BST property make this O(log n) on a balanced tree but O(n) on a skewed one?
```
