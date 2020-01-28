https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, no: int) -> List[List[int]]:
        if not no: return []
        op = [[1]]
        if no == 1: return op
        for i in range(1, no):
            temp = [1]
            for j in range(i-1):
                temp.append(op[i-1][j]+op[i-1][j+1])
            temp.append(1)
            op.append(temp)
        return op