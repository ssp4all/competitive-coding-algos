https://leetcode.com/problems/knight-dialer/

"""
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

 

Example 1:

Input: 1
Output: 10
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        dial = {
                    0: [4, 6],
                    1: [6, 8],
                    2: [7, 9],
                    3: [4, 8],
                    4: [0, 3, 9],
                    5: [],
                    6: [0, 1, 7],
                    7: [2, 6],
                    8: [1, 3],
                    9: [2, 4],
                }
        dp = [1] * 10
        
        for i in range(n - 1):
            temp = [0] * 10
            for k in dial.keys():
                temp[k] = sum([dp[j] for j in dial[k]])  % (10 ** 9 + 7)
            dp = temp
        return sum(dp) % (10 ** 9 + 7)