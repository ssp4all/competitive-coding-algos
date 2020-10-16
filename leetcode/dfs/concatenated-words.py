https://leetcode.com/problems/concatenated-words

"""
Given a list of words (without duplicates), please write a program that returns all 
concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two 
shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat"
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words or not words[0]:
            return []
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                pref = word[:i]
                suff = word[i:]
                if pref in d and suff in d:
                    return 1
                if pref in d and dfs(suff):
                    return 1
                
            return 0
        
        op = []
        for word in words:
            if dfs(word):
                op.append(word)
        return op


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words or not words[0]:
            return []
        words.sort(key=lambda t:len(t))
        d = set()
        def dfs(w):
            if not d:   return 0
            if w in d:  return 1
            for i in range(1, len(w)):
                if w[:i] in d and dfs(w[i:]):
                    return 1
            return 0
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
            d.add(w)
        return res

# memorized
class Solution:
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        d = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = 0
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    memo[word] = True 
                    return 1
                if prefix in d and dfs(suffix):
                    memo[word] = True 
                    return 1
            return 0
        return [word for word in words if dfs(word)] 