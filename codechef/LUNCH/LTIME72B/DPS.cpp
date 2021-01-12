// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define nl "\n"
#define ll long long
#define ull unsigned long long

#define io ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

/*
4
code
xyxyxy
sad
baab
*/

int main() {

	io;
	ll t, x, l, r;
	cin >> t;
	while(t--){

		string s;
		cin >> s;
		ll n = s.length();
		if (n == 1){	
			cout << "!DPS" << nl;
			continue;
		}
		ll arr[26]={0};
		memset(arr, 0, sizeof(arr));

		for (ll i=0; i<n; ++i)
			++arr[s[i]-97];
		// for (ll i=0; i<26; ++i)
		// 	cout << arr[i] << " ";
		// cout<<nl;

		ll odd=0;
		for (ll i=0; i<26; ++i)
			// cout << arr[i] << " ";
			if (arr[i] % 2 != 0)	++odd;
		
		// cout<<nl;
		// cout << odd <<nl;
		// cout << even << nl;

		if (odd > 0 and odd < 4)			
			cout << "DPS" << nl;
		else cout << "!DPS" << nl;
		
		
	}
	
  return 0;
}
