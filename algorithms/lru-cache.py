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
    def __init__(self, key, value):
        self.k = key 
        self.v = value 
        self.nxt = self.prev = None 

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity  
        self.head, self.tail = Node(-1, -1), Node(-1, -1) # TODO: revisit
        self.head.nxt = self.tail 
        self.tail.prev = self.head
        self.lookup = {} # store key = node reference 
    
    def get(self, key):
        if key in self.lookup:
            node = self.lookup[key]
            value = self.__remove(node)
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.__append(new_node)
            return node.v 
        else:
            raise KeyError('key not found')
    
    def __remove(self, node: Node):
        # removes node from the DLL 
        # TODO: what if there is only one key, or zero
        value = node.v
        left, right = node.prev, node.nxt 
        left.nxt = right 
        right.prev = left
        node.prev, node.nxt = None, None 
        del node 
        return value
    
    def __popleft(self):
        _ = self.__remove(self.head.nxt)
        return
    
    def __append(self, node):
        prev = self.tail.prev 
        prev.nxt = node 
        node.prev = prev 
        node.nxt = self.tail

    def put(self, key, value):
        try:
            if key in self.lookup:
                node = self.lookup[key]
                node.v = value
                self.__remove(node) 
                new_node = Node(key, value)
                self.__append(new_node)
                # update lookup 
                self.lookup[key] = new_node
            else:
                # size check 
                if len(self.lookup) == self.cap:
                    # evict left most 
                    self.__popleft()   
                new_node = Node(key, value)
                self.lookup[key] = new_node 
                self.__append(new_node)
            return 
        except Exception as e:
            return e 


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