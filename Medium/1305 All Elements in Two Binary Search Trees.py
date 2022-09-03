# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1=[]
        s2=[]
        res=[]
        while len(s1)>0 or len(s2)>0 or root1!=None or root2!=None:
            while root1:
                s1.append(root1)
                root1=root1.left
            while root2:
                s2.append(root2)
                root2=root2.left
            if len(s2)==0 or (len(s1)>0 and s1[-1].val<=s2[-1].val):
                root1=s1.pop()
                res.append(root1.val)
                root1=root1.right
            else:
                root2=s2.pop()
                res.append(root2.val)
                root2=root2.right 
                
        return res