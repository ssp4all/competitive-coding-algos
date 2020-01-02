leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        ans = 0
        n = len(s)
        dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(n-1):
            if dict[s[i]] < dict[s[i+1]]:
                ans -= dict[s[i]]
            else:
                ans += dict[s[i]]
        return ans + dict[s[-1]]