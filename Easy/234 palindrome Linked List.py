# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        temp = None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        # 1 2     1 2 3             1 2 3 4 5
        if temp:
            temp.next = None

        prevnode = None
        curr = nextnode = slow
        while nextnode:
            nextnode = nextnode.next
            curr.next = prevnode
            prevnode = curr
            curr = nextnode
        head2 = prevnode

        i, j = head, head2
        while i:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
