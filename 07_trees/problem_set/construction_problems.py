from tree_node import TreeNode

def construct_from_preorder_inorder(
    preorder: list[int],
    inorder: list[int],
) -> TreeNode | None:
    # Problem 26: Construct Binary Tree From Preorder And Inorder Traversal
    # Key idea: preorder gives the root; inorder splits left and right subtrees.
    # Time:
    # Space:
    raise NotImplementedError

def construct_from_inorder_postorder(
    inorder: list[int],
    postorder: list[int],
) -> TreeNode | None:
    # Problem 27: Construct Binary Tree From Inorder And Postorder Traversal
    # Key idea: postorder gives the root; inorder splits left and right subtrees.
    # Time:
    # Space:
    raise NotImplementedError

def serialize_binary_tree(root: TreeNode | None) -> str:
    # Problem 28: Serialize And Deserialize Binary Tree
    # Key idea: turn the tree into a sequence that preserves shape.
    # Time:
    # Space:
    raise NotImplementedError

def deserialize_binary_tree(data: str) -> TreeNode | None:
    # Problem 28: Serialize And Deserialize Binary Tree
    # Key idea: rebuild the tree from the serialized sequence.
    # Time:
    # Space:
    raise NotImplementedError
