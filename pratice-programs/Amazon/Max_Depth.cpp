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
