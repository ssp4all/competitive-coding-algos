// Suraj Pawar
// https://www.hackerrank.com/challenges/deque-stl/
#include <bits/stdc++.h>
using namespace std;
#define nl "\n" 
#define ll long long

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

void sliding_window_max(ll arr[], ll n, ll k){
    deque<ll> d;
    ll i;
    for( i = 0; i < k; ++i ){
        while( ( !d.empty() ) and arr[i] >= arr[d.back()])
            d.pop_back();
        d.push_back(i);
    }
    for(; i < n; ++i){
        cout<<arr[d.front()]<<" ";
        while( (!d.empty()) and d.front() <= ( i - k))
            d.pop_front();
        while( (!d.empty()) and arr[i] >= arr[d.back()] )
            d.pop_back();
        d.push_back(i);
    }    
    cout<<arr[d.front()]<<nl;
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll t = scan();
    while(t--){
        ll n, k;
        n = scan(), k = scan();
        // cout<<n<<" "<<k;
        ll arr[n];
        for(ll i=0; i<n; ++i)
            arr[i] = scan();
        sliding_window_max(arr, n, k);
    }
  return 0;
}
