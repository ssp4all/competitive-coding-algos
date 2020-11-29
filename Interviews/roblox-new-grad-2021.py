#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'efficientJanitor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY weight as parameter.
#

def efficientJanitor(weight):
    # Write your code here
    max_size = 3
    weight.sort()
    trips = 0
    i, j = 0, len(weight) - 1
    while i <= j:
        trips += 1
        if weight[i] + weight[j] <= max_size:
            i += 1
        j -= 1
    return trips


-----------------
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMinDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. INTEGER n
#
from collections import deque 
from itertools import combinations

def findMinDistance(w, h, n):
    grid = []
    for i in range(h):
        for j in range(w):
            grid += [(i, j, 0)]
    ans = float('inf')
    for points in combinations(grid, n):
        dq = deque()
        seen = set()
        for i, j, d in points:
            dq += [(i, j, d)]
            seen.add((i, j))
        
        dist_ans = 0
        while dq:
            m, n, dist = dq.popleft()
            dist_ans = max(dist_ans, dist)
            for ii, jj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = m + ii, n + jj
                if 0 <= ni < h and 0 <= nj < w and \
                    (ni, nj) not in seen:
                    dq += [(ni, nj, dist + 1)]
                    seen.add((ni, nj))
        ans = min(ans, dist_ans)
    return ans

if __name__ == '__main__':

-------------------------
def max_gap(L, v):
        G = [True for _ in range(L+2)]
        for ele in v:
            G[ele] = False
        
        cnt, ret = 0, 0

        for b in G:
            cnt = 1 if b else cnt+1
            ret = max(ret,cnt)
        return ret

    return max_gap(n,h)*max_gap(m,v)
