https://leetcode.com/problems/candy/

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
"""

# TLE solution 
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        
        n = len(ratings)
        candies = [1] * n
        flag = 1
        while flag:
            flag = 0
            for i in range(n):
                if i + 1 < n and ratings[i] > ratings[i + 1] and \
                        candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    flag = 1
                elif i - 1 >= 0 and ratings[i] > ratings[i - 1] and \
                        candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    flag = 1
        return sum(candies)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        
        n = len(ratings)
        
        left = [1] * n
        right = [1] * n
        candies = 0
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] = right[i + 1] + 1
        for i in range(n):
            candies += max(left[i], right[i])
        return candies