https://leetcode.com/discuss/interview-question/algorithms/124822/bloomberg-interview-question-find-first-unique-integer-in-a-stream

from heapq import *

class Node:
    def __init__(self, v):
        self.v = v
        self.next = self.prev = None
        
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = dict()
        
        self.head = self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        
        for n in nums:
            if n in self.cache:
                self._del(self.cache[n])
                self.cache[n] = None
            else:
                t = Node(n)
                self._add(t)
                self.cache[n] = t
                
    def _add(self, node):
        p = self.tail.prev
        node.next = p.next
        node.prev = p
        p.next = node
        self.tail.prev = node
    
    def _del(self, node):
        if not node:
            return
        p = node.next
        q = node.prev
        q.next = p
        p.prev = q
            
    def showFirstUnique(self) -> int:
        p = self.head.next 
        if p.v == float('inf'):
            return -1
        else:
            return p.v

    def add(self, value: int) -> None:
        if value in self.cache :
            n = self.cache[value]
            if n:
                self._del(n)
        else:
            t = Node(value)
            self._add(t)
            self.cache[value] = t
                
                    
                
            
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)