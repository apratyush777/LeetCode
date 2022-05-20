# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=0
        temp_head=head
        while temp_head:
            cnt+=1
            temp_head=temp_head.next
        if k!=0 and cnt!=0:
            k=k%cnt
        if k==0 or cnt==0:
            return head
        else:
            
            
            old_head=head
            l=r=head
            for i in range(k):
                r=r.next
            while r.next:
                l=l.next
                r=r.next
            new_head=l.next
            l.next=None
            temp=new_head
            while temp.next:
                temp=temp.next
            temp.next=old_head
        
            return new_head