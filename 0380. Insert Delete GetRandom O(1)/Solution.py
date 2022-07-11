import random
class RandomizedSet:
    ran_set = {}

    def __init__(self):
        self.ran_set = {}

    def insert(self, val: int) -> bool:
        if val in self.ran_set:
            return False
        else:
            self.ran_set[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.ran_set:
            self.ran_set.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.ran_set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()