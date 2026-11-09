# Understand 
# Input root of binary tree
# Output root of the Invert this tree

# Example 
# root = [4,2,7,1,3,6,9]
# return [4,7,2,9,6,3,1]

# Use Binary tree with DFS algo used Recursion for traversl of tree
# code 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return None
        # Swap childrens
        root.left, root.right = root.right, root.left
        # Depth all tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Complexity Time O(n), Space O(h)


