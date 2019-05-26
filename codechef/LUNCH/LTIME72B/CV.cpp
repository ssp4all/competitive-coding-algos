// Suraj Pawar
// https://www.codechef.com/LTIME72B/problems/CV
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
3
6
bazeci
3
abu
1
o
*/

int main(){

    fastio;
    ll t;
    cin >> t;
    while (t--){
        ll n;
		cin >> n;
		string s;
		cin >> s;
		string v = "aeiou";
		// string cons = "bcdfghjklmnpqrstvwxyz";
		ll ans=0;
		for (ll i=0; i<n-1; ++i){
			if (v.find(s[i]) == string::npos){
				if (v.find(s[i+1]) != string::npos){
					++ans;
				}
			}
		}
		cout << ans << nl;
    }
    return 0;   
}