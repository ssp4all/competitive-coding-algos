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
		char x;
		cin>>n>>s>>x;

		ll ans = 0, t = 0, l;
		ll total_len = n*(n+1)/2;

		ll temp = count(s.begin(), s.end(), x);
		if(temp == n){
			// cout<<"y";
			cout<<total_len<<nl; 
			continue;
		}
		for(ll i = 0; i < n; ++i){  
			++t;
			if(s[i] == x){
				l = ((t-1)*t) / 2;
				ans += l;
				t = 0;
			}	
		}
		if( t > 0){
			l = ((t+1)*t) / 2;
			ans += l;
		}
		ans = (total_len - ans);
		cout<<ans<<nl;
	}
	return 0;
}
