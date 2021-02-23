https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"

"""
# TC:O(NlgN + N * min(W, S)), O()
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s or not d:   return "" 
                
        d.sort(key=lambda x: (len(x), x))
        
        if len(s) < len(d[0]): return ""
        
        n = len(d)
        
        @lru_cache(None)
        def check(word: str, idx: int) -> bool:
            if word and idx == len(s):  return 0 
            if not word and idx <= len(s):
                return 1
            return (word[0] == s[idx] and check(word[1:], idx + 1)) or \
                        (check(word, idx + 1))
        
        ans = ""
        for i in range(n - 1, -1, -1):
            word = d[i]
            if len(word) > len(s):  
                continue
            if check(word, 0):
                if (len(word) > len(ans)) or \
                    (len(word) == len(ans) and word < ans):
                    ans = word 
                
                if i > 0 and len(d[i - 1]) < len(word):
                    break
        return ans

# upsolving
# TC:O(N * min(S, Avg length)), SC:O(MAx length in the D)
class Solution:
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        op = list(filter(isSubsequence, d)) 
        print(op)
        return min(op + [''], key=lambda x: (-len(x), x))

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''
    """
    "abpcplea"
    ["ale","apple","monkey","plea"]
    "abpcplea"
    ["a","b","c"]
    """