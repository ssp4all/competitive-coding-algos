https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num: return num
        n = len(num)
        
        if k >= n: return "0"
        i = 0
        numl = list(num)
        
        while k > 0:
            while i + 1 < len(numl) and int(numl[i]) <= int(numl[i + 1]):
                i += 1
            if i + 1 < len(numl) and int(numl[i + 1]) >=int(numl[i]):
                del numl[i + 1]
            else:
                del numl[i]
            i = (i - 1 if i > 0 else 0)
            k -= 1
            
            while len(numl) >= 1 and int(numl[0]) == 0:
                del numl[0]
                i = (i - 1 if i > 0 else 0)
                
        if not numl:   return "0"
        return "".join(numl)
            
            i