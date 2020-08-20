https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

"""
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means 
flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 
flowers. We only have 5 flowers 
so it is impossible to get the needed bouquets and we return -1.
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay:    return -1
        l, r = float('inf'), 0
        for b in bloomDay:
            l = min(l, b)
            r = max(r, b)
        
        def check(day):
            flower, bouq = 0, 0
            for b in bloomDay:
                if b > day:
                    flower = 0
                else:
                    bouq = (flower + 1) // k
                    flower = (flower + 1) % k
                    
            return bouq >= m
        if len(bloomDay) < m * k:
            return -1
        while l < r:
            mm = l + (r - l) // 2
            if check(mm):
                r = mm
            else:
                l = mm + 1
        return l