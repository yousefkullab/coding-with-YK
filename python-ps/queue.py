class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if  self.isEmpty():
            new_node = Node(node)
            self.front = new_node
            self.rear = new_node
        else:
            new_node = Node(node)
            self.rear.next = new_node
            self.rear = new_node
        

    def dequeue(self):
        if self.isEmpty():
            return -1
        
        data = self.front.data
        self.front = self.front.next 

        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.isEmpty():
            return -1
        return self.front.data

    def isEmpty(self):
        return self.front is None


if __name__ == '__main__':
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.peek())

# Time Complixty O(1) enqueue(), dequeue(), peek(), isEmpty() due to to enqueue in the rear and dequeue in the front only one step
# Space O(n)

# Used OF Queue
#   * BFS
#   * Task/Job Processing
#   * Print Queue
#   * Request/Server Queuing
#   * Producer/Consumer
#   * Backtacking
#   * Expression Evalution

# Queue can Be ( Simple, Circulur, Priority, Deque ) 
# BFS > Queue > FIFO

    