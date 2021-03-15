https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least 
one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one 
occurrence of the characters a, b and c are "abc", 
"abca", "abcab", "abcabc", "bca", "bcab", "bcabc", 
"cab", "cabc" and "abc" (again). 
"""

# TC:O(N), SC:O(1)
 def numberOfSubstrings(self, s):
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in xrange(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res