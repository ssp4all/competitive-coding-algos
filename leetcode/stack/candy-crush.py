# https://leetcode.com/discuss/interview-question/380650/bloomberg-phone-screen-candy-crush-1d

def candyCrush1D(S):
    stack = ['#']
    for c in S + '#':
        if c != stack[-1][-1] and len(stack[-1]) >= 3:
            stack.pop()
        if c == stack[-1][-1]:
            stack[-1] += c
        else:
            stack.append(c)
    return ''.join(stack[1:-1])
            
from functools import lru_cache
from itertools import groupby
@lru_cache()
def candyCrush1D_followup(S):
    l, segs = 0, []
    for c, seq in groupby(S):
        k = len(list(seq))
        if k >= 3:
            segs.append((l, l + k))
        l += k
    return min([
        candyCrush1D_followup(S[:l] + S[r:]) 
        for l, r in segs
    ], key=len, default=S)
        

S = "aaabbbc"
print(candyCrush1D(S))
print(candyCrush1D_followup(S))

S = "aabbbacd"
print(candyCrush1D(S))
print(candyCrush1D_followup(S))

S = "aaabbbacd"
print(candyCrush1D(S))
print(candyCrush1D_followup(S))