https://leetcode.com/problems/lfu-cache/

"""
Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Sets or inserts the value if the key is not already present. 
When the cache reaches its capacity, it should invalidate the least frequently used item 
before inserting a new item. For this problem, when there is a 
tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = self.next = None
        
class DLinkedList:
    def __init__(self):
        self.last = Node(None, None)
        self.last.next = self.last.prev = self.last
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def appendleft(self, node):
        node.next = self.last.next
        node.prev = self.last
        node.next.prev = node
        self.last.next = node
        self.size += 1
    
    def pop(self, node=None):
        if self.size == 0:  return 
        
        if not node:
            node = self.last.prev
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
        return node 

        
class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.nodes = {}
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0
    
    def update(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        
        if self.minfreq == freq and \
            not self.freq[freq]:
            self.minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self.freq[freq].appendleft(node)
    
    def get(self, key: int) -> int:
        if key not in self.nodes:    return -1
        
        node = self.nodes[key]
        self.update(node)
        return node.val
    
    

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:   return
        if key in self.nodes:
            node = self.nodes[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.cap:
                node = self.freq[self.minfreq].pop()
                del self.nodes[node.key]
                self.size -= 1
            
            node = Node(key, value)
            self.nodes[key] = node
            self.freq[1].appendleft(node)
            self.minfreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)