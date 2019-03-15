// Suraj Pawar
// Fenwick tree implementation
#include<bits/stdc++.h>
#define endl "\n";
using namespace std;

int get_sum(int bit_tree[], int x){
    ++x;
    int sum=0;
    while(x){
        sum += bit_tree[x];
        x -= x & (-x);
    }
    return sum;
}

void update_tree(int bit_tree[], int n, int i, int val){
    ++i;
    while(i <= n){
        bit_tree[i] += val;
        i += i & (-i);
    }
    for(int i=1; i<=n; i++)
        cout<<bit_tree[i]<<" ";
    cout<<endl;
}
int *construct_bit_tree(int arr[], int n){
    int *bit_tree = new int[n+1];
    // static int bit_tree[n+1];
    memset(bit_tree, 0, sizeof(0)*n);
    for(int i=0; i<n; ++i){
        update_tree(bit_tree, n, i, arr[i]);
    }       
    return bit_tree;
}

int main(){

    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

    int arr[] = {3, 4, 2, 1, 4, 5, 7, 3};
    int n = sizeof(arr)/sizeof(arr[0]);
    for(auto& e: arr)
        cout<<e<<" ";
    cout<<endl;
    // construct tree
    int *bit_tree = construct_bit_tree(arr, n);

    cout<<"Sum: "<<get_sum(bit_tree, 5)<<endl;
    cout<<"Sum between range : "<<get_sum(bit_tree, 5)-get_sum(bit_tree, 8);
    return 0;
}