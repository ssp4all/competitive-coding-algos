// Suraj Pawar
// https://www.codechef.com/APRIL19B/problems/MAXREM
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 
/*
6  
5 5 5 2 3 8
*/
#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    fastio;
	ll n, x;
	set<ll> s;
	cin>>n;
	for(ll i=0; i<n; ++i){
		cin>>x;
		s.insert(x);
	}
	vector<ll> v(s.begin(), s.end());
	ll size = v.size();
	if (size == 1)
		cout<<"0"<<nl;
	else
		cout<<v[size-2]<<nl;

	return 0;
}
