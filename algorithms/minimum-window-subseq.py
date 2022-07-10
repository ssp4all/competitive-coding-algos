# https://leetcode.ca/2017-11-26-727-Minimum-Window-Subsequence/

"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
If there is no such window in S that covers all characters in T, 
return the empty string "". If there are multiple such minimum-length windows, 
return the one with the left-most starting index.

Example 1:
Input: S = “abcdebdde”, T = “bde”

Output: “bcde”
Explanation:
“bcde” is the answer because it occurs before “bdde” which has the same length.
“deb” is not a smaller window because the elements of T in the window must occur in order.
"""

s = "abcxabxc"
t = "abc"

# TC: O(N)
# SC: O(N)
def shorted_substring_with_t(s, t):
    left, size = 0, len(s)
    ptr1, ptr2 = 0, 0 
    n = len(s)
    
    while ptr1 < n:
        if s[ptr1] == t[ptr2]:
            ptr2 += 1 
        if ptr2 == len(t): #found a match 
            rightIndex = ptr1 
            ptr2 -= 1
            while ptr2 >= 0: #track back until size of t 
                if t[ptr2] == s[ptr1]:
                    ptr2 -=  1 
                ptr1 -= 1 
            if left + size > rightIndex - ptr1: #record ans
                left = ptr1 + 1 
                size = rightIndex - left + 1 
            ptr2 = 0 
            ptr1 = rightIndex 
        ptr1 += 1 

    print(s[left: left + size])

shorted_substring_with_t(s, t)