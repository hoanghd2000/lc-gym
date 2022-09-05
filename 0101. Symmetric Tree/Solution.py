from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        trav1 = self.preorderTrav1(root)
        trav2 = self.preorderTrav2(root)
        
        if trav1 == trav2:
            return True
        else:
            return False
    
    def preorderTrav1(self, root):
        # Base Case
        if not root:
            return [None]
        
        # Recursive Case
        return [root.val] + self.preorderTrav1(root.left) + self.preorderTrav1(root.right)

    def preorderTrav2(self, root):
        # Base Case
        if not root:
            return [None]
        
        # Recursive Case
        return [root.val] + self.preorderTrav2(root.right) + self.preorderTrav2(root.left)