// Suraj Pawar
// https://www.codechef.com/problems/STRMCH
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
14
abacabacabacab
3
*/

vector<int> cal_z_array(string s){
	int n = s.size();
	vector<int> z(n);
	int l=0, r=0;

	for(int i = 1; i < n; ++i){
		if(i <= r)		
			z[i] = min( z[i - l], r-i+1 );
		while(i+z[i] < n && s[z[i]] == s[i+z[i]])
			++z[i];
		if(i+z[i]-1 > r)
			l = i, r = i+z[i]-1;		
	}
	return z;
}

// global
int a[1000001];

int main(){

    fastio;
	int n, k;
	string s;

// 	n = 14;
// 	s = "abacabacabacab";
// 	k = 3;
	cin>>n;
	cin>>s;
	cin>>k;
	// cout<<n<<nl<<s<<nl<<k;

	vector<int> z = cal_z_array(s);
	// for(auto &ele: z)
	// 	cout<<ele<<" ";
	// cout<<nl;
	a[0]++;
	// for(int i=1; i<n; ++i)
	// 	cout<<a[i]<<" ";
	// cout<<nl;

	for(int i=1; i<n; ++i){
		++a[0];
		--a[z[i]];
	}

	// for(int i=0; i<n; ++i)
	// 	cout<<a[i]<<" ";
	// cout<<nl;

	for(int i=1; i<=n; i++){
		a[i] = a[i] + a[i-1];
	}
	// for(int i=0; i<n; ++i)
	// 	cout<<a[i]<<" ";
	// cout<<nl;

	for(int i=n-1; i>=0; --i){
		if(a[i] >= k){
			cout<<i+1<<"\n"<<s.substr(0,i+1)<<"\n";
			return 0;
		}
	}
	cout<<"0\n";
}
