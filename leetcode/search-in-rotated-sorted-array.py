# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, a: List[int], t: int) -> int:
        def min_ind(nums, l, r):
            l = 0
            n = len(nums)
            r = n - 1
            while l < r:
                if nums[l] < nums[r]:
                    return l
                m = (l + r) // 2
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m
            return l

        if not a: return -1
        
        l = 0
        n = len(a)
        r = n - 1
        #find min inde ele
        ind = min_ind(a, l, r)
        print(ind)
        while l <= r:
            m = (l + r) // 2
            temp = (ind + m) % n
            if a[temp] == t: return temp
            if a[temp] < t: 
                l = m + 1
            else:
                r = m - 1
        
        return r if a[r] == t else -1
    
        