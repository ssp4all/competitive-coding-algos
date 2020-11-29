https://leetcode.com/problems/uncrossed-lines/

"""
We write the integers of A and B (in the order they are given) on two 
separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers 
A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each 
number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.


"""
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        cache = {}
        def helper(a, b):
            if (tuple(a), tuple(b)) in cache:
                return cache[(tuple(a), tuple(b))]
            # print(a, b)
            if not a or not b:
                return 0
            f, s = 0, 0
            if a[0] == b[0]:
                f = helper(a[1:], b[1:]) + 1
            else:
                s = max(helper(a, b[1:]), helper(a[1:], b))
            # print(f, s)
            cache[(tuple(a), tuple(b))] = max(f, s)
            return max(f, s)
        return helper(A, B)