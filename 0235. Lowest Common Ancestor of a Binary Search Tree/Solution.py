# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Find all ancestors of a node, in sequence
        ancestors_p = self.traverse(root, p)
        ancestors_q = self.traverse(root, q)
        
        # Find the LCA by traversing the list of ancestors backwards
        for anp in ancestors_p:
            for anq in ancestors_q:
                if anp.val == anq.val:
                    return anp
        
    def traverse(self, root, target):
        # Base Case
        if root.val == target.val:
            return [root]
        
        # Recursive Case
        elif target.val < root.val:
            return self.traverse(root.left, target) + [root]
        else:
            return self.traverse(root.right, target) + [root]