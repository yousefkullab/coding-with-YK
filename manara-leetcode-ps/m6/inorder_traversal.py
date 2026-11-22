# Understand 
# Input a root of binary tree
# Output inorder traversal of this tree

# Example 
# root = [1, null,2, 3]
# output = [1,3,2]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Use DFS inorder Traversal ( Binary tree )
# code
class Suoltion:
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return []
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

# Complexity Time O(n), Space O(h)
