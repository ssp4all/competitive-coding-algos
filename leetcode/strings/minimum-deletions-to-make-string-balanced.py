https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


""" 
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. 
s is balanced if there is no pair of indices (i,j) 
such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Example 1:

Input: s = "aababbab"
Output: 2

"""

#TC:O(N) and SC:O(N)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        if not s:   return 0 
        st = [] 
        
        size = len(s)
        count = 0
        
        for i in range(size - 1, -1, -1):
            ch = s[i]
            if st and st[-1] < ch:
                st.pop()
                count += 1 
            else:
                st += [ch]
        
        return count