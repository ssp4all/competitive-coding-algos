https://leetcode.com/problems/powerful-integers/


"""
Given three integers x, y, and bound, return a list of 
all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj 
for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, 
each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]

"""


# here Time complexity will be O(lg(bound) / lg(x) * lg(bound) / lg(y))

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        ans = set()
        
        i = 1 
        while i < bound:
            j = 1
            while i + j <= bound:
                ans.add(i + j)
                j *= y
                if y == 1:  break
            i *= x
            if x == 1:  break
        return ans