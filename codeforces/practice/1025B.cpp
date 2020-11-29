// Suraj Pawar
// https://codeforces.com/contest/1025/problem/B
#include <bits/stdc++.h>
using namespace std;
 
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define nl "\n"
#define int long long

const int N=2e5+5;

int z;
int m[N], n[N];

void do_it_for(int k)
{
	for(int i=2;i<=z;i++)
	{
		if(m[i]%k==0 || n[i]%k==0)
			continue;
		return;
	}
	cout<<k;
	exit(0);
}

void fact(int k)
{
	vector<int> v;
	for(int i=2;i*i<=k;i++)
	{
		int ct=0;
		while(k%i==0)
		{
			k/=i;
			ct++;
		}
		if(ct>0)
			v.push_back(i);
	}
	if(k>1)
		v.push_back(k);
	for(auto &it:v)
		do_it_for(it);
}

int32_t main()
{
	IOS;
	cin>>z;
	for(int i=1;i<=z;i++)
		cin>>m[i]>>n[i];
	fact(m[1]);
	fact(n[1]);
	cout<<"-1";
	return 0;
}