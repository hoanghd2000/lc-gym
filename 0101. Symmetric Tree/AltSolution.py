from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, root0, root1):
        if root0 and root1:
            return root0.val == root1.val and self.isMirror(root0.left, root1.right) and self.isMirror(root0.right, root1.left)
        if root0 == root1 == None:
            return root0 == root1 == None