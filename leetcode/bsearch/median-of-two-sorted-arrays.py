https://leetcode.com/problems/median-of-two-sorted-arrays
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if not a and not b: return 0
        la, lb = len(a), len(b)
        par = (la + lb + 1) // 2
        if la > lb:
            a, b, la, lb = b, a, lb, la
        s, e = 0, la
        # l, r = la //2 , par - (la // 2)
        # print(l, r)
        while s <= e:
            i = (s + e) // 2
            j = par - i
            if i < la and b[j - 1] > a[i]:
                s = i + 1
            elif i > 0 and b[j] < a[i - 1]:
                e = i - 1
            else:
                if i == 0:
                    ml = b[j - 1]
                elif j == 0:
                    ml = a[i - 1]
                else:
                    ml = max(a[i - 1], b[j - 1])
                
                if (la + lb) & 1:
                    return ml
                if i == la:
                    mr = b[j]
                elif j == lb:
                    mr = a[i]
                else:
                    mr = min(a[i], b[j])
                
                return (ml + mr) / 2