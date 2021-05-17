https://leetcode.com/problems/longest-string-chain/

""" 

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only 
if we can add exactly one letter anywhere in word1 to make
 it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., 
word_k] with k >= 1, where word_1 is a predecessor of word_2,
 word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with 
words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
""" 

# TC: O(N*L*L) L = max length of a word, N = Length of words   SC:O(N*L)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        unique = set(words)
        
        @functools.lru_cache(None)
        def dfs(word):
            n = len(word)
            w = list(word)
            maxi = 1
            for i in range(n):
                ch = w[i]
                del w[i]
                new = "".join(w)
                if new in unique:
                    maxi = max(maxi, 1 + dfs(new))
                w.insert(i, ch)
            return maxi 
        
        ans = 0
        
        for w in words:
            ans = max(ans, dfs(w))
        
        return ans