https://leetcode.com/problems/keyboard-row

# Given a List of words, return the words that can be 
# typed using letters of alphabet on only one 
# row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words:   return words
        n = len(words)
        r1 = set(['q','w','e','r','t','y','u','i','o','p'])
        r2 = set(['a','s','d','f','g','h','j','k','l'])
        r3 = set(['z','x', 'c','v','b','n','m'])

        check = lambda x:\
                    (any(\
                        [all(i in r1 for i in x.lower()),\
                             all(i in r2 for i in x.lower()),\
                                  all(i in r3 for i in x.lower())
                        ]))
        x = list(filter(check, words))
        return x