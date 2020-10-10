https://leetcode.com/problems/nested-list-weight-sum/

"""
Given a nested list of integers, return the sum 
of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- 
whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
"""

Recursive

ip = [1,[4,[6]]]
ans = 0
def helper(inp, d):
    global ans
    print(inp, d, ans)
    if type(inp) == list:
        for j in inp:
            helper(j, d + 1)
            
    else:
        ans += (d * inp)

for i in ip:
    d = 1
    helper(i, d)
print(ans)


Iterative
from collections import deque
dq = deque(ip)
depth, ans = 1, 0
while dq:
    print(dq)
    n = len(dq)
    for _ in range(n):
        i = dq.popleft()
        if type(i) == int:
            ans += (depth * i)
        else:
            dq += [j for j in i]
    depth += 1
print(ans)