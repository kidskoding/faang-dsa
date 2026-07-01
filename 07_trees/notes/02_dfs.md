# Tree DFS

## Pattern

DFS explores one branch as far as possible before moving to the next branch.

For trees, DFS is usually recursive because every child is another tree.

The three DFS orders are:

```text
preorder:  node -> left -> right
inorder:   left -> node -> right
postorder: left -> right -> node
```

## Intuition

Choose the traversal order based on when the current node should be processed.

Use preorder when information flows from parent to child.

```text
current node affects descendants
```

Use postorder when information flows from children to parent.

```text
children report back to current node
```

Use inorder when BST sorted order matters.

```text
left values -> current value -> right values
```

## How It Works

DFS helpers usually have one of two jobs.

Top-down DFS carries state downward:

```text
helper(node, running_sum)
helper(node, max_so_far)
helper(node, current_path)
helper(node, low_bound, high_bound)
```

Bottom-up DFS returns information upward:

```text
height(node) -> int
is_balanced(node) -> bool
lca(node) -> TreeNode | None
```

Before coding, decide whether the problem is top-down or bottom-up.

## Template: Top-Down DFS

```text
function dfs(node, state):
    if node is None:
        return

    update state using node
    dfs(node.left, state)
    dfs(node.right, state)
```

Use this when ancestor information matters.

## Template: Bottom-Up DFS

```text
function dfs(node):
    if node is None:
        return empty_answer

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(left, right, node)
```

Use this when the parent needs information from children.

## Backtracking Template

When the state is mutable, restore it after recursion:

```text
path.append(node.val)

dfs(node.left, path)
dfs(node.right, path)

path.pop()
```

The `pop` prevents one branch from leaking into a sibling branch.

## Complexity

Most DFS tree problems:

```text
Time: O(n)
Space: O(h)
```

If you copy paths into a result list, add the output cost.

## Pitfalls

- Using preorder when the problem needs child information first.
- Forgetting to return the recursive answer.
- Mutating a shared path without undoing it.
- Mixing up node count and edge count.
- Treating every DFS problem as the same helper shape.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is this problem top-down (state passed into children) or bottom-up (state returned from children)?
Which traversal order — preorder, inorder, or postorder — matches when I need to process the node?
If I'm carrying mutable state (like a path list), where exactly does the pop/undo happen?
What does the base case return, and does it differ for top-down vs bottom-up helpers?
Am I forgetting to use the recursive return value on the way back up?
```
