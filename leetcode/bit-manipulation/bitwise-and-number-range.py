Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        def find_msb(a):
            pos = -1
            while a > 0:
                a >>= 1
                pos += 1
            return pos
        
        while m > 0 and n > 0:
            msbm = find_msb(m)
            msbn = find_msb(n)

            if msbm != msbn:
                break
            
            temp = 1 << msbm
            res += temp
            
            m -= temp
            n -= temp
            
        return res