# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return None
        else:
            s = f = head
            while f and f.next:
                s = s.next
                f = f.next.next
                if s == f:
                    break
            if s == f:
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                if s == f:
                    return f
                return None
            else:
                return None
