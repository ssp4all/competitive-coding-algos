https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not A or A == sorted(A):
            return []
        
        #lets start out greedy solution 
        n = len(A)
        ptr = n - 1
        ans = []
        def swapping(A, ind):
            i = 0
            while i <= ind // 2:
                A[ind - i], A[i] = A[i], A[ind - i]
                i += 1
            return A
        
        cur_highest_ind = A.index(max(A[:ptr + 1]))
        # print(ptr, cur_highest_ind, A)
        while ptr > -1  and cur_highest_ind != ptr or A != sorted(A):
            # if cur_highest_ind == ptr:
            #     ptr -= 1
            ans += [cur_highest_ind + 1]
            A = swapping(A, cur_highest_ind)
            ans += [ptr + 1]
            A = swapping(A, ptr)
            ptr -= 1
            cur_highest_ind = A.index(max(A[:ptr + 1]))
            
        return ans