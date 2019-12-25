https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        ans = []
        
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            if matrix and matrix[-1]:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
            
        print(matrix, ans)
        return ans