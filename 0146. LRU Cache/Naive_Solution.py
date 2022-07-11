class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            for k in self.cache:
                self.lru[k] += 1
            self.lru[key] = 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            for k in self.cache:
                self.lru[k] += 1
            self.cache[key] = value
            self.lru[key] = 1
        else:
            if len(self.cache) >= self.capacity:
                lru_key = list(self.cache.keys())[0]
                for k in self.cache:
                    if self.lru[lru_key] < self.lru[k]:
                        lru_key = k
                self.cache.pop(lru_key)
                self.lru.pop(lru_key)
            for k in self.cache:
                self.lru[k] += 1
            self.cache[key] = value
            self.lru[key] = 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)