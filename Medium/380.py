# insert delete getrandom O(1)

import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.data)
        self.data.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val]
        last_val = self.data[-1]
        
        self.data[index] = last_val
        self.indices[last_val] = index

        self.data.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data) 
