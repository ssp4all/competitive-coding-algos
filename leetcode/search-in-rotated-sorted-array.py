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
    
#Mycode
# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, a: List[int], t: int) -> int:
        if not a: return -1
        
        def min_index():
            n = len(a)
            l = 0
            r = n - 1
            while l < r:
                if a[l] <= a[r]: return l
                m = (l+r) // 2
                if a[m] >= a[l]:
                    l = m + 1
                else:
                    r = m
            return l
        
        x = min_index()
        print(x)
        n = len(a)
        l = 0
        r = n - 1
        if a[x] == t: return x
        if l != x and a[l] <= t <= a[x-1]:
            r = x - 1
        else:
            l = x
            
        while l < r:
            m = (l + r) // 2
            if a[m] == t:   return m
            if a[m] < t:
                l = m + 1
            else:
                r = m
        return l if a[l] == t else -1
