# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt=0
        self.ans=0
        
        def helper(root):
            if root:
                helper(root.left)
                self.cnt+=1
                if self.cnt==k:
                    self.ans=root.val
                    
                    #return root.val
                helper(root.right)
            return self.ans
                
        ans=helper(root)
        return ans
