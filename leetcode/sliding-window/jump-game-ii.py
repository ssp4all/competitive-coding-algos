https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        end, far = 0, 0
        for i in range(n-1):
            far = max(far, i + nums[i])
            if i == end:
                ans += 1
                end = far
        return ans


"""
TC: O(n^(n - i)) i goes from 1 to n
SC: O(same as above)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dq = collections.deque([(0, 0)])
        seen = set()
        
        while dq:
            index, cost = dq.popleft() 
            if index >= n - 1:
                return cost
            if index in seen or nums[index] == 0:
                continue

            seen.add(index)
            for i in range(index + 1, index + nums[index] + 1):
                dq += [(i, cost + 1)]