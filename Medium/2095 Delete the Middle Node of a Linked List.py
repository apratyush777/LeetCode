# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        s = f = head
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        prev.next = prev.next.next
        return head
