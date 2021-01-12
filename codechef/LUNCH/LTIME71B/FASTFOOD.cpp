// Suraj Pawar
// https://www.codechef.com/LTIME71B/problems/FASTFOOD
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define io  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

struct fastio
{
	char s[100000];
	int it, len;
	fastio() {it=len=0;}
	inline char get()
	{
		if (it<len) return s[it++]; it=0;
		len=fread(s, 1, 100000, stdin);
		if (len==0) return EOF; else return s[it++];
	}
	bool notend()
	{
		char c=get();
		while (c==' '||c=='\n') c=get();
		if (it>0) it--;
		return c!=EOF;
	}
}_buff;

#define geti(x) x=getnum()
#define getii(x,y) geti(x),geti(y)
#define getiii(x,y,z) getii(x,y),geti(z)
#define puti(x) putnum(x),putchar(' ')
#define putii(x,y) puti(x),puti(y)
#define putiii(x,y,z) putii(x,y),puti(z)
#define putsi(x) putnum(x),putchar('\n')
#define putsii(x,y) puti(x),putsi(y)
#define putsiii(x,y,z) putii(x,y),putsi(z)

inline ll getnum()
{
	ll r=0; bool ng=0; char c; c=_buff.get();
	while (c!='-'&&(c<'0'||c>'9')) c=_buff.get();
	if (c=='-') ng=1, c=_buff.get();
	while (c>='0'&&c<='9') r=r*10+c-'0', c=_buff.get();
	return ng?-r:r;
}
template <class T> inline void putnum(T x)
{
	if (x<0) putchar('-'), x=-x;
	register short a[20]={}, sz=0;
	while (x) a[sz++]=x%10, x/=10;
	if(sz==0) putchar('0');
	for (int i=sz-1; i>=0; i--) putchar('0'+a[i]);
}

/*
3
3
2 3 2
10 3 4
4
7 5 3 4
2 3 1 3
2
10 1
1 10
*/
int main(){

    io;
	ll t;
	geti(t);
	while(t--){
		
		ll n;
		geti(n);
		ll arr[100005]={0}, brr[100005]={0};
		ll x;
		for(ll i=1; i<=n; ++i)
			geti(x),	arr[i] = arr[i-1] + x;
		
		for(ll i=0; i<n; ++i)
			geti(x),	brr[i] = x;

		for(ll i=n-1; i>=0; --i)
			brr[i] += brr[i+1];

// 		for(ll i=0; i<=n; ++i){
// 			puti(arr[i]);
// 		}
// 		cout<<nl<<nl;

// 		for(ll i=0; i<=n; ++i){
// 			puti(brr[i]);
// 		}
// 		cout<<nl;

		ll ans=-1;
		for(ll i=0; i<=n; ++i){
		  //  cout<<arr[i] + brr[i]<<" ";
			ans = max(ans, (arr[i] + brr[i]));
// 			cout<<nl<<ans;
		}
		putsi(ans);
// 		cout<<ans<<nl;
		
	}
	return 0;	
}
