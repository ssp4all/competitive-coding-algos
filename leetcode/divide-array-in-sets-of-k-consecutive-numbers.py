https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6]
"""
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums or 0 >= k or k > len(nums): return 0
        n = len(nums)
        x = Counter(nums)
        li = list(x.items())
        li.sort()
        # print(li)
        li = list(map(list, li))
        
        while True:
            # print("->", li)
            i = 0
            t = k
            if li:
                st = li[i][0]
            else:
                return 0
            while t > 0:
                if i < len(li) and li[i][1] <= 0:
                    return 0
                if li and i < len(li) and li[i][0] == st:
                    li[i][1] -= 1
                    t -= 1
                    st += 1
                else:
                    return 0
                if i < len(li) and not li[i][1]:
                    del li[i]
                else:
                    i += 1
                # print(li, t)
                if not li and t > 0:
                    return 0
                
            if not li and not t:
                return 1

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums or 0 >= k or k > len(nums): return 0
        n = len(nums)
        x = Counter(nums)
        li = sorted(x)
        # print(li)
        for i in li:
            if x[i] <= 0:
                continue
            count = x[i]
            for j in range(i, i+k):
                if x[j] < count:
                    return 0
                x[j] -= count
        return 1
        