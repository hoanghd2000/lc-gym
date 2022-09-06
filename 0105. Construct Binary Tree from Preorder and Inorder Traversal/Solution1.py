from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base Case
        
        ## 0 element in tree
        if len(preorder) == 0:
            return None

        ## 1 element in tree
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        # Recursive Case
        root = preorder[0]
        root_pos_in = inorder.index(root)
        right_child_pos_pre = root_pos_in + 1
        return TreeNode(root, self.buildTree(preorder[1:right_child_pos_pre], inorder[:root_pos_in]), self.buildTree(preorder[right_child_pos_pre:], inorder[root_pos_in+1:]))