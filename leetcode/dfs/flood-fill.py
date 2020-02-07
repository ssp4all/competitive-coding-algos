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