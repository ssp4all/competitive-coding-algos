https://leetcode.com/problems/short-encoding-of-words/

"""
A valid encoding of an array of words is any reference string 
s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting 
from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the 
shortest reference string s possible of any valid encoding of words.


Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
"""


# TC:O(N*N*M), SC:O(N)
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        ans = 0
        n = len(words)
        used = set()
        
        words.sort(key=len, reverse=1)
        
        for i in range(n):
            if i in used:   continue
            for j in range(i + 1, n):
                if j in used:   continue 
                if words[i].endswith(words[j]):
                    used.add(j)
            ans += len(words[i]) + 1
        
        return ans 

# TC:O(N*N), SC:O(N)
 class Solution(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)

# TC:O(avg word length), SC:O(N)
class Node:
    def __init__(self):
        self.childrens = defaultdict(Node)
        self.length = 0

class Solution(object):
    def minimumLengthEncoding(self, words):
        
        root = Node()

        def build(root):
            for w in set(words):
                cur = root 
                for ch in w[::-1]:
                    cur = cur.childrens[ch]
                cur.length = len(w) + 1
        
        build(root)
        
        def count_ans(node):
            if node and len(node.childrens) == 0:
                return node.length 
            count = 0
            for ch in node.childrens:
                count += count_ans(node.childrens.get(ch, None))
            return count
        
        ans = count_ans(root)
        
        return ans