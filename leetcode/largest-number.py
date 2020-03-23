https://leetcode.com/problems/largest-number/

"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
"""
class Funct(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums: return -1
        
        nums = list(map(str, nums))
        xx = sorted(nums, key=Funct)
        
        print(xx)
        ans = "".join(xx)
        return "0" if ans[0] == "0" else ans