from tree_node import TreeNode

def path_sum(root: TreeNode | None, target_sum: int) -> bool:
    # Problem 13: Path Sum
    # Key idea: carry the remaining sum from root to leaf.
    # Time:
    # Space:
    
    if not root:
        return False
    
    if not root.left and not root.right:
        return True if root.val == target_sum else False
    
    return path_sum(root.left, target_sum - root.val) or path_sum(root.right, target_sum - root.val)
    
def path_sum_ii(root: TreeNode | None, target_sum: int) -> list[list[int]]:
    # Problem 14: Path Sum II
    # Key idea: backtrack with a current root-to-leaf path.
    # Time:
    # Space:
    
    if not root:
        return []
    
    result = []
    path = []
    
    def path_sum_ii_helper(node, remaining_sum):
        if node is None:
            return
        
        path.append(node.val)
        
        if not node.left and not node.right and node.val == remaining_sum:
            result.append(path[:])
            
        path_sum_ii_helper(node.left, remaining_sum - node.val)
        path_sum_ii_helper(node.right, remaining_sum - node.val)
        
        path.pop()
    
    path_sum_ii_helper(root, target_sum)
    return result
            
def binary_tree_paths(root: TreeNode | None) -> list[str]:
    # Problem 15: Binary Tree Paths
    # Key idea: build every root-to-leaf path.
    # Time:
    # Space:
    
    if not root:
        return []
    
    res = []
    
    def binary_tree_paths_helper(node, path):
        if not node:
            return    
        
        if not node.left and not node.right:
            res.append(path)
        
        if node.left:
            binary_tree_paths_helper(node.left, f"{path}->{node.left.val}")
        if node.right:
            binary_tree_paths_helper(node.right, f"{path}->{node.right.val}")
    
    binary_tree_paths_helper(root, f"{root.val}")
    return res

def sum_root_to_leaf_numbers(root: TreeNode | None) -> int:
    # Problem 16: Sum Root To Leaf Numbers
    # Key idea: carry the current number down the tree.
    # Time:
    # Space:
    
    if not root:
        return 0
    
    nums = []
    
    def helper(node: TreeNode | None, path):
        if not node:
            return 0
        
        if not node.left and not node.right:
            nums.append(int(path))
            
        if node.left:
            helper(node.left, f"{path}{node.left.val}")
        if node.right:
            helper(node.right, f"{path}{node.right.val}")
    
    helper(root, f"{root.val}")
    return sum(nums)
