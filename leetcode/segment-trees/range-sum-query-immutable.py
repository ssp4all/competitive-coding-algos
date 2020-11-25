https://leetcode.com/problems/range-sum-query-immutable/

"""
Given an integer array nums, find the sum of the elements between indices 
i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array 
in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
"""

class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sum = [0] * (n + 1)
        for i in range(n):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]

class NumArray:

    def __init__(self, arr: List[int]):
        if not arr: return 
        n = len(arr)
        self.nn = n
        x = (int)(ceil(log2(n)))
        max_size = 2 * (int)(2**x) - 1;
        
        self.seg = [0] * max_size 
        
        def build(left, right, pos):
            if left == right:
                self.seg[pos] = arr[left]
                return 
            m = left + (right - left) // 2
            build(left, m, 2 * pos + 1)
            build(m + 1, right, 2 * pos + 2)
            self.seg[pos] = self.seg[2 * pos + 1] + self.seg[2 * pos + 2]
        build(0, n - 1, 0)
    
    def query(self, qleft, qright, left, right, pos):
        if qleft <= left and qright >= right:
            return self.seg[pos]
        if qleft > right or qright < left:
            return 0
        m = left + (right - left) // 2
        
        return self.query(qleft, qright, left, m, 2 * pos + 1) +\
                self.query(qleft, qright, m + 1, right, 2 * pos + 2)
          
    def sumRange(self, i: int, j: int) -> int:
        return self.query(i, j, 0, self.nn - 1, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)