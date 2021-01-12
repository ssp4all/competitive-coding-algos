from collections import defaultdict, deque
class TP:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n
	
	def addEdge(self, x, y):
		self.graph[x].append(y)
	
	def exp(self, v, visited, stack):
		visited[v] = 1
		for x in self.graph[v]:
			if visited[x] == 0:
				self.exp(x, visited, stack)
		# stack.insert(0, v)
		stack.append(v)
		print(stack)

	def dfs(self):
		visited = [0]*self.n
		stack = []
		for v in range(self.n):
			if visited[v] == 0:
				self.exp(v, visited, stack)
		print(stack[::-1])

"""
Kanh's algorithm
"""
class TP:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n
	
	def addEdge(self, x, y):
		self.graph[x].append(y)
	
	def topo(self):
		indegree = {i:0 for i in self.n}

		for i in range(self.n):
			for j in self.graph[i]:
				indegree[i] += 1
		ans = []
		que = deque([i for i in self.n if indegree[i] == 0])
		cnt = 0
		while que:
			x = que.popleft()
			ans.append(x)
			for i in self.graph[x]:
				indegree[i] -= 1
				if indegree[i] == 0:
					que.append(i)

			cnt += 1

		return ans * (cnt == self.n)

if __name__ == '__main__':
	n = 6
	g = TP(n)
	g.addEdge(5, 2); 
	g.addEdge(5, 0); 
	g.addEdge(4, 0); 
	g.addEdge(4, 1); 
	g.addEdge(2, 3); 
	g.addEdge(3, 1); 
	g.dfs()