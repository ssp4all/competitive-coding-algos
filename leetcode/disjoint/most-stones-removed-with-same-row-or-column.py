https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


"""
On a 2D plane, we place n stones at some integer coordinate points. 
Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same 
column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents 
the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
"""

from collections import defaultdict

# O(n)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        dsu = DSU(n)
        col, row = defaultdict(int), defaultdict(int)
        
        for i in range(n):
            x, y = stones[i]
            
            if x not in col:
                col[x] = i 
                
            if y not in row:
                row[y] = i 
            
            dsu.join(col[x], i)
            dsu.join(row[y], i)
            
        return n - dsu.count
        
        
class DSU:
    #O(n)
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.count = n 
    
    #O(1)
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    #O(1)
    def join(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:    return 
        self.count -= 1
        self.p[px] = py 
    
    