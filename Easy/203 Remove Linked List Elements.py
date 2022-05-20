# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=tail=ListNode(0,head)
        while tail.next:
            if tail.next.val==val:
                tail.next=tail.next.next
            else:
                tail=tail.next
        return dummy.next