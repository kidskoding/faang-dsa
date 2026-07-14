# Tree Fundamentals

## Pattern

Binary trees are recursive structures. Every node is the root of a smaller binary tree.

Most tree problems reduce to this question:

```text
What answer should this node return to its parent?
```

Once that return value is clear, the recursive solution becomes much easier.

## Intuition

At any node, you usually do three things:

1. Ask the left child for information.
1. Ask the right child for information.
1. Combine those answers with the current node.

That gives this general shape:

```text
left_answer = solve(node.left)
right_answer = solve(node.right)
return combine(left_answer, right_answer, node.val)
```

## How It Works

A tree problem is not solved by thinking about the whole tree at once. Think about one node.

For one node, decide:

- What does an empty subtree return?
- What does the left subtree return?
- What does the right subtree return?
- What does the current node return upward?

Examples of return meanings:

```text
height(node) returns the height of this subtree
same_tree(p, q) returns whether these two subtrees are identical
invert(node) returns the root after this subtree is inverted
```

## Template

```text
function solve(node):
    if node is None:
        return empty_tree_answer

    left = solve(node.left)
    right = solve(node.right)

    return combine(left, right, node.val)
```

## Dry Run Mental Model

For this tree:

```text
    1
   /   2   3
```

A postorder-style recursive function usually finishes nodes in this order:

```text
2 -> 3 -> 1
```

The parent cannot finish until both children have returned their answers.

## Base Case

The base case defines what an empty subtree contributes.

Common empty answers:

```text
height: 0
count: 0
validity check: True
search result: None
path exists: False
```

Do not memorize one base case for all tree problems. Match the base case to the return meaning.

## Complexity

Most basic recursive tree problems:

```text
Time: O(n)
Space: O(h)
```

`n` is the number of nodes. `h` is the height of the tree.

Balanced tree:

```text
h = O(log n)
```

Skewed tree:

```text
h = O(n)
```

## Pitfalls

- Calling recursion but ignoring the return value.
- Returning after checking only the current node.
- Forgetting that `None` is part of the recursive structure.
- Checking only direct children when the whole subtree matters.
- Recomputing subtree information when one helper can return it.

## Interview Checklist

Before coding, make sure you can answer:

```text
What single value should this node return to its parent?
What does an empty subtree (None) return, and why is that the correct base case?
How do I combine left_answer, right_answer, and node.val into the return value?
Can I state the return meaning in one sentence, e.g. "height(node) returns ..."?
Am I recomputing subtree info across multiple passes instead of returning it once?
```
