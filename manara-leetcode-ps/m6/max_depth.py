class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

# Understand 
# Input root of BT
# Output return the maximum depth

# Example 
# root = [3,9,20,null,null,15,7]
# return 3

# Brute Force
# we can search all paths from the root to nodes then choose long path

# Problem > it is cost time and momery 
# Optimize > recursion

# code
class Solution:
    def maxDepth(self, root :TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1+ max(left_depth, right_depth)

# Test & Compixicty, Time O(n), Space O(h)
