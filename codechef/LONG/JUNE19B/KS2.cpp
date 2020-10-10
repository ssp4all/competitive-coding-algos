// Suraj Pawar
// https://www.codechef.com/JUNE19B/problems/KS2
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long  
#define ull unsigned long long 


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
1
2
*/

int main(){
    io;
    ll t;
	geti(t);
    // cin >> t;
	while (t--){
		ull n;
		geti(n);
		// cin >> n;
		ull no_digits = log10(n)+1;
		// cout << no_digits;
		
		ull sum=0;
		for (ull x=n; x>0; x/=10)
			sum += x%10;
		// cout << sum << nl;
		ull add=sum;
		while (add%10 != 0)
			++add;
		
		// cout << add << nl;
		n = 10*n + (add-sum);
		putsi(n);
		// cout << n << nl;
	}

    return 0;   
}
