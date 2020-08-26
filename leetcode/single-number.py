class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return -1
        x = 0
        for i in nums:
            x ^= i
        return x
        
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber(self, nums): 
	    hash_table = {}
	    for i in nums:
	        try:
	            hash_table.pop(i)
	        except:
	            hash_table[i] = 1
	    return hash_table.popitem()[0]