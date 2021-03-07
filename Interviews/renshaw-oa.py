https://leetcode.com/discuss/interview-question/428228/Audible-or-OA-2019-or-Team-Formation
"""
Renshaw OA 2021

Temp formation
"""
from heapq import heappop, heappush

def find_ans(scores, teamSize, k):
    if len(scores) < teamSize:  return 0
    n = len(scores)
    heapLeft = [] 
    heapRight = [] 
    """
    k = 3 
    n = 7 
    size = 2
    """
    
    for i in range(k):
        heappush(heapLeft, (-scores[i], i))
    
    left = max(k, n - k)
    for i in range(left, n):
        heappush(heapRight, (-scores[i], i))
    
    leftPtr, rightPtr = k, left - 1

    ans = []

    while (heapLeft or heapRight):
        # print(ans, heapLeft, heapRight)

        if len(ans) == teamSize:
            return sum(ans)
        
        if heapLeft and not heapRight:
            t1, idx = heappop(heapLeft)
            t1 *= -1 
            ans += [t1]
            if leftPtr <= rightPtr:
                heappush(heapLeft, (-scores[leftPtr], idx))
                leftPtr += 1

        
        elif not heapLeft and heapRight:
            t2, idx = heappop(heapRight)
            t2 *= -1 
            ans += [t2]
            if leftPtr <= rightPtr:
                heappush(heapRight, (-scores[rightPtr], idx))
                rightPtr -= 1

        else:
            if -heapLeft[0][0] >= -heapRight[0][0]:
                t1, idx = heappop(heapLeft)
                t1 *= -1 
                ans += [t1]
                if leftPtr <= rightPtr:
                    heappush(heapLeft, (-scores[leftPtr], idx))
                    leftPtr += 1  
            else:
                t2, idx = heappop(heapRight)
                t2 *= -1 
                ans += [t2]
                if leftPtr <= rightPtr:
                    heappush(heapRight, (-scores[rightPtr], idx))
                    rightPtr -= 1

    return sum(ans)

score = []
teamSize = 5
k = 1
ans = find_ans(score, teamSize, k) 
print(ans)  
