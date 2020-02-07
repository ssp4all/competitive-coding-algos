https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        seen = set()
        
        def check(mat):
            row = len(mat)
            for i in range(row):
                seen.clear()
                for j in range(row):
                    if mat[i][j] != "." and mat[i][j] in seen:
                        return 0
                    elif mat[i][j] != ".":
                        seen.add(mat[i][j])

            seen.clear()
            for i in range(row):
                seen.clear()
                for j in range(row):
                    if mat[j][i] != "." and mat[j][i] in seen:
                        return 0
                    elif mat[j][i] != ".":
                        seen.add(mat[j][i])

            return 1
            
                    
        blocks = [[] for _ in range(9)]
        j = 0
        for ind, val in enumerate(board):
            if 0 <= ind < 3:
                j = 0
            elif 3 <= ind < 6:
                j = 3
            elif 6 <= ind < 9:
                j = 6
            for i in range(0, 9, 3):
                # print(i, j, ind)
                ss = val[i : i+3]
                
                blocks[j].extend(ss)
                # print(ss, blocks)
                j += 1
        # print(blocks)
        if check(board):
            for i in blocks:
                seen.clear()
                for j in range(9):
                    if i[j] != "." and i[j] in seen:
                        return 0
                    else:
                        seen.add(i[j])
        else:
            return 0
        return 1

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        
        for i, r in enumerate(board):
            for j, n in enumerate(r):
                if n == ".":    
                    continue
                if n in row[i]:
                    return 0
                if n in col[j]:
                    return 0
        
                right = i // 3
                down = j // 3
                if n in box[right + 3*down]:
                    return 0

                row[i].add(n)
                col[j].add(n)
                box[right + down*3].add(n)
            
        return 1