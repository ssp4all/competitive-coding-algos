https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, nc: int) -> List[List[int]]:
        if not image:   return image
        def FF(u, v, xx, nc):
            if u >= row or v >= col or u < 0 or v < 0 or image[u][v] != xx:
                return
            
            image[u][v] = nc
            
            FF(u+1, v, xx, nc)
            FF(u-1, v, xx, nc)
            FF(u, v+1, xx, nc)
            FF(u, v-1, xx, nc)
            return
            
        if image[sr][sc] == nc: return image
        row = len(image)
        col = len(image[0])
        
        FF(sr, sc, image[sr][sc], nc)
        return image

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, nc: int) -> List[List[int]]:
        sp = image[sr][sc]
        if not image or sp == nc or not image[0]: return image
        row = len(image)
        col = len(image[0])
        
        queue = deque([(sr, sc)])
        while queue:
            x, y = queue.popleft()
            image[x][y] = nc
            for (a, b) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + a, y + b 
                if 0 <= nx < row and 0 <= ny < col and \
                    image[nx][ny] == sp:
                    queue.append((nx, ny))
        return image