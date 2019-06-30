// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long  
#define ull unsigned long long 

#define io  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);	

/*
3
1 3 3
5 7 2
38657 76322 564
*/


int main(){
    io;
    ull t;
	cin >> t;
	// cout << mod;
	while (t--){
		ll x, y, k, ans;
		cin >> x >> y >> k;
		ans = (x+y)/k;
		if (ans % 2 == 0)	cout << "Chef" << nl;
		else cout << "Paja" << nl;
	}

    return 0;   
}
