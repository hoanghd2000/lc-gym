from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)
        if l:
            if r:
                return list(l + [root.val] + r)
            else:
                return list(l + [root.val])
        else:
            if r:
                return list([root.val] + r)
            else:
                return [root.val]