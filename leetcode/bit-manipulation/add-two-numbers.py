class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a and not b: return None
        if not a or not b: return a or b
        ans = (a if not b else self.getSum(a^b, (a&b)<<1))
        return ans


class Solution:
    def getSum(self, a: int, b: int) -> int:
		mask = 0xFFFFFFFF
        while not b == 0:
            carry = a & b
            a = (a^b) & mask
            b = (carry << 1) & mask
        
        if a > 2**31:
            return ~(a^mask)
        
        else:
            return a