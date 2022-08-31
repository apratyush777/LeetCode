# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,arr):
    if root:
        helper(root.left,arr)
        arr.append(root.val)
        helper(root.right,arr)
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr=[]
        helper(root,arr)
        arr=list(set(arr))
        arr.sort()
        if len(arr)<2:
            return -1
        elif len(arr)==2:
            return max(arr[0],arr[1])
        else:
            return arr[1]