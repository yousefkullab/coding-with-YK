# Understand 
# INPUT root of binary tree, targetsum
# OUTPUT return if the tree has a root-to-leaf path sum values = targetsum

# Example 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Ture

# Use DFS to traversal on tree and sum the value 

# code 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None: 
            return False
        if root.left is None and root.rgiht is None:
            return targetSum == root.val

        return (
            self.hasPathSum(root.left, targetSum-root.val)
            or
            self.hasPathSum(root.right, targetSum-root.val)
        )            

# Complixety Time O(n), Space O(h)