https://leetcode.com/problems/buddy-strings/

"""
Given two strings A and B of lowercase letters, return true if you can swap two 
letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):    return 0
        
        if A == B:#same strings
            seen = set()
            for ch in A:
                if ch in seen:  return 1
                seen.add(ch)
            return 0
        mismatch = 0
        different_chars = []
        for i in range(len(A)):
            if A[i] != B[i]:
                mismatch += 1
                different_chars += [A[i], B[i]]
            if mismatch > 2:
                return 0
        if mismatch == 2:
            return different_chars[:2] == different_chars[2:][::-1]
        return 0
            