// Suraj Pawar
// https://www.codechef.com/JUNE19B/problems/PROXYC
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
/*
1
9
PAAPPAPPP
*/

int main()	{
    fastio;
    ll t;
    cin >> t;
	while (t--){
		ll n;
		string str;
		cin >> n >> str;

		ll p=0, ans=0;
		for (ll i=0; i<n; ++i)
			if (str[i] == 'P')	++p;

		// cout << p << nl;

		if (p*100/n >= 75){
			cout << ans << nl;
			continue;
		}
		for (ll i=2; i<n-2; ++i){
			if (str[i] == 'A'){
				if ((str[i-1] == 'P' or str[i-2] == 'P') and 
					(str[i+1] == 'P' or str[i+2] == 'P'))
					++ans;
			}
			if ((p+ans)*100/n >= 75)	break;
		}
		// cout << ans << nl;
		// cout << float((p+ans)/n) << nl;


		if ( ((p+ans)*100/n) >= 75)	
			cout << ans << nl;
		else	
			cout << "-1" << nl;

	}

    return 0;   
}
