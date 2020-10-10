// Suraj Pawar
// https://www.codechef.com/APRIL19B/problems/FENCE
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
2
4 4 9
1 4
2 1 
2 2
2 3
3 1
3 3
4 1
4 2
4 3
4 4 1
1 1
*/
int main(){

    fastio;
	ll t;
	cin>>t;
	while(t--){
		ll n, m, k, r, c;
		map<pair <ll, ll>, ll> ma;
		map<pair <ll, ll>, ll>::iterator it;
		cin>>n>>m>>k;
		for(ll i=0; i<k; ++i){
			cin>>r>>c;
			ma[make_pair(r, c)] = 1;
		}
		ll ans = 0;
		for(it = ma.begin(); it != ma.end(); ++it){
			ll i = it->first.first;
			ll j = it->first.second;
				
			if(ma.find(make_pair(i,j)) != ma.end()){
				if(ma.find(make_pair(i,j-1)) == ma.end())	++ans;
				if(ma.find(make_pair(i-1,j)) == ma.end())	++ans;
				if(ma.find(make_pair(i,j+1)) == ma.end())	++ans;
				if(ma.find(make_pair(i+1,j)) == ma.end())	++ans;
			}
		}
		cout<<ans<<nl;
	}
	return 0;	
}
