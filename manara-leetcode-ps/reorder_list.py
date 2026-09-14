# Understand 
#    Input head
#    Output None (only reorder list)

# Example 
# head = [1,2,3,4]
# Output = [1,4,2,3]

# Brute Force
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        currnet = head.next 
        while currnet.next:
            head


        