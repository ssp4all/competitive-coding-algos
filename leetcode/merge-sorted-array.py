https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 and not nums2: return nums1
        if not nums1 or not nums2: return nums1 or nums2
        la = m + n
        while m < la:
            nums1.pop()
            la -= 1
        # print(nums1)
        a = 0
        b = 0
        while b < n:
            if a < la:
                if nums1[a] >= nums2[b]:
                    nums1.insert(a, nums2[b])
                    b += 1
                    la += 1
                else:
                    a += 1
            else:
                nums1.extend(nums2[b:])
                break