# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans=None
        def inorder(cloned):
            if cloned:
                inorder(cloned.left)
                if cloned.val==target.val:
                    self.ans=cloned
                    
                inorder(cloned.right)
                
            
        inorder(cloned)
        return self.ans