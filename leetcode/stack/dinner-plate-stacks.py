https://leetcode.com/problems/dinner-plate-stacks/

"""
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, 
each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.

void push(int val) Pushes the given positive integer val into the leftmost 
stack with size less than capacity.

int pop() Returns the value at the top of the rightmost non-empty stack and removes it 
from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) Returns the value at the top of the stack with the 
given index and removes it from that stack, and returns -1 if the stack with 
that given index is empty.
Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push",
"popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

"""

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [] 
        self.queue = [] #holds leftmost index in stacks
        self.cap = capacity
        
    # TC: O(lgn)
    def push(self, val: int) -> None:
        while self.queue and self.queue[0] < len(self.stacks) and \
            len(self.stacks[self.queue[0]]) == self.cap:
            heapq.heappop(self.queue)
        if not self.queue:
            heapq.heappush(self.queue, len(self.stacks))
        if self.queue[0] == len(self.stacks):
            self.stacks += [[]]
        self.stacks[self.queue[0]] += [val]

    # TC: O(lgn)        
    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop() 
        return self.popAtStack(len(self.stacks) - 1)

    # TC: O(lgn)
    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.queue, index)
            val = self.stacks[index].pop()
            return val
        return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)