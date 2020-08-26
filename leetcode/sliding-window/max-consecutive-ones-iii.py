https://leetcode.com/problems/max-consecutive-ones-iii/

Brute force

class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        if not a: return 0
            
        n = len(a)
        l, r = 0, n-1
        m = 0
        ans, maxi, zeroes, ones = 0, 0, 0, 0
        
        if k == 0: 
            while l <= r:
                while l <= r and a[l] == 1:
                    ones += 1
                    l += 1
                ans = max(ans, ones)
                ones = 0
                while l <= r and a[l] == 0:
                    l += 1
                
            return ans
        
        while l <= r and m <= r:
            while m <= r:   #add zeroes counter
                if a[m] == 1:   
                    ones += 1
                else:
                    zeroes += 1
                if zeroes > k:
                    zeroes -= 1
                    m -= 1
                    break
                m += 1 
            ans = max(ans, zeroes + ones)
            # print(m, ans)
            while m <= r and l <= m and a[l] == 1 :
                ones -= 1
                l += 1
            while m <= r and l <= m and a[l] == 0 and zeroes >= k:
                zeroes -= 1
                l += 1
            m += 1
        return ans


class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        if not a: return 0
            
        n = len(a)
        i = 0
        for j in range(n):
            k -= (1 - a[j])
            if k < 0:
                k += (1 - a[i])
                i += 1
        return (j - i + 1)
