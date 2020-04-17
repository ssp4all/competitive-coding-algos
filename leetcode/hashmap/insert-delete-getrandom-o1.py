https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ip, self.cache = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.cache:
            return 0
        self.ip += [val]
        self.cache[val] = len(self.ip) - 1
        return 1
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.cache:
            return 0
    
        loc, last = self.cache[val], self.ip[-1]
        self.ip[loc] = last
        self.cache[last] = loc
        del self.cache[val]
        self.ip.pop()
        return 1

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """ 
        return self.ip[randint(0, len(self.ip) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()