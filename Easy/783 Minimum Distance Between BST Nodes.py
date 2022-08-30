# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev=9999999
        self.minn=9999999
        def helper(root):
            if root:
                helper(root.left)
                
                self.minn=min(self.minn,abs(root.val-self.prev))
                self.prev=root.val
                
                helper(root.right)
                
        helper(root)
        return self.minn
                