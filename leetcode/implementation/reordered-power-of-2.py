https://leetcode.com/problems/reordered-power-of-2/

"""
Starting with a positive integer N, we reorder the digits 
in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such 
that the resulting number is a power of 2.

Input: 1
Output: true
"""

# Time Complexity: O((lgN)!) * lgN 
# Space: O(lgN)
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))