https://leetcode.com/problems/asteroid-collision/

"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:   return []
        
        n = len(asteroids)
        l, r = 0, n - 1
        
        while l + 1 <= r:
            if asteroids[l] > 0 and asteroids[l + 1] < 0:
                if abs(asteroids[l]) > abs(asteroids[l + 1]):
                    del asteroids[l + 1]
                elif abs(asteroids[l]) == abs(asteroids[l + 1]):
                    del asteroids[l:l + 2]
                    r = max(0, r - 1)
                else:
                    del asteroids[l]
                r = max(0, r - 1)
                l = max(0, l - 1)
            else:
                l += 1
        return asteroids

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new: 
                    stack.pop()
                break
            else:
                stack += [new]
        return stack