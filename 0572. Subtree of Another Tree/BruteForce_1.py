from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the subTree is empty
        if not subRoot:
            return True
        # If the subTree is not empty, but the tree is empty => False
        if not root:
            return False
        
        # For each node, check if subRoot is the same as node
        if self.sameTree(root, subRoot):
            return True
        
        # Check if left/right subtree of tree is subTree => logically confusing
        if self.isSubtree(root.left, subRoot):
            return True
        elif self.isSubtree(root.right, subRoot):
            return True
        else:
            return False
        
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val == root2.val:
            if self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right):
                return True

        return False