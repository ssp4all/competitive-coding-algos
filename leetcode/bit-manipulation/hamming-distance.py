leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if not x and not y: return 0
        return bin(x^y).count('1')
