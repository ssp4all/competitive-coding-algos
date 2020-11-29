https://leetcode.com/problems/decode-string/

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:   return ""
        ans = ""
        stack = []
        
        cur_str, cur_num = "", 0
        for ch in s:
            if ch == "[":
                stack += [cur_str, cur_num]
                cur_str, cur_num = "", 0
            
            elif ch == "]":
                num, prev = stack.pop(), stack.pop() 
                cur_str = prev + num * cur_str
                
            elif ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            else:
                cur_str += ch
        return cur_str