# BFS — Breadth First Search ( Level By Level )
# Apply with Queue
# Used Level Order, Shortest Path in Unweighted Graph
# Time O(n)
# Space O(w), w: most num of node on one level

from collections import deque

def bfs(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)