https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        op = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        # print(op)
        
        tb = {}
        for i, row in enumerate(b):
            tb[i] = {}
            for j, val in enumerate(row):
                if val:
                    tb[i][j] = val
        # print(tb)
           
        for i, row in enumerate(a):
            for j, v1 in enumerate(row):
                # print(i, j, v1)
                
                if v1:
                    for k, v2 in tb[j].items():
                        # print(k, v2)
                
                        op[i][k] += (v1 * v2)
                        # print(op)
            
            
        # for i in range(len(a)):
        #     for j in range(len(b)):
        #         for k in range(len(a[0])):
        #             op[i][j] +=(a[i][k] * b[k][j])
        return op