# Understand 
# Input a root of binary tree
# Output postorder traversal of this tree

# Example 
# root = [1, null,2, 3]
# output = [1,3,2]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Use DFS postorder Traversal ( Binary tree )
# code
class Suoltion:
    def postorderTraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return []
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

# Complexity Time O(n), Space O(h)
