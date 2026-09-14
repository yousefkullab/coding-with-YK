class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Understand 
#   * Input > list1, list2 [linkedlist] 
#   * Output > sorted_list [linkedlist]
#   * Constraints sorted and range[0, 50] node
#   * edge case (if any list in none return other list)

# Middle Example 
# list1 = 1 > 2 > 4, list2 = 1 > 3 > 4
# output = 1 > 1 > 2 > 3 > 4 > 4

# Brute Force Time O((n+m) log(n+m)), Space O(n+m)
class Solution:
    def mergeTwoLists(self, list1, list2):
        values = []

        currnet = list1
        while currnet:
            values.append(currnet.val)
            currnet = currnet.next

        currnet = list2
        while currnet:
            values.append(currnet.val)
            currnet = currnet.next

        # Sort values
        values.sort()

        # bulid new linkedlist
        dummy = ListNode()
        tail = dummy

        for value in values:
            new_node = ListNode(value)
            tail.next = new_node
            tail = tail.next

        return dummy.next

# Problem > the list is sorted while we sorted again with values.sort()

# Optimze > use pointer ( dummy, tail)

# code
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2


        return dummy.next

# Test & Complexity Time O(n+m), Space O(1) 
if __name__ == '__main__':

    s = Solution()

    # list1 = 1 > 2 > 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # list2 = 1 > 3 > 4 
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # merage lists
    res = s.mergeTwoLists(list1, list2)

    # print res list
    currnet = res 
    while currnet:
        print(currnet.val, end=" > ")
        currnet = currnet.next

    print(None)
    