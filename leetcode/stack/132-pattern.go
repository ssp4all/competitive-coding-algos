// https://leetcode.com/problems/132-pattern/submissions/

// Given an array of n integers nums, a 132 pattern is a subsequence of 
// three integers nums[i], nums[j] and nums[k] such that i < j < k and 
// nums[i] < nums[k] < nums[j].

// Return true if there is a 132 pattern in nums, otherwise, return false.

 

// Example 1:

// Input: nums = [1,2,3,4]
// Output: false
// Explanation: There is no 132 pattern in the sequence.
// Example 2:

// Input: nums = [3,1,4,2]
// Output: true
// Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
// Example 3:

// Input: nums = [-1,3,2,0]
// Output: true
// Explanation: There are three 132 patterns in the sequence: 
// [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

// TC: O(N)
// SC: O(N)

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

// TC: O(N^2)
// SC: O(1)
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


//////////////////////////////////////////////////////////////////////////
// 123-pattern
// https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/
// https://leetcode.com/problems/increasing-triplet-subsequence/

// Solution - 1
// TC: O(N^2)
// SC: O(1)
def find123pattern(nums):
    n = len(nums)
    mini = nums[0]
    for i in range(1, n - 1):
        mini = min(mini, nums[i])
        for j in range(i + 1, n):
            if nums[j] > mini and nums[i] < nums[j]:
                return True 
    return False

// Optimization - 1
// 1. Maintain two extra arrays named smaller and greater to track index of elements 
//   smaller and greater for the given element 
// 2. Fill both array in two runs 
// 3. In last run check if current element has smaller and greater is not -1 

class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
// or solve it using https://leetcode.com/problems/longest-increasing-subsequence/ 
// in TC: O(NlgK)