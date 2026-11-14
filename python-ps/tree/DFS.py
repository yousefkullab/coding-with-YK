# DFS — Depth First Search ( Go Deep First )
# Apply with Stack/Recursion 
# Used Path Sum, Tree Depth
# Time O(n)
# Space O(h), h: lenght of tree

# def dfs(root):
#     if root is None:
#         return

#     print(root.val)

#     dfs(root.left)
#     dfs(root.right)

def dfs(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)