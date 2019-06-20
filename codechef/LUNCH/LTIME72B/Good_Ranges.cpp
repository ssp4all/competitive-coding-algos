// Suraj Pawar
// https://www.hackerearth.com/challenges/competitive/amazon-all-india-campus-programming-challenge-dry-run/algorithm/the-good-ranges-1456e1a2-e908a292/
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*

*/
int main(){

    fastio;
    ll t, n;
    cin >> n >> t;
    set<ll> s;
	ll ans=0;
	while(t--){
		ll x;
		cin >> x;
		if (s.find(x) == s.end()){

			auto it = s.upper_bound(x);
			if (s.size() == 0)
				ans += 1 + n;
			else if( it == s.end())
				ans += *(--it) + x; 
			else if (it == s.begin())
				ans += x + *it;			
			else 
				ans += 2*x;
			cout << ans << nl;
		}
		else
			cout << ans << nl;
		
		s.insert(x);        
    }
    return 0;   
}
