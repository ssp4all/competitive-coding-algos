https://leetcode.com/problems/vowel-spellchecker/

"""
Input: wordlist = ["KiTe","kite","hare","Hare"], 
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
"""

#   TC: O(C), where C is the total content of wordlist and queries
#   SC:O(C)
class Solution(object):
    def spellchecker(self, wordlist, queries):


        """
        idea is to use one set and two dictionaries
        first dic { kite: Kite} -> lowercase: original
        second dic {k*e*: Kite} -> hide all vowels
        """
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""
        ans = map(solve, queries)    
        return ans
    