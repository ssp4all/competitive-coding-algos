https://leetcode.com/problems/student-attendance-record-ii/

"""
Given a positive integer n, return the number of all possible attendance records with length n, 
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more 
than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 

"""
# TC:O(3^N), SC:O(lg3N) without memo else TC:O(N*2*8) SC:O(N)
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1_000_000_007
    
        @functools.lru_cache(None)
        def rec(index, a_count, last_two):

            if index == n - 1:
                return 1

            e1 = rec(index+1, a_count+1, (last_two+'A')[-2:]) if a_count == 0 else 0
            e2 = rec(index+1, a_count, (last_two+'L')[-2:]) if last_two != 'LL' else 0
            e3 = rec(index+1, a_count, (last_two+'P')[-2:])

            return ( e1 + e2 + e3 ) % MOD

        return ( rec(0, 1, 'A') + rec(0, 0, 'L') + rec(0, 0, 'P') ) % MOD