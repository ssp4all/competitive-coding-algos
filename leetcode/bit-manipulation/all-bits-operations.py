Count numbers of bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        bit = 0
        for i in range(32):
            if n & mask != 0:
                bit += 1
            mask <<= 1
        return bit

Check whether a number is power of two or not
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return 0
        return (n & -n) == n