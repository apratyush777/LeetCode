import random
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        temp = self.head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        rand = math.floor(random.random()*10000)
        rand = rand % cnt
        temp = self.head
        for i in range(rand):
            temp = temp.next

        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
