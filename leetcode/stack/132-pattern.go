https://leetcode.com/problems/132-pattern/submissions/

Given an array of n integers nums, a 132 pattern is a subsequence of 
three integers nums[i], nums[j] and nums[k] such that i < j < k and 
nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: 
[-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

func find132pattern(nums []int) bool {
    n := len(nums)
    st := make([]int, 0, n)
    s3 := int(math.Inf(-1))
    // s1, s3, s2
    for i := n - 1; i > -1; i-- {
        curr := nums[i]
        if curr < s3 { // s1 found
            return true 
        } else { 
            for len(st) > 0 && curr > st[len(st) - 1] { // curr is s2
                s3 = st[len(st) - 1]
                st = st[: len(st) - 1]
            }
        }
        st = append(st, curr)
    }
    return false
}

// Python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:    return 0
        n = len(nums)
        
        mini = float('inf')
        for i in range(n):
            mini = min(mini, nums[i])
            for j in range(i + 1, n):
                if nums[j] > mini and nums[j] < nums[i]:
                    return 1
        return 0