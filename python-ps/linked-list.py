# Array good at access elements 
# Linked List good at instert and delete elements, But used more Memery

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None
    linked_list.delete(linked_list.head, 2)
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None
