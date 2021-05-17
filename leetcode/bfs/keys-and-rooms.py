https://leetcode.com/problems/keys-and-rooms/

"""
There are N rooms and you start in room 0.  Each room has a 
distinct number in 0, 1, 2, ..., N-1, and each room may 
have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each 
key rooms[i][j] is an integer in [0, 1, ..., N-1] where 
N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        n = len(rooms)
        dq = deque([0])
        remain = n - 1
        seen = set()
    
        while dq:
            room = dq.popleft()
            if room in seen:    continue 
            if remain == 0:  return 1
            seen.add(room)
            remain -= 1
            dq += [*rooms[room]]
        
        return 0

# TC:O(N+E), SC:O(N)
class Solution:
    def canVisitAllRooms(self, rooms):
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms): return True
        return len(seen) == len(rooms)