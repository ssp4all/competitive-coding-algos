https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration
 in seconds is divisible by 60.  Formally, we want the number of indices i, j 
 such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
"""

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        n = len(time)
        seen = defaultdict(int)
        for i in range(n):
            num = 60 - (time[i] % 60 if time[i] % 60 != 0 else 60)
            pairs += seen[num]
            seen[time[i] % 60] += 1
        return pairs