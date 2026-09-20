class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,node):
        new_node = Node(node)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return -1
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            return -1
        return self.top.data

    def is_empty(self):
        return self.top is None

if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(12)
    stack.push(14)
    stack.push(16)
    stack.push(18)

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())

# Complexity Time O(1) push, pop, peek, is_empty due to you deal with top
# Space O(n)


# Used OF Stack
#   * Fundctions Call stack
#   * Undo/Redo
#   * Browser History
#   * DFS
#   * Valid Parentheses
#   * Backtacking
#   * Expression Evalution

# Stack can Be ( Array/List, Linkedlist ) 
# DFS > Stack > LIFO
