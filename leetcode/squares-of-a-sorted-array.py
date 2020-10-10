https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, ip: List[int]) -> List[int]:
        # op = [i**2 for i in ip]
        # return sorted(op)
        # neg = []
        n = len(ip)
        op = [0]*n
        # xx = 0
        i, j = 0, n-1
        for k in range(n-1, -1, -1):
            if abs(ip[i]) > abs(ip[j]):
                op[k] = ip[i]**2
                i += 1
            else:
                op[k] = ip[j]**2
                j -= 1
        return op
        
class Solution:
    def sortedSquares(self, ip: List[int]) -> List[int]:
        # op = [i**2 for i in ip]
        # return sorted(op)

        n = len(ip)
        xx = 0
        for i in range(n):
            if ip[i] < 0:
                xx += 1
        a, b = xx - 1, xx
        op = []
        while a >= 0 and b < n:
            if ip[b]**2 <= ip[a]**2:
                op.append(ip[b]**2)
                b += 1
            else:
                op.append(ip[a]**2)
                a -= 1
        
        while a >= 0:
            op.append(ip[a]**2)
            a -= 1
            
        while b < n:
            op.append(ip[b]**2)
            b += 1
        return op
                
            
                
        
        