# https://leetcode.com/problems/two-city-scheduling/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key= lambda x:x[0]-x[1])
        return sum(i[0] for i in costs[:n//2]) + sum(i[1] for i in costs[n//2:])
        print(costs)