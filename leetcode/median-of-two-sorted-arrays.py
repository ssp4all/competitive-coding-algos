https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        m = len(a)
        n = len(b)
        even = 0
        if (m+n) % 2 == 0:
            even = 1
        tar = (m + n - 1) // 2
        op = []
        i, j = 0, 0
        while i < m and j < n:
            if a[i] < b[j]:
                op.append(a[i])
                i += 1
            else:
                op.append(b[j])
                j += 1
            if even == 0 and len(op)-1 == tar:
                return op[tar]
            elif even == 1 and len(op)-1 == tar+1:
                return (op[tar] + op[tar+1]) / 2 
        op += a[i:]
        op += b[j:]
        if even == 0:
            return op[tar]
        else:
            return (op[tar] + op[tar+1]) / 2
            