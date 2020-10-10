// Suraj Pawar
// https://www.codechef.com/JUNE19B/problems/RSIGNS
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long  
#define ull unsigned long long 

#define io  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);	

/*
1
1
*/
const ull mod = 1e9+7;

//Fermat's Little Theroem
ll cal_pow(ll x){
	ll res;
	if (x == 0)	res=1;
	else if (x == 1)	res=2;
	else {
		res = cal_pow(x/2);
		if (x % 2 == 0)	
			res = (res * res) % mod;
		else
			res = (((res*res) % mod) * 2) % mod;
	}
	return res;
}

int main(){
    io;
    ull t;
	cin >> t;
	// cout << mod;
	while (t--){
		ull n, ans;
		cin >> n;
		ans = cal_pow(n-1);
		// cout << ans << nl;
		ans *= 10;
		ans %= mod;
		cout << ans  << nl;
	}

    return 0;   
}
