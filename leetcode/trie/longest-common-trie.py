from collections import defaultdict

class Node:
    def __init__(self):
        self.childrens = defaultdict(Node)
        self.end = 0

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        self.root = Node()
        for s in strs:
            ans = ""
            cur = self.root
            if cur.end or len(cur.childrens) > 1 or not s:
                return ""
            prev = cur
            for w in s:
                cur = cur.childrens[w]
                ans += w
                if len(prev.childrens) > 1:
                    return ans[:-1]
                if cur.end:
                    return ans
                
                prev = cur
            cur.end = 1
        return ans