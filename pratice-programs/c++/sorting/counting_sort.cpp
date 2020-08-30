#include<bits/stdc++.h>
using namespace std;

void counting_sort(int arr[], int n){
    int i, *k;
    k = max_element(arr, arr+n);
    int size = *k;
    int occ[size]={0}, out[n]={0};
    cout<<endl;
    for(i=0; i<n; i++){
        //count numbet of occurences
        occ[arr[i]]++;
    }
    cout<<endl;
    for(i=1; i<size; i++)
        occ[i] += occ[i-1];

    for(i=size; i>0; i--)
        occ[i] = occ[i-1];
    occ[0] = 0;

    for(i=0; i<n; i++){
        out[occ[arr[i]]] = arr[i];
        occ[arr[i]]++;
    }

    for(i=0; i<n; i++)
        arr[i] = out[i];
    cout<<endl;

}
int main(){
    cout<<"Counting sort by Suraj Pawar"<<endl;
    int i, n;
    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    int arr[] = {1,4,999,0,3,1,3,1,8,5};
    n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    //cout<<"Array after sorting:\t";
    counting_sort(arr, n);

    cout<<"Sorted array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    return 0;
}
