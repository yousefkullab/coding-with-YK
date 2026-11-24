class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Stack: 
    def __init__(self):
        self.top = None
        self.size = 0

# Stack can Be ( Array/List, Linkedlist ) 
# DFS > Stack > LIFO

# push(), pop(), peek(), isEmpty(), size
# Complexity Time O(1), Space O(n)

# Used 
#   - Undo / Redo.
#   - Browser History.
#   - DFS in Graphs, Trees.
#   - Parentheses Validation.
#   - Function Call Stack.
#   - Backtacking
#   - Expression Evalution

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size +=1

    def pop(self):
        if self.size == 0:
            return None
        pop_elm = self.top
        self.top = self.top.next
        self.size -= 1
        return pop_elm.val

    def peek(self):
        if self.size == 0:
            return None
        return self.top.val

    def isEmpty(self):
        return self.size == 0

if __name__ == '__main__':
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)

    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.size)
    print(s.isEmpty())

print("$" * 50)

# Stack in PY 
stack = []

stack.append(10) # append
stack.append(50)
stack.append(90)

print(stack[-1]) # peek
print(stack.pop()) # pop
print(len(stack) == 0) # check size
print(len(stack)) # size


