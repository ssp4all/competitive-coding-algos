class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])
        
        res = [[0] * c2 for _ in range(r1)]
        
        # now using compression technique 
        def get_compressed(mat):
            m, n = len(mat), len(mat[0])
            comp = [[] for _ in range(m)] 
            for i in range(m):
                for j in range(n):
                    if mat[i][j]:
                        comp[i].append((mat[i][j], j)) # store (val, col_index)
            return comp 

        A, B = get_compressed(mat1), get_compressed(mat2)

        for i in range(r1):
            for v1, j in A[i]:
                for v2, k in B[j]:
                    res[i][k] += v1 * v2 


        # for i in range(r1):
        #     for j in range(c1):
        #         if mat1[i][j]:
        #             for k in range(c2):
        #                 res[i][k] += mat1[i][j] * mat2[j][k]


        # for i in range(r1):
        #     for j in range(c2):
        #         for k in range(r2):
        #             res[i][j] += mat1[i][k] * mat2[k][j]

        return res