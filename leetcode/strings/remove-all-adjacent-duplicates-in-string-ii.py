https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

"""
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters 
from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:   return ""
        if k <= 0:  return s

        stack = [["#", 0]]
        
        for ch in s:
            if stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack += [[ch, 1]]
                
        return "".join(i * j for i, j in stack[1:])

# two pointer solution
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:   return s 
        
        n = len(s)
        
        #two pointer solution 
        s = list(s)
        counter = [0] * n 
        i = -1
        
        for j in range(n):
            i += 1
            s[i] = s[j]
            counter[i] = counter[i - 1] + 1 if i > 0 and s[j] == s[i - 1] else 1 
            if counter[i] == k:
                i -= k 
        i += 1     
        return "".join(s[:i])

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:   return ""
        if k <= 0:  return s

        found = 1
        while found == 1:
            
            found = 0
            prev = len(s)
            cur = 0
            ans = ""

            while cur < len(s):
                ch = s[cur]
                anchor = cur
                while cur < len(s) and anchor + k > cur and s[cur] == ch:
                    cur += 1
                if anchor + k > cur:
                    ans += s[anchor: cur]

            if len(ans) != prev:
                found = 1
                s = ans

        return s 