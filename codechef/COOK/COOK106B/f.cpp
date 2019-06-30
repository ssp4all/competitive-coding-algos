// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long  

#define io  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
3
6
ABCDAB
ABCDAB
8
DDCABCCA
DNCBBBBA
3
CDD
NDC
*/

int main(){
    io;
	ll t;
	cin >> t;
	while (t--){
		ll n, ans=0;
		string s, u;
		cin >> n >> s >> u;

		for (ll i=0;i<n;){
			if (s[i] == u[i])	++ans, ++i;
			else if (u[i] == 'N')	++i;
			else	i += 2;
		}

		cout << ans << nl;
	}

    return 0;   
}
