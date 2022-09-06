# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans=None
        self.d={}
        def helper(root,d,ans):
            if root:
                if self.ans:
                    return
                helper(root.left,self.d,self.ans)
                if k-root.val in self.d:
                    self.ans=True
                    return
                else:
                    self.d[root.val]=1
                    
                helper(root.right,self.d,self.ans)
                
                
        helper(root,self.d,self.ans)
        return self.ans