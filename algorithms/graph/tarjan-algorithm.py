# https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
# tarjan algorithm to find strongly connected components in the given directed graph


edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]

# build graph
n = 5
graph = {i: set() for i in range(n)} 
for i, j in edges:
    graph[i].add(j)

# tarjans algorithm
def dfs(u, disc, low, stack, stack_member):
    # print("node", u, disc, low)
    global time
    
    disc[u] = time
    low[u] = time  
    time += 1
    stack += [u]
    stack_member[u] = 1
    for v in graph[u]:
        if disc[v] == -1:
            dfs(v, disc, low, stack, stack_member)
            low[u] = min(low[u], low[v])

        elif stack_member[v] == 1:
            low[u] = min(low[u], disc[v])
    w = -1 
    if low[u] == disc[u]:
        while w != u and stack:
            w = stack.pop() 
            stack_member[w] = 0
            print(w) 
        print()


def tarjan_algorithm():
    global time
    disc, low = [-1] * n, [-1] * n 
    stack_member = [0] * n 
    stack = []
    time = 0
    # print(graph, disc, low)
    for i in range(n):
        if disc[i] == -1:
            dfs(i, disc, low, stack, stack_member)



tarjan_algorithm()