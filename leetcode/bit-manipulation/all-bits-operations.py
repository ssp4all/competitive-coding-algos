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


Count total 1 bits for all numbers <= n

https://leetcode.com/problems/counting-bits/

def count(no):
    c = 0
    while no:
        c += no & 1
        no >>= 1
    return c

z = count(3)
print(z)

class Solution:
    def countBits(self, num: int) -> List[int]:
        if not num: return [0]
        dp = [0] * (num + 1)
        os = 1
        for i in range(1, num + 1):
            if os*2 == i:
                os *= 2
            dp[i] = dp[i - os] + 1
        return dp

https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            # print(res)
            n >>= 1
        return res