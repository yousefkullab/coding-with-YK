class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Understand 
#   Input > head of list 
#   Output > reorder this list 
#   Constarins  1 <= node.val <= 1000

# Middle Example 
# head = [1,2,3,4,5]
# reordered list = [1,5,2,4,3]

# Brute Force Solve. Time O(n), Spave O(n)
class Solution:
    def reorderList(self, head):
        if not head:
            return

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left = 0
        right = len(nodes)-1

        while left < right:

            nodes[left].next = nodes[right]
            left +=1

            if left == right: break

            nodes[right].next = nodes[left]
            right -=1

        nodes[left].next = None

# Problem > Use extera Array

# Optimze > use slow/fast Pointers

# code
# class Solution:
    # def reorderList(self, head):
    #     pass

# Test & Complexity Time O(n), Space O(1)
if __name__ == '__main__':
    testList = ListNode(1)
    testList.next = ListNode(2)
    testList.next.next = ListNode(3)
    testList.next.next.next = ListNode(4)

    # print list 
    current = testList
    while current:
        print(current.val, end=" > ")
        current = current.next
    print(None)

    s = Solution()
    head = testList
    ordered_list = s.reorderList(head)

    # print orderd-list 
    current = testList
    while current:
        print(current.val, end=" > ")
        current = current.next
    print(None)

      