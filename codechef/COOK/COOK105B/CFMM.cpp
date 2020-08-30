// Suraj Pawar
// https://www.codechef.com/COOK105B/problems/CFMM
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
1
6
cplusplus
oscar
deck
fee
hat
near
*/
int main(){

    fastio;
    ll t;
    cin>>t;
    while(t--){
        ll n;
		cin>>n;
		string t, s = "";
		while(n--){
			cin>>t;
			s += t;
		}
		string org = "ceodhf";
// 		cout<<s<<nl;
		vector<ll> count_char;
		for (ll i=0; i<6; ++i){
			ll c = count(s.begin(), s.end(), org[i]);
			count_char.push_back(c);
		}
		// cout<<count_char.size();
		ll ans = 0;
		// for (ll i=0; i<6; ++i)
		// 	cout<<count_char[i]<< " ";
		ll l = s.size();
		ll i;
		while ( l > 7 ){
			ll temp = 0;
			for (i=0; i<6; ++i){
				if (count_char[i]<1)    break;
				if ((i == 0 || i == 1) && count_char[i] >= 2)
					count_char[i] -= 2, temp += 2;
				else if ( (i == 2 || i == 3 || i == 4 || i == 5) && count_char[i] >= 1)
					count_char[i] -= 1, ++temp;
				if (temp == 8)	
					++ans, temp=0;
			}
			// for (auto e: count_char)
			// 	cout<<e<<" ";
			// cout<<nl;
			// cout<<"ans: "<<ans<<nl;
			
			if (i == 6)	l -= 8;
			else break;
		}
		cout<<ans<<nl;

	}
    return 0;   
}
