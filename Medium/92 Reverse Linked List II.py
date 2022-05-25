# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = temp = ListNode(0, head)
        l = head
        for i in range(left-1):
            l = l.next
            temp = temp.next

        prevnode = None
        curr = nextnode = l
        for i in range(right-left+1):
            nextnode = nextnode.next
            curr.next = prevnode
            prevnode = curr
            curr = nextnode

        temp.next.next = curr
        temp.next = prevnode

        return dummy.next
