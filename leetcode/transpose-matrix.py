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

from functools import reduce
a = [['a','b','c'],['d','e','f'],['g','h','i']]
n = len(a[0])
a = list(reduce(lambda x, y:x+y, a))
print(a)
op = []
for i in range(n):
    op.append(a[i::n])
print(op)

output: [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']]