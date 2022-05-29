# O(m+n) and time O(1) solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        temp1, temp2 = head1, head2
        l1, l2 = 0, 0
        while temp1:
            l1 += 1
            temp1 = temp1.next
        while temp2:
            l2 += 1
            temp2 = temp2.next
        if l1 <= l2:
            temp2 = head2
            minus = l2-l1
            for i in range(minus):
                temp2 = temp2.next
            temp1 = head1
            while temp1:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        else:
            temp1 = head1
            minus = l1-l2
            for i in range(minus):
                temp1 = temp1.next
            temp2 = head2
            while temp1:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next

        return None

# O(m+n) and time O(1) solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        temp = head1
        d = {None: None}
        while temp:
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1
            temp = temp.next

        temp = head2
        while temp:
            if temp in d:
                return temp
            else:
                temp = temp.next

        return None
