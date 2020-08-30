// Suraj Pawar
// https://www.codechef.com/APRIL19B/problems/SUBREM
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long 

#define fastio  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

/*
1
3 5
1 -5 -10
1 2
2 3
*/

ll n, k, z, t;
vector<ll> con[100001];
ll a[100001];

ll dfs(ll x, ll pre){
    ll ret=0, sum=0;
    for (auto e: con[x]){
        if (e == pre)   continue; 
        sum += dfs(e, x);
    }
    ret = max(sum+a[x], -k);
    return ret;
}

int main(){

    fastio;
    cin>>t;
    while(t--){
        
        cin>>n>>k;
        memset(a, 0, sizeof(a));
        for (ll i=1; i<n+1; ++i)  cin>>a[i];
        
        for(ll i=1; i<n+1; ++i)   con[i].clear();
       
        ll u, v;
        for (ll i=1; i<n; ++i){
            cin>>u>>v;
            con[u].push_back(v);
            con[v].push_back(u);
        }
        ll ans = dfs(1, 0);
        cout<<ans<<nl;
    }
    return 0;   
}
