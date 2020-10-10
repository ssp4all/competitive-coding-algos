// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long  

#define io  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
1
3 6
5 7
1 9
2 5
*/
const ll size = 1e5+1;

int main(){
    io;
	ll t;
	cin >> t;
	while (t--){
		ll n, m, ans=0;
		cin >> n >> m;

		vector<ll> con[size], vec;
		// ll vec[size]={0};
		
		// for(ll i=0; i<m; ++i)   con[i].clear();

		ll u, v;
		for (ll i=0; i<n; ++i){
			cin >> u >> v;
			con[u].push_back(v);
		}
		// cout << "r";
		for (ll i=1; i<=m; ++i){
			if (con[i].size() > 0){
				vec.push_back(*max_element(con[i].begin(), con[i].end()));
				
			}	
		}
		sort(vec.begin(), vec.end());
		
		// for (auto e: vec){
		// 	cout << e << nl;
		// }
		ll len = vec.size();
		cout << vec[len-1]+vec[len-2] << nl;

		


	}

    return 0;   
}
