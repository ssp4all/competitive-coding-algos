https://leetcode.com/problems/largest-number/

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