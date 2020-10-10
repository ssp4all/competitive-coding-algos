// Suraj Pawar
// https://www.codechef.com/LTIME70B/problems/TSTROBOT
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
2
6 10
RRLLLL
2 0
LL
*/

int main(){
    fastio;
	ll t;
	cin>>t;
	while(t--){
		ll n, x, ans=0;
		cin>>n>>x;
		string str;
		cin>>str;
		set<ll> a;
		a.insert(x);
		for(ll i=0; i<n; ++i){
			if( str[i] == 'L')
				a.insert(--x);				
			else
				a.insert(++x);				
		}
		cout<<a.size()<<nl;
	}
	return 0;
}
