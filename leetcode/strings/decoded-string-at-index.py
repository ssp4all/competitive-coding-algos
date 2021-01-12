https://leetcode.com/problems/decoded-string-at-index

"""
An encoded string S is given.  To find and write the decoded string to a tape, 
the encoded string is read one character at a time and the following steps are 
taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly 
written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the 
K-th letter (1 indexed) in the decoded string.


Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
"""

# TC: O(N), SC:O(1)
class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size //= int(c)
            else:
                size -= 1
