#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sortIntersect' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY volcanic
#  2. INTEGER_ARRAY nonVolcanic
#
from collections import Counter
def sortIntersect(volcanic, nonVolcanic):
    # Write your code here
    if not volcanic and not nonVolcanic:    return []
    ans = []
    freq_volcanic = Counter(volcanic)
    freq_nonvolcanic = Counter(nonVolcanic)
    # print(freq_volcanic, freq_nonvolcanic)
    for v in freq_volcanic.keys():
        if v in nonVolcanic:
            ans += [v]* min(freq_volcanic[v], freq_nonvolcanic[v])
    
    return sorted(ans, reverse=1)



from collections import defaultdict
def countSentences(wordSet, sentences):
    # ana = []


    # Write your code here
    d = {}
    for w in wordSet:
        w = "".join(sorted(list(w)))
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    res = []
    for s in sentences:
        h = {}
        ans = 1
        for w in s.split():
            w = "".join(sorted(list(w)))
            if w in h and w in d:
                h[w] += 1
            elif w in d:
                h[w] = 1
        
        for k, v in h.items():
            ans *= d[k] ** v
        res += [ans]
    return res

def firstOccurrence(s, x):
    # Write your code here

    if '*' not in x:
        return s.index(x)
    else:
        for i in range(len(s) - len(x)):
            if s[i] == x[0]:
                ctr = 0
                while  (x[ctr] == '*' or s[i + ctr] == x[ctr]):
                    ctr += 1
                    if len(x) == ctr:
                        return i
    return -1

from collections import deque
def segment(x, space):
    # Write your code here
    # n = len(space)
    # # maxi = float('-inf')
    mina = []
    mina += [min(space[:x])]

    for i in range(x, len(space)):
        if space[i] < mina[-1]:
            mina += [space[i]]
        else:
            if mina[-1] == space[i - x]:
                mina += [min(space[i - x + 1:i + 1])]
            else:
                mina += [mina[-1]]
    return max(mina)

dq = deque()
maxi = float('-inf')
for i in range(x):
    while dq and space[i] <= space[dq[-1]]:
        dq.pop()
    dq += [i]
for i in range(x, len(space)):
    maxi = max(maxi, space[dq[0]])
    while dq and dq[0] <= i - x:
        dq.popleft()
    while dq and space[i] <= space[dq[-1]]:
        dq.pop()

    dq += [i]
maxi = max(maxi, space[dq[0]])
return maxi
