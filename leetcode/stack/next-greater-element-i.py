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

 #my sol 
 class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        use monotonous increading stack 
        idea is traverse from end then maintain stack of next bigg elem
        """
        n = len(nums2)
        st = [] 
        next_bigg = {} 
        for i in range(n - 1, -1, -1):
            val = nums2[i]
            while st and nums2[st[-1]] < val:
                st.pop() 
            next_bigg[val] = nums2[st[-1]] if st else -1 
            st += [i]
        res = []
        for num in nums1:
            res += [next_bigg.get(num, -1)]
        
        return res


##############################################
https://leetcode.com/problems/next-greater-element-ii/submissions/

"""
Given a circular integer array nums (i.e., 
the next element of nums[nums.length - 1] is 
nums[0]), return the next greater number for
every element in nums.

The next greater number of a number x is 
the first greater number to its traversing-
order next in the array, which means you could 
search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #lets try bruteforce 
        #use modulus to keep number out of range in side 0...N 
        
        n = len(nums)
        res = [-1] * n 
        for i in range(n):
            val = nums[i]
            
            for j in range(1, n):
                if nums[(i + j) % n] > val:
                    res[i] = nums[(i + j) % n]
                    break 
            
        return res


#upsolving 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #now one with mono stack 
        
        n = len(nums)
        res = [-1] * n 
        st = [] # mono stack
        for i in range(2 * n - 1, -1, -1):
            val = nums[i % n]
            
            while st and nums[st[-1]] <= val:
                st.pop() 
            
            res[i % n] = nums[st[-1]] if st else -1  
            st += [i % n] 
        
        return res
            