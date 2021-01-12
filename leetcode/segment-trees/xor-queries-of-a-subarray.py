https://leetcode.com/problems/xor-queries-of-a-subarray/

"""
Given the array arr of positive integers and the array queries 
where queries[i] = [Li, Ri], for each query i compute the XOR of 
elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). 
Return an array containing the result for the given queries.
 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if not arr: return []
        n = len(arr)
        
        extra = [0] * (n + 1)
        
        for i in range(n):
            extra[i + 1] = arr[i] ^ extra[i]
        res = []
        for a, b in queries:
            val = extra[b + 1] ^ extra[a]
            res += [val]
        return res
######################################
#segment tree
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if not arr: return 0 
        n = len(arr)
        
        x = (int)(ceil(log2(n)))
        max_size = 2 * (int)(2**x) - 1;
        
        seg = [0] * max_size 
        
        def build(left, right, pos):
            if left == right:
                seg[pos] = arr[left]
                return 
            m = left + (right - left) // 2
            build(left, m, 2 * pos + 1)
            build(m + 1, right, 2 * pos + 2)
            seg[pos] = seg[2 * pos + 1] ^ seg[2 * pos + 2]
        build(0, n - 1, 0)

        
        def query(qleft, qright, left, right, pos):
            if qleft <= left and qright >= right:
                return seg[pos]
            if qleft > right or qright < left:
                return 0
            m = left + (right - left) // 2
            
            return query(qleft, qright, left, m, 2 * pos + 1) ^\
                    query(qleft, qright, m + 1, right, 2 * pos + 2)
          
        res = []
        for a, b in queries:
            ans = query(a, b, 0, n - 1, 0)
            res += [ans]    
        
        return res