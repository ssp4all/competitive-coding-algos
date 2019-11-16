# https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:  return ""
       
        def LCP(a, b): 
            i, j = 0, 0
            l = min(len(a), len(b))
            while i < l:
                if a[i] == b[i]:
                    j += 1
                else:
                    break
                i += 1
            return j
        ans = 9**99
        n = len(strs)
        
        for i in range(n-1):
            ans = min(ans, LCP(strs[i], strs[i+1]))
        
        return (strs[0][:ans])

# Using Trie data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        
            cur = cur.children[c]
        cur.end = True
        print(cur)
        # temp = self.root
        # while temp.end == False:
        #     print(list(temp.children))
        #     temp = temp.children
    
    def longest_prefix(self):
        res = []
        cur = self.root
        while cur:
            # return when reaches the end of word or when there are more than 1 branches
            if cur.end or len(cur.children) > 1:
                return ''.join(res)
            c = list(cur.children)[0]
            print(c)
            res.append(c)
            cur = cur.children[c]
        return ''.join(res)
        
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        T = Trie()
        for s in strs:
            T.add_word(s)
        return T.longest_prefix()