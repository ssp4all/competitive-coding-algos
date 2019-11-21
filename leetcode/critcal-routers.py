# Articulation point detection
from collections import defaultdict

class Graph:
	def __init__(self, n):
		self.n = n
		self.graph = defaultdict(set)
		self.time = 0
	
	def addEdge(self, x, y):
		self.graph[x].add(y)
		self.graph[y].add(x)



	def explore(self, u, visited, parent, disc, low, ap):
		visited[u] = 1
		# print(u)
		child = 0
		
		disc[u] = self.time
		low[u] = self.time
		
		self.time += 1

		for v in self.graph[u]:
			if visited[v] == 0:
				child += 1
				parent[v] = u

				self.explore(v, visited, parent, disc, low, ap)
				
				low[u] = min(low[u], disc[v])
				
				if parent[u] == -1 and child > 1:
					ap[u] = 1
				if parent[u] != -1 and low[v] >= disc[u]:
					ap[u]= 1
			elif v != parent[u]:
				low[u] = min(low[u], disc[v])

				

	def dfs(self):
		visited = [0]*self.n
		parent = [-1]*self.n
		disc = [-1]*self.n
		low = [-1]*self.n
		ap = [0]*self.n
		
		for u in range(self.n):
			if visited[u] == 0:
				self.explore(u, visited, parent, disc, low, ap)
		for i, v in enumerate(ap):
			if v == 1: print(i)

if __name__ == "__main__":
	n = 4
	
	g1 = Graph(5) 
	g1.addEdge(1, 0) 
	g1.addEdge(0, 2) 
	g1.addEdge(2, 1) 
	g1.addEdge(0, 3) 
	g1.addEdge(3, 4) 

	g1.dfs()