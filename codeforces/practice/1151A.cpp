// Suraj Pawar
// https://codeforces.com/contest/1151/problem/A
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
4
ZCTH
*/
int main(){

    fastio;
    ll n;
	string s;
    cin>>n>>s;
	string org = "ACTG";
	ll ans = 999999;	
	for (ll i=0; i<n-3; ++i){
		ll cost = 0;
		for (ll j=0; j<4; ++j){
			// cout<<"org: "<<org[j]<<" "<<"string: "<<s[i+j]<<nl;
			ll t = (org[j] - s[i+j]);
			cost += min(abs(t), t+26);
			// cout<<cost<<nl;
		}	
			
		ans = min(ans, cost);	
	}
	cout<<ans;
    return 0;   
}
