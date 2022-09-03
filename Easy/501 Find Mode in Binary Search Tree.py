# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(root,arr,vararr):
    if root:
        helper(root.left,arr,vararr)
        
        if root.val==vararr[0]:
            vararr[2]+=1
        else:
            vararr[2]=1
            
        if vararr[2]>vararr[1]:
            vararr[1]=vararr[2]
            arr.clear()
            arr.append(root.val)
        elif vararr[2]==vararr[1]:
            arr.append(root.val)
        vararr[0]=root.val
        helper(root.right,arr,vararr)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #vararr=[prev,maxx,cnt]
        vararr=[99999999,0,0]
        
        arr=[]
        helper(root,arr,vararr)
        
        return arr