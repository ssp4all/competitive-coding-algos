#include<bits/stdc++.h>
using namespace std;


void quick_sort(int arr[], int beg, int end){
    int loc;
    if(beg<end){
        loc = partition(arr, beg, end);
        quick_sort(a, beg, loc-1);
        quick_sort(a, loc+1, end);
    }
}
int partition(int arr[], int beg, int end){
    int loc;
    for


    return loc;
}
int main(){
    cout<<"Quick-sort by Suraj Pawar"<<endl;
    int i, n=10;
    int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    //int arr[n] = {1,2,3,5,4};

    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    quick_sort(arr, 0, n-1);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}

