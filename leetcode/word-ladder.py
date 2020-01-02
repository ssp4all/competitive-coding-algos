https://leetcode.com/problems/word-ladder/

from collections import deque
class Solution:
    def ladderLength(self, start: str, end: str, wordlist: List[str]) -> int:
        def built_dict(wordlist):
            d = {}
            n = len(wordlist)
            for i in wordlist:
                for j in range(len(i)):
                    ss = i[:j] + '_' + i[j+1:]
                    d[ss] = d.get(ss, []) + [i]
            # print(d)
            return d
        def bfs(wordlist, start, end, d):
            que = deque([(start, 1)])
            visited = set()
            while que:
                # print(que)
                i, j = que.popleft()
                if i not in visited:
                    visited.add(i)
                    if i == end:
                        return j
                    for z in range(len(i)):
                        ss = i[:z] + '_' + i[z+1:]
                        neigh = d.get(ss, [])
                        for n in neigh:
                            if n not in visited:
                                que.append((n, j+1))
            return 0
        d = built_dict(wordlist)
        return bfs(wordlist, start, end, d)
            
                    
            