# https://leetcode.com/problems/transpose-matrix
from functools import reduce
from operator import add
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(A), len(A[0])
        ans = []
        x = list(reduce(add, A))
        xl = len(x)
        for i in range(n2):
            temp = []
            for j in range(0, xl, n2):
                temp.append(x[i:][j])
            ans.append(temp)
        # print(ans)
        return ans


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)