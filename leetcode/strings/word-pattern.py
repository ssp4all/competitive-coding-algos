https://leetcode.com/problems/word-pattern

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern: return 0
        
        map_char = {}
        map_word = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):  return 0
        
        for char, word in zip(pattern, words):
            if char not in map_char:
                if word in map_word:
                    return 0
                else:
                    map_char[char] = word
                    map_word[word] = char
            else:
                if map_char[char] != word:
                    return 0
        return 1
                
        
        