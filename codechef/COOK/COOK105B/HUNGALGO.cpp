// Suraj Pawar
// https://www.codechef.com/COOK105B/problems/HUNGALGO
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
	short a[20]={}, sz=0;
	while (x) a[sz++]=x%10, x/=10;
	if(sz==0) putchar('0');
	for (int i=sz-1; i>=0; i--) putchar('0'+a[i]);
}
/*
1
3
0 0 4
3 0 1
0 1 0
*/


int main(){
    io;
    ll t;
    // cin>>t;
	geti(t);
    while (t--){
		ll n;
		// cin>>n;
		geti(n);
		ll mat[n][n], row[n]={0}, col[n]={0};
		
// 		memset(row, -1, sizeof(row));
// 		memset(col, -1, sizeof(col));
		
		for (ll i=0; i<n; ++i)
			for (ll j=0; j<n; ++j)
				geti(mat[i][j]);
				// cin>>mat[i][j];
	
		for (ll i=0; i<n; ++i){
			for (ll j=0; j<n; ++j){
				if (mat[i][j] == 0)	row[i] = 1;
				if (mat[j][i] == 0)	col[i] = 1;
			}
		}

		ll flag = 0;
		for (ll i=0; i<n; ++i)
			if (row[i] == 0 || col[i] == 0)
				flag = 1;
		
		if (flag == 0)	cout<<"YES"<<nl;
		else	cout<<"NO"<<nl;
    }
    return 0;   
}
