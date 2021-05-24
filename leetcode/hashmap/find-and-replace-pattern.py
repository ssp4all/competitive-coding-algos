https://leetcode.com/problems/find-and-replace-pattern/


"""
Given a list of strings words and a string pattern, return a 
list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of 
letters p so that after replacing every letter x in the pattern 
with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from 
letters to letters: every letter maps to another letter, 
and no two letters map to the same letter.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

"""

#TC:O(N*max(of wordlist)), SC:O(max of word list + pattern)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        matches = []
        
        for word in words:
            lookup = {}  # pattern to word mapping
            backward = {} # word to pattern mapping
            if len(word) != len(pattern):
                continue 
            size = len(word)
            
            for i in range(size):
                ch = word[i]
                if pattern[i] in lookup :
                    if lookup[pattern[i]] != ch:
                        break 
                elif ch not in backward:
                    lookup[pattern[i]] = ch
                    backward[ch] = pattern[i]
                else:
                    break
            else:
                matches += [word]
        
        return matches