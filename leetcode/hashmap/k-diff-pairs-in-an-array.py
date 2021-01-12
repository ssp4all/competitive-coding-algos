https://leetcode.com/problems/k-diff-pairs-in-an-array/

"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:    return 0 
        n = len(nums)
        freq = Counter(nums)
        count = 0
        for key in freq.keys():
            if k != 0 and key + k in freq or k == 0 and freq[key] > 1:
                count += 1
        return count

"""
More practice:
1) Two sum 
	Two sum (with duplicate)
	Two sum (sorted)
2) Count all unique (a, b) in given array 
	- Use two hashmaps to record visited and one for pairs generated  refer amazon OA
3) Cound all unique index pairs with given sum
	- https://leetcode.com/discuss/interview-question/960180/Microsoft-or-Virtual-Onsite-or-All-the-pair-with-sum-equals-target
	solution:
	1) if not sorted: use hashmap
	2) If sorted given: use two pointers 
"""