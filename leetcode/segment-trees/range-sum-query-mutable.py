https://leetcode.com/problems/range-sum-query-mutable/

"""
Given an integer array nums, find the sum of the elements between indices 
i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""
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

    def update_tree(self, left, right, index, value, pos):
        if left == right:
            self.seg[pos] = value 
            return
        m = left + (right - left) // 2
        if left <= index <= m:
            self.update_tree(left, m, index, value, 2*pos + 1)
        else:
            self.update_tree(m + 1, right, index, value, 2*pos + 2)
        
        self.seg[pos] = self.seg[2*pos + 1] + self.seg[2*pos + 2]
        

    def update(self, i: int, val: int) -> None:
        self.update_tree(0, self.nn - 1, i, val, 0)
    
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
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)