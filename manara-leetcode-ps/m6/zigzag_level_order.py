# Understand 
# Input root of binary tree
# Output list of node in every level with zigzag direction

# Example 
# root = [3,9,20,null,null,15,7]
# output [[3],[20,9],[15,7]]

# Use DSA Binary Tree with BFS used queue
# code
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        else:
            queue = deque([root])
            res = []
            left_to_right = True

            while queue:
                level = []
                level_size = len(queue)
                for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if not left_to_right:
                    level.reverse()  
                res.append(level)
                left_to_right = not left_to_right
            return res

# Complexity Time O(n), Space O(n)
