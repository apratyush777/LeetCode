# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next

        K = l-k
        curr1, curr2 = head, head
        for i in range(k-1):
            curr1 = curr1.next
        for i in range(K):
            curr2 = curr2.next

        curr1.val, curr2.val = curr2.val, curr1.val
        return head
