# Types of Tree
#   - General tree
#   - Binary tree
#   - Binary Search tree
#   - AVL tree
#   - Red Black tree
#   - N-ary tree

# Traversal ( DFS, BFS )

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val): # O(logn)
    if root == None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    return root


def search(root, target): # O(logn)
    if root is None:
        return False
    if root.val ==target:
        return True
    if target < root.val:
        return search(root.left, target)
    return search(root.rgiht, target)

def inorder(root): # O(n)
    if root is None:
        return 
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def checkBST(root): # Range Check O(n)
    def validate(node, min_val, max_val):
        if node is None:
            return True
        if node.val < min_val or node.val > max_val:
            return False
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    return validate(root, float("-inf"), float("inf"))

root = None

for val in [10,5,15,3,7]:
    root = insert(root,val) 

print("InOrder Traversing: ")
inorder(root)

print("\nSearch 10 is in tree: ", search(root, 10))
print("Search 2 is in tree: ", search(root, 2))

print("Is this tree is BST: ", checkBST(root))

