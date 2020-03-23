https://leetcode.com/problems/design-hashmap/

class Pool:
    def __init__(self):
        self.pool = []
        
    def get(self, key):
        for i, kv in enumerate(self.pool):
            if kv[0] == key:    
                return self.pool[i][1]
        return -1
    
    def update(self, key, val):
        for i, kv in enumerate(self.pool):
            if kv[0] == key:
                self.pool[i] = (key, val)
                return
        self.pool.append((key, val))
    
    def remove(self, key):
        for i, kv in enumerate(self.pool):
            if kv[0] == key:
                del self.pool[i]
                return 
        return -1
        
class MyHashMap:    

    def __init__(self):
        """
        Initialize your data structure here.
        """
         self.hash_key = 2069
        self.ht = [Pool() for _ in range(2069)]

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        nk = key % self.hash_key
        self.ht[nk].update(key, val)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        nk = key % self.hash_key
        return self.ht[nk].get(key)
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        nk = key % self.hash_key
        self.ht[nk].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)