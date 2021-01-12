https://leetcode.com/problems/implement-queue-using-stacks/

# (Two Stacks) Push - O(1)O(1) per operation, Pop - Amortized O(1)O(1) per operation
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = [] 
        self.l2 = []
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.l1 += [x]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.l2.pop() if self.l2 else -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.l2:
            while self.l1:
                self.l2 += [self.l1.pop()]
        return self.l2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.l1 and not self.l2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
Q = [1,2,3]
s1 = [7,8]
s2 = [6,5]

"""

q = [2, 3]
cap = 3
size = 3
front   rear
2        5
