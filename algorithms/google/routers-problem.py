"""
Let's define a kind of message called "Broadcast & Shut Down." When a router receives this message,
it broadcasts the same message to all other routers within its wireless range.
Then, that router shuts down, and can no longer send or receive messages.

For example, Router A is at (0, 0); Router B is at (0, 8); Router C is at (0, 17); Router D is at (11, 0).
If the wireless range is 10, when Router A sends a message, it could first reach B;
the message from Router B would further reach Router C but Router D would never receive this message.

Given a list of routers' locations (their names and the corresponding 2D coordinates),
tell me whether a message from Router A can reach Router B.

Write a method / function with appropriate input and output arguments.
"""

requirements - 
- one query for now 
- number of routers (<= 10K - 100K Routers)
- BFS/DFS
- output is boolean if there is code break then we will return exception 
- base condition 


"""
{
'a': [0, 0], 
'b': [0, 8]
} = dictionary 

source, destination = string
range = int
return = bool 
"""

"""
Follow UP:

Let's say we are allowed to change the wireless range of the
routers. (With range still being an integer). What is the minimum
range such that router A can transmit a message to router B ?


a (0, 0) -> b (0, 8) -> c (0, 17)



D (10, 0)
"""

from math  import sqrt
from collections import defaultdict

def get_dist(pointA: list, pointB: list)-> int:
  return math.sqrt((pointB[0] - pointA[0])** 2 + (pointB[1] - pointA[1])** 2)


def is_router_reachable(routers: dict, source: str, destination: str, limit: int)-> bool:
  """ docstring"""

  # build a graph using limit    
  # use source and destination run DFS algorithm 
  # return ans 
  if source == destination: return True 

  graph = defaultdict(list) 
  for routerA, pointA in routers.items():
      for routerB, pointB in routers.items():
        if routerA == routerB:   continue 
        if get_dist(pointA, pointB) <= limit:
          graph[routerA].append(routerB) 
          graph[routerB].append(routerA)
  seen = set()
  return dfs(graph, seen, source, destination)
          
def dfs(graph: dict, seen: set, node: str, dest: str)->bool:
    seen.add(node) 
    for nei in graph[node]:
      if nei == dest: return True
      if nei in seen: continue

      if dfs(graph, seen, nei, dest):
        return True 
    
    return False
"""
N: Vertices, R: Range
Time complexity: O(N**2 + N) DFS: O(N**2)
"""
// Router A is at (0, 0); Router B is at (0, 8); Router C is at (0, 17); Router D is at (11, 0)        
          {
            A: [B]
            B: [A, C]
            C: [B]
            D: []
          }
        
    DFS(A) -> 
    DFS(B)  
    seen: {A, B, C}
    
  