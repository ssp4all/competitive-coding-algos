https://leetcode.com/problems/paint-house/

Brute force

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        n = len(costs)
        
        def helper(i, j):
            total = costs[i][j]
            if i == n-1:
                return total
            
            total += min([helper(i+1, k) for k in range(3) if k != j])
            return total
            
        return min([helper(0, j) for j in range(3)])

Memoized Solution

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        n = len(costs)
        cache = dict()
        
        def helper(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            total = costs[i][j]
            if i == n-1:
                return total
            total += min([helper(i+1, k) for k in range(3) if k != j])
            cache[(i, j)] = total
            return total
        return min([helper(0, j) for j in range(3)])
    
Dynamic programming

def minCost(self, costs: List[List[int]]) -> int:    
    for n in reversed(range(len(costs) - 1)):
        costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
        costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
        costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

    if len(costs) == 0: return 0
    return min(costs[0]) 
