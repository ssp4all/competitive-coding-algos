https://leetcode.com/problems/alphabet-board-path/

"""
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  
You may return any path that does so.

 

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
"""

from collections import deque

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        board = []
        for i in range(26):
            if i % 5  == 0:
                board += [[]]
            board[-1] += [chr(i + ord('a'))]
        # print(board)
        
        output = []
        
        def within(x, y, seen):
            if ((x, y) == (5, 0) and (x, y) not in seen) or \
                    (0 <= x < len(board) - 1  and \
                    0 <= y < len(board[0])) and \
                        (x, y) not in seen:
                return 1
            return 0
            
        dq = deque([(0, 0, "")])
        neigh = [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]
        cur = 0
        seen = set()
        while dq:
            i, j, path = dq.popleft()
            if cur == len(target):
                return "".join(output)
            if cur < len(target) and board[i][j] == target[cur]:
                output += path + "!"
                seen.clear()
                dq = deque([(i, j, "")])
                cur += 1
                continue
            seen.add((i, j))
            for x, y, D in neigh:
                ni, nj = x + i, y + j
                if within(ni, nj, seen):
                    dq += [(ni, nj, path + D)]
                    
        return ""

                    
from string import ascii_lowercase

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        mapping = {c : [i // 5, i % 5] for i, c in enumerate(ascii_lowercase)}
        output = ""
        x0, y0 = 0, 0
        for ch in target:
            x, y = mapping[ch]
            if y < y0:  output += "L" * (y0 - y)
            if x < x0:  output += "U" * (x0 - x)
            if x0 < x:  output += "D" * (x - x0)
            if y0 < y:  output += "R" * (y - y0)
            output += "!"
            x0, y0 = x, y
        return output
                    
                
                