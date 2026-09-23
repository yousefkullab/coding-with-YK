from heapq import heapify, heappush, heappop
# heapq is used to apply Min heap we can use negative to apply Max heap

heap = []
heapify(heap) 

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("Head value of heap : "+str(heap[0]))

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")

element = heappop(heap)

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')

# Applications of Heap

# 1.Priority Queue 
# 2.Heapsort
# 3.Graph algorithm (Prim's, Dijkstra's, and A* search)
# 4.Resource allocation
# 5.Job scheduling ...

# from queue import PriorityQueue 
# q = PriorityQueue() 

# q.put(10)
# q.put(20) 
# q.put(5) 

# print(q.get()) 
# print(q.get()) 

# print('Items in queue :', q.qsize()) 
# print('Is queue empty :', q.empty()) 
# print('Is queue full :', q.full())
