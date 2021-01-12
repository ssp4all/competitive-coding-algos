https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k 
        self.front, self.rear = 0, k - 1
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():   return 0
        self.size += 1
        self.rear = (self.rear + 1) % self.k 
        self.q[self.rear] = value
        return 1

    def deQueue(self) -> bool:
        if self.isEmpty():  return 0 
        self.size -= 1
        self.front = (self.front + 1) % self.k 
        return 1

    def Front(self) -> int:
        self.front = (self.front) % self.k 
        return self.q[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        self.rear = (self.rear) % self.k 
        return self.q[self.rear] if not self.isEmpty() else -1


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

"""
Q = [0,0,0]
front   rear
0       2

[4,4,3]
"""