// Suraj Pawar
// https://www.codechef.com/MARCH19A/problems/SUBPRNJL
#include <bits/stdc++.h>
using namespace std;
#define endl "\n" 
#define ll long long
#define loop(i,a,b) for(ll i=a;i<b;i++)


inline int scan(){
    int x = 0;
    char c = getchar_unlocked();
    bool b = 0;
    while ( c < '0' || c > '9'){
        if( c == '-'){
            b = 1;
        }
        c = getchar_unlocked();
    }
    while ( c >= '0' && c <= '9'){
        x = ( x << 3) + ( x << 1) + c - '0';
        c = getchar_unlocked();
    }
    if(b)
        return -x;
        
    return x;
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
	t = scan();
	while(t--){
		ll n, k, ans=0;
		n = scan(), k = scan();
		
		vector<ll>a(n);
		for(ll i=0; i<n; ++i)
			a[i] = scan();

		// for(ll i=0; i<n; ++i)
		// 	cout<<a[i]<<" ";
		// cout<<n<<k;
		loop(l,0,n)
		{
			ll freq[2001]={};
			ll mn = a[l];
			ll mx = a[l];
			loop(r,l,n)
			{
				++freq[a[r]];
				mx = max(mx, a[r]);
				mn = min(mn, a[r]);

				ll size = r-l+1;
				ll m = (k-1)/size + 1;
				// cout<<"m: "<<m,nl;
				ll index = (k-1)/m;
				// cout<<"index: "<<index,nl;
				ll num;
				if( index == 0 )
					num = mn;
				else if( index == size-1 )
					num = mx;
				else
				{
					ll current=0;
					ll rindex = size - index;
					for(ll i=mx; i>=mn; --i)
					{
						current += freq[i];
						if( current >= rindex )
						{
							num = i;
							break;
						}
					}
				}
				if( freq[freq[num]] )
					++ans;
			}
		}
		cout<<ans<<endl;
	}
  return 0;
}
