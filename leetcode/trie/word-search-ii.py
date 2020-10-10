https://leetcode.com/problems/word-search-ii/

from collections import defaultdict

class Node():
    def __init__(self):
        self.childs = defaultdict(Node)
        self.end = 0
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        op = []
        def build(w):
            cur = root
            for ch in w:
                cur = cur.childs[ch]
            cur.end = 1

        for w in words:
            build(w)

        r, c = len(board), len(board[0])
        seen = set()
        def dfs(cur, i, j, w):
            seen.add((i, j))
            if cur.end == 1:
                op.append("".join(w))
            
            tempp = cur
            for (x, y) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                if (ni, nj) in seen or \
                    not ( 0 <= ni < r and 0 <= nj < c) or \
                            board[ni][nj] not in cur.childs:   continue
                ch = board[ni][nj]
                
                temp = cur.childs[ch]
                dfs(temp, ni, nj, w + [ch])
                cur = tempp
            seen.remove((i, j))
                
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                cur = root
                seen.clear()
                if val in cur.childs:
                    cur = cur.childs[val]
                    dfs(cur, i, j, [val])
                    
        return set(op)