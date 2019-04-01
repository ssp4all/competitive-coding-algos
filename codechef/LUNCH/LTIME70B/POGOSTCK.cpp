// Suraj Pawar
// https://www.codechef.com/LTIME70B/problems/POGOSTCK
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
2
5 2
3 6 4 7 2
5 3
3 -5 6 3 10
*/

int main(){
    fastio;
	ll t;
	cin>>t;
	while(t--){
		ll n, k, x, ans=0;
		cin>>n>>k;
		vector<ll> a, op;
		for(ll i=0; i<n; ++i){
			cin>>x;
			a.push_back(x);
		}
		for(ll i=0; i<n; ++i){
			ans = 0;
			for(ll j=i; j<n; j += k){
				ans += a[j];
			}
			op.push_back(ans);
		}
		ll maxi = 0;
		maxi = *max_element(op.begin(), op.end());
		cout<<maxi<<nl;
	}
	return 0;
}
