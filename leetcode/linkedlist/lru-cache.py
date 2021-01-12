https://leetcode.com/problems/lru-cache

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the 
capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?
"""

class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        else:
            return -1
    
    def _remove(self, n):
        p = n.prev
        q = n.next
        p.next = q
        q.prev = p
        
    def _add(self, n):
        p = self.tail.prev
        p.next = n
        n.prev = p
        n.next = self.tail
        self.tail.prev = n
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.cap:
            p = self.head.next
            self._remove(p)
            del self.dic[p.key]
            
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

Same can be solved using Ordered dict 
as well as deque but complexity will be O(capacity)

def __init__(self, capacity):
    self.deque = collections.deque([])
    self.dic = {}
    self.capacity = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    self.deque.remove(key)
    self.deque.append(key)
    return self.dic[key]

def set(self, key, value):
    if key in self.dic:    
        self.deque.remove(key)
    elif len(self.dic) == self.capacity:
        v = self.deque.popleft()  # remove the Least Recently Used element
        self.dic.pop(v)
    self.deque.append(key)
    self.dic[key] = value 