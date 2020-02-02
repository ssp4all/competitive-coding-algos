https://leetcode.com/problems/search-suggestions-system/

class Node:
    def __init__(self):
        self.letters = [None] * 26
        self.end = 0
        self.suggestions = []

class Solution:
    
    def suggestedProducts(self, products: List[str], search: str) -> List[List[str]]:
        if not products:   return products
        n = len(products)
        root = Node()
        k = 3
        
        def to_int(c):
            return ord(c) - ord('a')
        
        def to_char(i):
            return chr(i + 97)
        
        def insert_into_trie(product):
            cur = root
            for w in product:
                val = to_int(w)
                if not cur.letters[val]:
                    cur.letters[val] = Node()
                cur = cur.letters[val]
            cur.end += 1
        
        def start_with(word):
            cur = root
            for w in word:
                i = to_int(w)
                cur = cur.letters[i]
                if not cur: return []
            words = dfs(cur, list(word))
            return words
        
        def dfs(cur, path):
            words = []
            if not cur: return []
            if cur.suggestions:
                return cur.suggestions
            if cur.end:
                w = "".join(path)
                for _ in range(cur.end):
                    words.append(w)
            for ind, node in enumerate(cur.letters):
                ws = dfs(node, path + [to_char(ind)])
                words += ws
                if len(words) >= k:
                    cur.suggestions = words[:k]
                    return cur.suggestions
                cur.suggestions = words
            return cur.suggestions
                
        
        for prod in products:
            insert_into_trie(prod)
        return [start_with(search[:i]) for i in range(1, len(search) + 1)]
            
        
import bisect

class Solution:
    
    def suggestedProducts(self, A: List[str], word: str) -> List[List[str]]:
        if not A:   return A
        A.sort()
        # print(A)
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            # print(prefix)
            i = bisect.bisect_left(A, prefix, i)
            # print(i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
            # print(res)
        return res