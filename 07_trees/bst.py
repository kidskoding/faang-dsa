from turtle import left
from tree_node import TreeNode
from collections import deque

def search(root: TreeNode | None, target: int) -> TreeNode | None:
    # Return the node whose value equals target, or None if it is missing.
    #
    # BST idea:
    # - if target is smaller than node.val, search left
    # - if target is larger than node.val, search right
    # - if equal, return the current node
    #
    # Time:
    # Space:
    
    if root is None:
        return None
        
    if target < root.val:
        return search(root.left, target)
    if target > root.val:
        return search(root.right, target)
    
    return root

def contains(root: TreeNode | None, target: int) -> bool:
    # Return True if target exists in the BST.
    #
    # This can use search(root, target), or you can write the traversal directly.
    #
    # Time:
    # Space:
    
    if not root:
        return False
    if target == root.val:
        return True
    
    return contains(root.left, target) if target < root.val else contains(root.right, target)

def insert(root: TreeNode | None, val: int) -> TreeNode:
    # Insert val into the BST and return the root.
    #
    # BST idea:
    # - smaller values go left
    # - larger values go right
    # - decide how this file should handle duplicates before implementing
    #
    # Time:
    # Space:
    
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    if val < root.val:
        root.left = insert(root.left, val)
        
    return root
    
def min_value_node(root: TreeNode | None) -> TreeNode | None:
    # Return the node with the smallest value.
    #
    # BST idea:
    # - the smallest value is found by walking left until you cannot go left
    #
    # Time:
    # Space:
    
    if not root:
        return None
    
    if not root.left:
        return root
 
    return min_value_node(root.left)

def max_value_node(root: TreeNode | None) -> TreeNode | None:
    # Return the node with the largest value.
    #
    # BST idea:
    # - the largest value is found by walking right until you cannot go right
    #
    # Time:
    # Space:
    
    if not root:
        return None
    
    if not root.right:
        return root
 
    return min_value_node(root.right)

def inorder_values(root: TreeNode | None) -> list[int]:
    # Return BST values in sorted order.
    #
    # BST idea:
    # - inorder traversal of a BST visits values in ascending order
    #
    # Time:
    # Space:
    
    if not root:
        return []
    
    res = []
    
    res.extend(inorder_values(root.left))
    res.append(root.val)
    res.extend(inorder_values(root.right))
    
    return res

def is_valid_bst(root: TreeNode | None) -> bool:
    # Return True if the entire tree satisfies the BST invariant.
    #
    # Important:
    # - checking only node.left.val < node.val < node.right.val is not enough
    # - every node must respect lower and upper bounds from its ancestors
    #
    # Time:
    # Space:
    
    def is_valid_bst_helper(node: TreeNode | None, low, high) -> bool:
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        left_valid = is_valid_bst_helper(node.left, low, node.val)
        right_valid = is_valid_bst_helper(node.right, node.val, high)
        
        return left_valid and right_valid
    
    return is_valid_bst_helper(root, float('-inf'), float('inf'))

def delete(root: TreeNode | None, val: int) -> TreeNode | None:
    # Delete val from the BST and return the new root.
    #
    # Cases:
    # - value is not found
    # - node is a leaf
    # - node has one child
    # - node has two children
    #
    # Time:
    # Space:
    
    if root is None:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left and root.right:
            successor = min_value_node(root.right)
            root.val = successor.val
            root.right = delete(root.right, successor.val)
        elif root.left:
            return root.left 
        else:
            return root.right

    return root
