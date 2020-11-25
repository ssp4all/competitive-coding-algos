#https://leetcode.com/problems/beautiful-arrangement/

"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation:  

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
"""

#recursive
class Solution:
    def countArrangement(self, N):
        if N <= 0:  return 0
        global count
        
        def helper(cur, seen):
            global count
            if cur > N:
                count += 1
            else:
                for i in range(1, N + 1):
                    if seen[i] == 0 and \
                        (i % cur == 0 or cur % i == 0):
                        seen[i] = 1
                        helper(cur + 1, seen)
                        seen[i] = 0
        seen = [0] * (N + 1)
        count = 0
        helper(1, seen)
        return count

#memo
def arrangements(N):
    cache = {}
    def repeat(i, X):
        if i == 1:
            return i
        key = i, X
        if key in cache:
            return cache[key]
        total = sum(repeat(i - 1, X[:j] + X[j + 1:])
                    for j, x in enumerate(X)
                    if x % i == 0 or i % x == 0)
        cache[key] = total
        return total
    return repeat(N, tuple(range(1, N + 1)))
