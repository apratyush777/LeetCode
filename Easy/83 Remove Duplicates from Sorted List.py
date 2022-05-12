#1st method. kinda what I thought and wanted to do


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
    
    
    
    #2nd method neetcode
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp:
            while temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
                
            temp=temp.next
        return head
