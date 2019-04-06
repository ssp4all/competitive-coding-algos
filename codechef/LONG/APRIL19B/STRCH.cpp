// Suraj Pawar
// https://www.codechef.com/APRIL19B/problems/STRCH
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
2
3
abb b
6
abcabc c
*/

int main(){

    fastio;
	ll t;
	cin>>t;
	while(t--){
		ll n;
		string s;
		char a;
		cin>>n>>s>>a;
		ll c = 0;
		for (ll i = 0; i < n; ++i){  
     	   for (ll len = 1; len <= n - i; ++len){
				// cout << s.substr(i, len) << endl;
				string sub = s.substr(i, len);
				if(sub.find(a) != string::npos)
					++c;
			}
		}
	cout<<c<<nl;
	}
	return 0;
}
