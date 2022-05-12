# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=j=head
        while j:
            if i.val!=j.val:
                i.next=j
                i=i.next
            else:
                j = j.next
        if head!=None: 
            
            i.next=None
        return head