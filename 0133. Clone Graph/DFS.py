import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # If graph has 0 node
        if not node:
            return None
        
        # If graph has 1 node
        if len(node.neighbors) == 0:
            return Node(node.val, [])
        
        # If graph has 2 and more nodes
        ## For the new graph
        node_dict = {}
        
        ## For the old graph
        visited = set()
        q = collections.deque()
        
        ## Initialization, (new parent node, old cur_node)
        q.append((None, node))
        
        while q:
            cur = q.pop()
            newNode = None
            
            if cur[1].val not in visited:
                visited.add(cur[1].val)
                newNode = Node(cur[1].val, [])
                node_dict[cur[1].val] = newNode
                for neigh in cur[1].neighbors:
                    q.append((newNode, neigh))
            else:
                newNode = node_dict[cur[1].val]
            
            if cur[0]:
                cur[0].neighbors.append(newNode)
        
        return node_dict[1]