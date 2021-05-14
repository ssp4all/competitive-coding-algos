https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

"""
There are several cards arranged in a row, and 
each card has an associated number of points 
The points are given in the integer array cardPoints.

In one step, you can take one card from the 
beginning or from the end of the row. You have to 
take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, 
return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
"""


#TC:O(N), SC:O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        #use sliding widonw to find lowest sum subarray
        # of length N - k
        
        j = sum_ = 0 # prev pointer, to hold current subarray sum (idx - j + 1)
        low = float('inf') #lowest sum
        
        for idx, ele in enumerate(cardPoints):
            sum_ += ele 
            
            if idx - j + 1 > (n - k):
                sum_ -= cardPoints[j]
                j += 1 
            if idx - j + 1 == (n - k):
                low = min(low, sum_)    
                
        return sum(cardPoints) - low
                