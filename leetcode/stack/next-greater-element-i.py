https://leetcode.com/problems/next-greater-element-i/

"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right 
in nums2. If it does not exist, output -1 for this number.

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]

"""
#O(n^2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {num: ind for ind, num in enumerate(nums2)}
        res = []
        n = len(nums2)
        for num in nums1:
            st = seen.get(num, -1)
            if st == -1 or st == n - 1:
                res += [-1]
            else:
                flag = 0
                for i in range(st + 1, n):
                    if nums2[i] > num:
                        res += [nums2[i]]
                        flag = 1
                        break 
                if not flag:
                    res += [-1]
        return res

#O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        seen = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                seen[stack.pop()] = num 
            stack += [num]
        
        res = []
        for num in nums1:
            res += [seen.get(num, -1)]
        
        return res