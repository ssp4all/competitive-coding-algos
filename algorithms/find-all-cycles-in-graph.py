
reference: https://www.tutorialspoint.com/print-all-the-cycles-in-an-undirected-graph-in-cplusplus


#program to print all nodes included in the cycle in the given undirected graph 
import collections

edges = [[1, 2], [2, 3], [1, 3], [2, 4], [4, 5], [5, 6], [4, 6]]
n = 6

parent = [0] * (n + 1)
color = [0] * (n + 1)
mark = [0] * (n + 1)
cycleno = 0

graph = collections.defaultdict(set)

for i, j in edges:
    graph[i].add(j)
    graph[j].add(i)

def dfs(u, v):
    global cycleno 

    if color[u] == 2: #node explore complete
        return 
    elif color[u] == 1: #cycle found
        cycleno += 1
        cur = v 
        mark[cur] = cycleno 
        while cur != u:
            cur = parent[cur]
            mark[cur] = cycleno 
    else:
        parent[u] = v 
        color[u] = 1
        for nei in graph[u]:
            if nei == parent[u]:    continue 
            dfs(nei, u)
        color[u] = 2 #exploration for this node completed
    

dfs(1, 0)
print(mark)
