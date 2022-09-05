# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum=0
        def helper(root):
            if root:
                helper(root.left)
                if root.val>=low and root.val<=high:
                    self.sum+=root.val
                helper(root.right)
                
            
        helper(root)
        return self.sum