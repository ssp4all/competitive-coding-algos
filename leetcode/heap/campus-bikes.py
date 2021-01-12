https://leetcode.com/problems/campus-bikes/

"""
On a campus represented as a 2D grid, there are N workers and M bikes, 
with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes 
and workers, we choose the (worker, bike) pair with the shortest 
Manhattan distance between each other, and assign the bike to that worker. 
(If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, 
we choose the pair with the smallest worker index; if there are multiple ways to do that, 
we choose the pair with the smallest bike index). We repeat this process until there are 
no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan
(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) 
of the bike that the i-th worker is assigned to.
"""

#bucket sort
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        dist = [[] for _ in range(2001)]
        
        for i, (x, y) in enumerate(workers):
            for j, (a, b) in enumerate(bikes):
                distance = abs(x - a) + abs(y - b)
                dist[distance] += [(i, j)]
                
        used = set()
        assigned = [-1] * len(workers)
        
        for d in dist:
            for x, y in d:
                if assigned[x] == -1 and y not in used:
                    assigned[x] = y
                    used.add(y)
        return assigned

#heap
def assignBikes(self, workers, bikes):
    distances = []     # distances[worker] is tuple of (distance, worker, bike) for each bike 
    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance
    
    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
    heapq.heapify(queue)
    
    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike
    
    return result