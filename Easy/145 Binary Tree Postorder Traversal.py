# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,arr):
    if root:
        helper(root.left,arr)
        helper(root.right,arr)
        arr.append(root.val)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        helper(root,arr)
        return arr