# Tree Serialization

## Pattern

Serialization converts a tree into a sequence. Deserialization rebuilds the same tree from that sequence.

The sequence must preserve structure, not just values.

## Intuition

Values alone are not enough.

These trees have the same values but different shapes:

```text
1        1
 \      /
  2    2
```

Without null markers, both could serialize as `1,2`.

Null markers preserve missing children.

## DFS Preorder Serialization

Preorder is the most common interview-friendly approach.

```text
node, left, right
```

Template:

```text
function serialize(node):
    if node is None:
        write null marker
        return

    write node.val
    serialize(node.left)
    serialize(node.right)
```

## DFS Preorder Deserialization

Deserialization must consume tokens in the same order.

```text
function deserialize():
    token = next token

    if token is null marker:
        return None

    node = TreeNode(token)
    node.left = deserialize()
    node.right = deserialize()
    return node
```

The recursive calls rebuild exactly the structure that serialization wrote.

## BFS Serialization

BFS serialization matches level-order array style.

It uses a queue and writes null markers for missing children.

This is useful for LeetCode-style helpers, but DFS preorder is often simpler to implement under interview pressure.

## Complexity

```text
Time: O(n)
Space: O(n)
```

The encoded output stores every real node plus enough null markers to recover shape.

## Pitfalls

- Serializing values without null markers.
- Deserializing in a different order from serialization.
- Losing track of the current token index.
- Stripping null markers that are needed for internal missing children.
- Mixing BFS format and DFS format.

## Interview Checklist

Before coding, make sure you can answer:

```text
Why aren't values alone enough to reconstruct the tree — what do null markers preserve?
Does deserialize() consume tokens in the exact same order serialize() wrote them?
Am I tracking a single shared token index/iterator across recursive deserialize calls?
Is this DFS preorder (node, then children) or BFS level-order, and am I consistent between serialize/deserialize?
Why is space O(n) even though I'm writing null markers for missing children?
```
