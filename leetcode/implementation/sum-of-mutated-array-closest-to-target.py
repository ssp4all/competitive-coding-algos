https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

"""
Given an integer array arr and a target value target, return the integer value such that when 
we change all the integers larger than value in the given array to be equal to value,
 the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
"""

# TC:O(nlgn), SC:O(1)
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        length = len(arr)
        for i in range(length):
            sol = round(target/length)
            # print(sol)
            if arr[i]>=sol:
                return sol
            target-=arr[i]
            length-=1
        return arr[-1]