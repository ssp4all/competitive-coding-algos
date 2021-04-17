https://leetcode.com/problems/jump-game-vi/

"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can 
jump at most k steps forward without going outside the
 boundaries of the array. That is, you can jump from index 
 i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1).
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence
[1,-1,4,3] (underlined above). The sum is 7.
"""

#TC:O(N^no of ways), SC:O(N)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:    return 0 
        
        n = len(nums)
        
        dq = deque([(0, nums[0])])
        neigh = [1, k]
        seen = set()
        maxi = float('-inf')
        while dq:
            idx, score = dq.popleft() 
            if (idx, score) in seen:   continue 
            if idx == n - 1:
                maxi = max(maxi, score)
                continue
            seen.add((idx, score))
            for nei in neigh:
                nidx = min(nei + idx, n - 1)
                dq += [(nidx, score + nums[nidx])]
        return maxi


#upsolving 
# TC:O(N), SC:O(N)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:    return 0 
        
        n = len(nums)
        
        dq = deque([])
        
        for i in range(n - 1, -1, -1): #for each index
            curr = nums[i] + (nums[dq[0]] if dq else 0)
            
            while dq and curr >= nums[dq[-1]]: #remove indexes with less sum
                dq.pop() 
                
            dq += [i]
            
            while dq and dq[0] >= i + k: #remove indexes out of range
                dq.popleft() 
             
            nums[i] = curr #store current answer in the original result in the auxiliary array
            
        return curr