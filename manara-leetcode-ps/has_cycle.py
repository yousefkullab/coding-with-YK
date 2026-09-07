class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Understand
#   Input head
#   Output True or False (hasCycle)
#   How to Know is it Cycle (we visit same node again)

# Example 
# 3 > 2 > 0 > 4 > None
# Not Cycle 

# Brute Force 
def hasCycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# Problem > We Store all node in set Time O(n), Space O(n) 

# Optimze use Floyd's Cycle Detection
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test & Complexity Time O(n), Space O(1)

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, head, data):
        if head == None:
            return
        if head.data == data:
            return head.next
        current = head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return head
            current = current.next
        return head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(0)
    linked_list.insert(-4)

    # Cycle Node
    cycle_node = linked_list.head.next
    last_node = linked_list.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = cycle_node

    # linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None

    print(hasCycle(linked_list.head)) # True

