from typing import Optional, List
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = queue.Queue()
        # Need to show which nodes belong to the same level
        hmap = {}
        
        q.put([root, 0])
        
        while not q.empty():
            cur = q.get()
            if cur[1] in hmap:
                hmap[cur[1]].append(cur[0].val)
            else:
                hmap[cur[1]] = [cur[0].val]

            if cur[0].left:
                q.put([cur[0].left, cur[1]+1])
            if cur[0].right:
                q.put([cur[0].right, cur[1]+1])
                
        return list(hmap.values())