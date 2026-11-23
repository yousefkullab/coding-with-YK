# Understand 
# Input root of binary tree
# Output return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 
# root = [4,2,6,1,3]
# return 1

# Use Dfs with Recursion

# code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        previous = None
        min_diff = float("inf")

        def dfs(node):
            nonlocal previous, min_diff
            if node is None:
                return 
            # visit left node
            dfs(node.left)
            # cal diff
            if previous is not None:
                min_diff = min(min_diff, node.val - previous.val)
            # update previous
            previous = node
            # visit right node
            dfs(node.right)
        dfs(root)
        return min_diff

# Complexity Time O(n), Space O(h)