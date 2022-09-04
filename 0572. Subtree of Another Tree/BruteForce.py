from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the tree is empty
        if not root:
            if not subRoot:
                return True
            else:
                return False
        
        # If the tree is not empty, but the subroot is empty => problematic
        if root:
            if not subRoot:
                return False
        
        # If the root.val == subRoot.val, check if left/right subtree of tree is the same as left/right subtree of subTree
        if root.val == subRoot.val:
            l = self.sameTree(root.left, subRoot.left)
            r = self.sameTree(root.right, subRoot.right)
            if l and r:
                return True
        
        # Check if left/right subtree of tree is subTree => logically confusing
        if self.isSubtree(root.left, subRoot):
            return True
        elif self.isSubtree(root.right, subRoot):
            return True
        else:
            return False
        
    def sameTree(self, root1, root2):
        if not root1:
            if not root2:
                return True
            else:
                return False
        
        if not root2:
            return False
        
        if root1.val != root2.val:
            return False
        if self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right):
            return True
        else:
            return False
            