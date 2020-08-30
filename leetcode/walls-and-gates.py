https://leetcode.com/problems/walls-and-gates/

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        row = len(rooms)
        col = len(rooms[0])
        seen = set()
        
        def dfs(u, v, depth):
            if 0 <= u < row and 0 <= v < col and \
                    (u, v) not in seen and \
                            rooms[u][v] != -1:
                seen.add((u, v))
                if rooms[u][v] not in [0, -1]:
                    if rooms[u][v] > depth:
                        rooms[u][v] = depth
                    else:
                        return
                dfs(u, v+1, depth+1)
                dfs(u, v-1, depth+1)
                dfs(u+1, v, depth+1)
                dfs(u-1, v, depth+1)
         
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0 :
                    dfs(i, j, 0)
                    seen.clear()
        print(rooms)