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

//merge sort approach
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <map>
using namespace std;

#define vit vector<int>
#define vst vector<string>
#define loop(i,n) for(int i = 0;i < n; i++)
#define loopi(i,a,n) for(int i = a;i <= n; i++)
#define pb push_back
#define mp make_pair
typedef long long ll;

ll ans;
ll a[4000005];
ll c[2000001];
int s;
void sort(ll a[], ll low, ll high, ll mid) 
{
    ++s;
    ll i = low;
    ll j = mid + 1;
    ll k = low;
    for (; i <= mid && j <= high;) {
        if (a[i] <= a[j]) {
            c[k] = a[i];
            ans += high - j + 1;
            cout<<"ans "<<ans<<endl;
            k++;
            i++;
        }
        else {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    for (; i <= mid;) {
        c[k] = a[i];
        k++;
        i++;
    }
    for (; j <= high;) {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i <= high; i++)
        a[i] = c[i];
}

void merge(ll a[], ll low, ll high) {

    ll mid;
    if (low < high) {
        mid = (low + high) / 2;
        cout<<low<<" "<<high<<" "<<mid<<endl;
        merge(a, low, mid);
        cout<<'r'<<endl;
        cout<<mid+1<<" "<<high<<endl;
        merge(a, mid + 1, high);
        cout<<'d'<<endl;

        sort(a, low, high, mid);
    }

}

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    ll n, k;
    cin >> n >> k;
    ans = 0;
    ll i;
    for (i = 1; i <= n; i++)
    {
        cin>>a[i];
        a[i] -= k;
        a[i] += a[i - 1];
        cout<<a[i]<<" ";
    }
    cout<<endl;
    merge(a, 0, n);
    for (i = 0; i < n; i++)
        cout<<a[i]<<" ";

    cout<<endl;
    cout << ans<<" "<<s;
    return 0;
}
