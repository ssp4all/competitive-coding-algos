// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define nl "\n"
#define ll long long
#define ull unsigned long long

#define io ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

/*
4 3
1 7 2 4
*/

int main()
{

	io;
	ll n, k, x;
	cin >> n >> k;
	//   vector<ll> v;
	int f[k];

	memset(f, 0, sizeof(f));

	for (ll i = 0; i < n; ++i)
	{
		cin >> x, ++f[x % k];
	}
	if (k % 2 == 0)
		f[k / 2] = min(1, f[k / 2]);
	ll res = min(f[0], 1);

	for (ll i = 1; i <= k / 2; ++i)
	{
		res += max(f[i], f[k - i]);
	}
	cout << res << nl;

	return 0;
}
