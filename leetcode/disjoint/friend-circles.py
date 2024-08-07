https://leetcode.com/problems/friend-circles/
"""
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct 
friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
"""

# TC: O(n^2), SC:O(n) with path compression of union find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:   return 0
        
        n = len(M)
        ans = 0
        seen = set()
        
        def dfs(i):
            seen.add(i)     
            for j in range(n):
                if M[i][j] == 1 and j not in seen:
                    dfs(j)
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
       
# TC: O(n^2), SC:O(n) with path compression of union find
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        sx, sy = self.size[px], self.size[py]
        
        if px == py:    return 
        
        if sx > sy:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
        self.count -= 1
    
    def counter(self):    return self.count
        
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:   return 0
        
        row, col = len(M), len(M[0])
        uf = UF(row)
        
        for i in range(row):
            for j in range(col):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.counter()