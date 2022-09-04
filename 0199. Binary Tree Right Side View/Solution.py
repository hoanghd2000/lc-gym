from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Each element of the queue stores in this format [node, the node's level in the tree]
        q = [[root, 0]]
        
        # Storing the tree by levels, key:value = level:[node vals on that level]
        levels = {}
        
        while q:
            node = q.pop(0)
            self.addD(levels, node)
            
            if node[0].left:
                q.append([node[0].left, node[1]+1])
            if node[0].right:
                q.append([node[0].right, node[1]+1])
        
        levels = levels.values()
        res = []
        for level in levels:
            res.append(level[-1])
        return res
    
    def addD(self, levels, ele):
        if ele[1] in levels:
            levels[ele[1]].append(ele[0].val)
        else:
            levels[ele[1]] = [ele[0].val]