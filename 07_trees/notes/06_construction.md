# Tree Construction

## Pattern

Tree construction rebuilds a tree from ordered information.

The main job is to identify the root and determine which values belong to the left and right subtrees.

## Intuition

Every recursive call builds one subtree.

For that subtree, ask:

```text
What is the root?
What range belongs to the left subtree?
What range belongs to the right subtree?
```

## Sorted Array To BST

A sorted array becomes a balanced BST by choosing the middle value as root.

```text
middle -> root
left half -> left subtree
right half -> right subtree
```

Choosing the middle prevents the tree from becoming a linked list.

## Preorder + Inorder

Preorder tells you the root first:

```text
root, left, right
```

Inorder tells you the split:

```text
left, root, right
```

So the algorithm is:

```text
root = next preorder value
root index in inorder splits left and right
build left subtree
build right subtree
```

## Inorder + Postorder

Postorder tells you the root last:

```text
left, right, root
```

Inorder still gives the split.

The idea is the same, but root values are consumed from the end of postorder.

## Template: Range Recursion

```text
function build(left, right):
    if left > right:
        return None

    root_value = next root from traversal
    mid = inorder_index[root_value]

    root = TreeNode(root_value)
    root.left = build(left, mid - 1)
    root.right = build(mid + 1, right)
    return root
```

The exact order of building left/right depends on whether roots are consumed from preorder or postorder.

## Complexity

With a value-to-index map:

```text
Time: O(n)
Space: O(n)
```

Without the map, searching inorder repeatedly can become `O(n^2)`.

## Pitfalls

- Slicing arrays in every recursive call.
- Searching inorder linearly every time.
- Off-by-one errors in subtree ranges.
- Building left and right in the wrong order for postorder.
- Forgetting to return the root.

## Interview Checklist

Before coding, make sure you can answer:

```text
Which traversal tells me the root (preorder = first, postorder = last), and which gives the left/right split (inorder)?
Am I using a value-to-index map for inorder lookups instead of searching linearly each call?
What are the exact left/right index ranges for the current subtree, and where's the off-by-one risk?
If building from postorder, am I consuming root values from the end and building right before left?
Why does slicing arrays at each call blow up the complexity, and how does index-range recursion avoid it?
```
