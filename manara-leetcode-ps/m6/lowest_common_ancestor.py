# Understand 
# Input root of BT and p, q nodes
# Output LCA of p and q

# Example 
# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# output = 3

# Use DFS with Recursion
# code
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            if node == q or node == p:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left is not None and right is not None:
                return node
            return left if left else right 
        return dfs(root)


# Complexity Time O(n), Space O(h)

