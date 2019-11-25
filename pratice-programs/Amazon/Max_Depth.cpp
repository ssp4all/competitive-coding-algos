// Suraj Pawar
// https://www.hackerearth.com/challenges/competitive/amazon-all-india-campus-programming-challenge-dry-run/algorithm/level-devil-4217c612-ac8e882d/
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
/*
6 3
1 5 7 8 6 10
1 2
1 3
2 4
2 5
3 6
1 6
2 7
6 2
*/

const ll no = 2e5+1;
ll a[no];
vector<ll> con[no];
ll max_depth;
set<ll> level[no];
bool vis[no];

void dfs(ll x, ll depth){
	
	vis[x] = true;
	level[depth].insert(a[x]);
	cout << "depth :" << depth << nl;

	max_depth = max(max_depth, depth);

	for (ll i=0; i<con[x].size(); ++i){
		if ( vis[con[x][i]] == false)
			dfs(con[x][i], depth+1);	
	}

}

int main(){
	// cout << no << nl;
    fastio;
    ll n, q;
    cin >> n >> q;

	for (ll i=1; i<=n; ++i)
		cin >> a[i];
	
	// for (ll i=1; i<=n; ++i)
	// 	cout << a[i];
	// cout << nl;

	ll u, v;
	for (ll i=0; i<n-1; ++i){
		cin >> u >> v;
		con[u].push_back(v);
		con[v].push_back(u);
	} 

	// for (ll i=1; i<10; ++i){
	// 	for (ll j=0; j<con[i].size(); ++j){
	// 		cout << con[i][j] << " ";
	// 	}	
	// 	cout << nl;
	// }
	
	memset(vis, false, sizeof(vis));
	max_depth = 0;
	dfs(1, 0);
	
	cout << "level" << nl;
	for (ll i=0; i<10; ++i){
		for (auto ele: level[i]){
			cout << ele << " ";
		}	
		cout << nl;
	}
	cout << "max :" << max_depth << nl;

	ll mod = max_depth + 1;
	// for (auto it: level)
	// 	cout << *it << " ";
	
	while(q--){
		ll l, x;
		cin >> l >> x;
		l %= mod;
		// auto it = lower_bound(level[l].begin(), level[l].end(), x);
		auto it = level[l].lower_bound(x);
		if (it == level[l].end())	cout << "-1" << nl;
		else cout << *it << nl;
		
	}
	
    return 0;   
}
/* python */
from collections import defaultdict
class Graph:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n

	def addEdge(self, x, y):
		self.graph[x].append(y)
		# self.graph[y].append(x)

	def explore(self, u, visited, depth, level):
		global MD
		visited[u] = 1
		level[depth].add(u)
		MD = max(MD, depth)
		print(u, level)
		for v in self.graph[u]:
			if visited[v] == 0:
				self.explore(v, visited, depth+1, level)



	def dfs(self, s, depth):
		visited = [0]*n
		level = [set() for _ in range(self.n)]
		if visited[s] == 0:
			self.explore(s, visited, depth, level)
		print(level)
		print(MD)
	
if __name__ == "__main__":
	MD = 0
	n = 4
	g = Graph(4)
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(1, 2) 
	g.addEdge(2, 0) 
	g.addEdge(2, 3) 
	g.addEdge(3, 3)
	print(g.graph)
	g.dfs(0, 0)
