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

# TC: O(M + N)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if len(nums1) == m:  return 
        
        i = m - 1
        j = n - 1
        k = m + n - 1 
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i, k = i - 1, k - 1
            else:
                nums1[k] = nums2[j]
                j, k = j - 1, k - 1
            
        while j >= 0:
            nums1[k] = nums2[j]
            j, k = j - 1, k - 1
        return 