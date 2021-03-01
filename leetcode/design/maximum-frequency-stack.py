https://leetcode.com/problems/maximum-frequency-stack/

"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the 
top of the stack is removed and returned.
 
Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
"""

# TC:O(1), SC:O(N)
class FreqStack:

    def __init__(self):
        self.freq = Counter()  #to keep track of frequencies
        self.groups = defaultdict(list) # to keep track of elements with cetain freq
        self.maxi = 0 #current max freq in the stack 
        
    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.freq[x] > self.maxi:
            self.maxi = self.freq[x]
        
        self.groups[self.freq[x]] += [x]

    def pop(self) -> int:
        try:
            item = self.groups[self.maxi].pop()
            self.freq[item] -= 1
            if not self.groups[self.maxi ]:
                self.maxi -= 1

            return item
        except IndexError:
            # print(self.freq, self.groups)
            print('Empty!!!')

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()