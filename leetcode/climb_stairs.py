# https://leetcode.com/problems/climbing-stairs/

# This algorithm uses fibonacci to solve this problem, just return fibonacci number of n+1 for a given n numbers of stairs.
Here, idea is to store previously calculated values instead of calculating again and again.

def climbStairs(self, n: int) -> int:
        ans = [-1]*47   #initialize list
        ans[0] = 0
        ans[1] = 1
        if ans[n+1] != -1:  #if already calculated then return directly
            return ans[n+1]
        else:
            for i in range(ans.index(-1), n+2): #if not calculated then calculate and then store
                ans[i] = ans[i-1] + ans[i-2]
        return ans[n+1]
