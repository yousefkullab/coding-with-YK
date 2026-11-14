# Understand 
# INPUT root of binary tree
# Output sum of left leaves

# Example
# root = [3,9,20,null,null,15,7]
# return 24

# DAS is Tree and use BFS to traversal level by level 

# The node must be left of Parent and has no child
# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        queue = deque([root])
        total = 0

        if root is None:
            return 0
        
        while queue:
            node = queue.popleft()
            if node.left is not None and node.left.left is None and node.left.right is None: 
                total += node.left.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return total