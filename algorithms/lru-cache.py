# Design a Least Recently Used (LRU) cache. Think about the readability, maintainability and scalability of your code.
# Implement the LRUCache class:
# LRUCache(capacity): Initializes the LRU cache with a positive size capacity
# int get(key): Returns the value of the key if the key exists
# void put(key, value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key

"""
N = 2
[1,5]
{1:asd, 4: 123}
"""

class Node:
    def __init__(self, k, v):
        self.k = k 
        self.v = v 
        self.nxt = self.prev = None 

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity  
        self.head, self.tail = Node(-1, -1), Node(-1, -1) # TODO: revisit
        self.head.nxt = self.tail 
        self.tail.prev = self.head
        self.lookup = {}
    
    def get(self, key):
        if key in self.lookup:
            node = self.lookup[key]
            self.__remove(node)
            self.__append(node)
            return node.v 
        return -1
    
    def __remove(self, node: Node):
        left, right = node.prev, node.nxt 
        left.nxt = right 
        right.prev = left
        node.prev, node.nxt = None, None  
    
    def __popleft(self):
        if len(self.lookup) == 0:   return 
        node = self.head.nxt
        self.__remove(node)
        return node
    
    def __append(self, node):
        prev = self.tail.prev 
        prev.nxt = node 
        node.prev = prev 
        node.nxt = self.tail
        self.tail.prev = node

    def put(self, key, value):
        if key in self.lookup:
            node = self.lookup[key]
            node.v = value
            self.__remove(node) 
            self.__append(node)
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node 
            self.__append(new_node)
            # size check 
            if len(self.lookup) > self.cap:
                node = self.__popleft()  # evict left most 
                del self.lookup[node.k]
                del node
        return 

cache = LRUCache(3)
try:
    value = cache.get(10)
except Exception as e:
    print(e)
cache.put(10, 10)
try:
    value = cache.get(10)
    print(value)
except Exception as e:
    print(e)
cache.put(20, 20)
cache.put(30, 30)
cache.put(40, 40)
value = cache.get(40)
print(value)
value = cache.get(10)
print("->", value)