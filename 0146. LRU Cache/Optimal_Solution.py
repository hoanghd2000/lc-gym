class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked_list and hashmap
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        del self.cache[node.key]
    
    # Insert a node to the right of the linked_list and into the hashmap
    def insert(self, key, value):
        prev, nxt = self.right.prev, self.right
        node = Node(key, value)
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        self.cache[key] = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].value
            self.remove(self.cache[key])
            self.insert(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the old node
            self.remove(self.cache[key])
            # insert it as the MRU node
            self.insert(key, value)
        else:
            if len(self.cache) >= self.capacity:
                self.remove(self.left.next)
            # insert the new node as the MRU node
            self.insert(key, value)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)