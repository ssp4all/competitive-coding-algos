https://leetcode.com/problems/intersection-of-two-arrays-ii

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 and nums2: return None
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 >= n2:
            tar, aa = nums1, nums2
        else:
            tar, aa = nums2, nums1
    
        x = Counter(tar)
        op = []
        for i in aa:
            if i in x and x[i] > 0:
                op.append(i)
                x[i] -= 1
        return op
        
"""Two pointer """
class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res