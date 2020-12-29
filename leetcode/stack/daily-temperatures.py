https://leetcode.com/problems/daily-temperatures/

"""

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be 
an integer in the range [30, 100].

"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:   return []
        
        stack = []
        n = len(T)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop() 
            if stack:
                ans[i] = stack[-1] - i 
            stack += [i]
        return ans

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:   return []
        stack = []
        n = len(T)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop() 
            if stack:
                ans[i] = stack[-1] - i 
            stack += [i]
        return ans
    
    """
    n = 8
    
    [0,1,2,3,4,5,6,7]

    [73, 74, 75, 71, 69, 72, 76, 73]
    
    stack = [2,3,4,5]
    
    ans = [1,1,0,0,0,1,0,0]
    [1, 1, 4, 2, 1, 1, 0, 0]    
    """
