# Understand 
# Input root of BT
# return the kth smallest element 

# Example 
# Input root = [5,3,6,2,4,null,null,1], k = 3
# return 3

# Use DFS Inorder Traversal due to the elements ordered Accending

# code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        arr = []
        def dfs(node):
            if node is None:
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k-1]
# Complexity Time O(n), Space O(h)

# Other Soultion
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        res = None
        count = 0
        # inorder traversal to order elements in accending order
        def dfs(node):
            nonlocal count, res
            if node is None:
                return 
            dfs(node.left) 
            if res is not None:
                return    
            count += 1 
            if count == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
# Complexity Time O(h+k), Space O(h)
