# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return
        s = f = head
        prev = None
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        prev.next = None

        prevnode = None
        curr = nextnode = s
        while nextnode:
            nextnode = nextnode.next
            curr.next = prevnode
            prevnode = curr
            curr = nextnode
        head2 = prevnode

        head1 = head
        while head1:
            temp1, temp2 = head1.next, head2.next
            prev = head2
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2

        if head2:
            prev.next = head2
