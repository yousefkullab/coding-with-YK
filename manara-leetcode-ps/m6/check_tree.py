# Undrstand 
# INPUT root of binary tree have only tree node
# OUTPUT check of sum (left, right) child is equal root

# Example
# root = [10,4,6]
# true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return 
        return (root.left.val+ root.right.val) == root.val
    
# Complexity Time O(1), Space O(1)