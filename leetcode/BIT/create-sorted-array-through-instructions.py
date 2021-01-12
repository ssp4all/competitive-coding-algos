https://leetcode.com/problems/create-sorted-array-through-instructions

from bisect import bisect_left, bisect_right

# TC: O(N*(2lgN + N))
# SC: O(N)
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        op = []
        MOD = 10 ** 9 + 7
        n = len(instructions)
        cost = 0
        for ins in instructions:
            if not op:
                op += [ins]
            else:
                left = bisect_left(op, ins)
                right = bisect_right(op, ins)
                mini = min(left, right)
                cost += min(left, len(op) - right)
                op.insert(mini, ins)
        return cost % MOD

# TC:O(N*lgM), space: O(M)

class Solution:
    def createSortedArray(self, arr: List[int]) -> int:
        op = []
        MOD = 10 ** 9 + 7
        
        
        maxi = max(arr)
        BIT = [0] * (maxi + 1)
        n = len(BIT)
        
        def get(num):
            count = 0
            while num > 0:
                count += BIT[num]
                num -= num & -num
            return count
        
        def update(num):
            while num < n:
                BIT[num] += 1 
                num += num & -num 
                
        count = 0
        for i, num in enumerate(arr):
            count += min(get(num - 1), i - get(num))
            update(num)
        return count % MOD