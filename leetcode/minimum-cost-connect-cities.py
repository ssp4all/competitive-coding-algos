https://www.geeksforgeeks.org/minimum-cost-connect-cities/

Uses prim algorithm to generate mini spanning tree


def find_mini(n, keyval, visited):
    mini = float('inf')
    ind = None 
    for i in range(n):
        if keyval[i] < mini and not visited[i]:
            mini = keyval[i]
            ind = i
    return ind
    # return keyval.index(min(keyval))

def findcost(n, mat):
    if not mat: return 0
    parent = [None]*n
    keyval = [float('inf')] * n 
    visited = [0] * n
    parent[0] = -1
    keyval[0] = 0
    for i in range(n-1):
        u = find_mini(n, keyval, visited)
        visited[u] = 1
        for v in range(n):
            if not visited[v] and 0 < mat[u][v] < keyval[v]:
                keyval[v] = mat[u][v]
                parent[v] = u
    cost = 0
    for i in range(1, n):
        cost += mat[parent[i]][i]
    return cost
n1 = 5
city1 = [[0, 1, 2, 3, 4],  
            [1, 0, 5, 0, 7],  
            [2, 5, 0, 6, 0], 
            [3, 0, 6, 0, 0],  
            [4, 7, 0, 0, 0]]  
x = findcost(n1, city1) 
print(x)