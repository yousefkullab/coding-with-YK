from collections import deque

# Understand 
# In a complete binary tree, every level, except possibly the last,
#  is completely filled, and all nodes in the last level
#  are as far left as possible.
#  It can have between 1 and 2h nodes inclusive at the last level h.
# Input root of tree
# Output return if the tree is compelete tree or not 

# Example 
# root = [1,2,3,4,5,6]
# return true

# Use BFS to check level level in tree
# code 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        # empty tree is considered completed
        if root is None:
            return True
        # use queue to traversal tree level by level 
        queue = deque([root])
        # Tracks None node 
        found_gap = False
        while queue:
            node = queue.popleft()

            if node is None:
                found_gap = True
            else:
                if found_gap:
                    return False
            queue.append(node.left)
            queue.append(node.right)
        return True
# Complexity Time O(n), Space O(n)
