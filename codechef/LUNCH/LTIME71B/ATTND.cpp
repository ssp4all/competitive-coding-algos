// Suraj Pawar
// https://www.codechef.com/LTIME71B/problems/ATTND
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
1
4
hasan jaddouh
farhod khakimiyon
kerim kochekov
hasan khateeb
*/
int main(){

    fastio;
	ll t;
	cin>>t;
	while(t--){
		
		ll n;
		vector<string> f;
		vector<string> l;
		cin>>n;
		string fn, ln;
		for(ll i=0; i<n; ++i){
			cin>>fn>>ln;
			f.push_back(fn);
			l.push_back(ln);
		}
		for(ll i=0; i<n; ++i){
			if (count(f.begin(), f.end(), f[i]) > 1)
				cout<<f[i]<<" "<<l[i]<<nl;
			else	cout<<f[i]<<nl;

		}
	}
	return 0;	
}
