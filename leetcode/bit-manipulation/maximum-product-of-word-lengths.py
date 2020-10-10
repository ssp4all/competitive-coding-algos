
leetcode.com/problems/maximum-product-of-word-lengths

"""
Given a string array words, find the maximum value of 
length(word[i]) * length(word[j]) where the two words do not 
share common letters. You may assume that each word will contain 
only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        n = len(words)
        ans = 0
        # maxi = -99*99
        def isMismatch(a, b):
            if not len(set(a).intersection(set(b))):
                return 1
            else: 
                return 0
            
        for i in range(n):
            for j in range(1, n):
                a, b = words[i], words[j]
                if isMismatch(a, b):
                    ans = max(ans, len(a)*len(b))
        return ans

"""Optimal SOlution O(n^2) """
class Solution(object):
    def maxProduct(self, words):
        dict = {}
        for w in words:
            mask = 0
            for charr in set(w):
                mask |= (1 << (ord(charr) - ord('a')))
            # print(w, mask)
            dict[mask] = max(dict.get(mask, 0), len(w))
        # print(d)
        return max([dict[x] * dict[y] \
                for x in dict for y in dict \
                    if not x & y] or [0])