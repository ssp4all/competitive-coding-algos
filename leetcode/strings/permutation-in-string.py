https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:   return 1
        if not s1 or not s2:    return 0
        
        x = Counter(s1)
        ls1, ls2 = len(s1), len(s2)
        
        l, r = 0, 0
        y = Counter()
        while l < ls2 - ls1 + 1:
            while r < ls2 and r - l + 1 <= ls1:
                # print(s2[l: r])
                if s2[r] in x.keys():
                    y[s2[r]] += 1
                r += 1
            # print(s2[l: r + 1], x, y)
            if x == y:
                return 1
            if s2[l] in x.keys():
                y[s2[l]] -= 1
            l += 1
        return 0