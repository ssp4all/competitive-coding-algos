// Suraj Pawar
// https://www.codechef.com/problems/SUBARR
// 4 2
// 1 2 3 -1
#include<bits/stdc++.h>
using namespace std;
#define endl "\n" 
#define lld long long int 

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

const int N = 1e6 + 1;
int n, k, bit[N], newarr[N], current = 0;
lld ans = 0, sum[N];
pair < lld, int> arr[N];

void modify(int i){
    while( i <= current){
        ++bit[i];
        i += i & -i;
    }
}

int get_sum(int i){
    int result = 0;
    while(i){
        result += bit[i];
        i -= i & -i;
    }
    return result;
}
int main(){

    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    sum[0] = 0;
    n = scan(), k = scan();
    for(int i = 1; i <= n; ++i){
        sum[i] = sum[i-1] + scan() - k;
        arr[i] = make_pair(sum[i], i);
        ans += ( sum[i] >= 0 );
    }
    sort( arr + 1, arr + n + 1 );
    arr[0].first = LLONG_MIN;
    for( int i = 1; i <= n; ++i){
        current += (arr[i].first != arr[i -1].first);
        newarr[ arr[i].second ] = current;
    }
    for( int i = 1; i <= n; ++i){
        ans += get_sum(newarr[i]);
        modify(newarr[i]);
    }
    cout<<ans<<endl;
    return 0;
}