# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            h1 = temp1 = head
            h2 = temp2 = head.next
            while temp1.next and temp2.next:
                temp1.next = temp1.next.next
                temp2.next = temp2.next.next
                temp1 = temp1.next
                temp2 = temp2.next
            temp1.next = None

            temp1, temp2 = h1, h2
            prev = None
            while temp1 and temp2:
                nx1, nx2 = temp1.next, temp2.next
                temp2.next = temp1
                temp1.next = nx2
                temp2 = nx2
                prev = temp1
                temp1 = nx1
            # print(temp1.val)
            if temp1:
                prev.next = nx1
            return h2
