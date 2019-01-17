#include<bits/stdc++.h>

using namespace std;
int main(){
    cout<<"Sort by Suraj Pawar"<<endl;
    int i, n=5;
    int arr[n];
    srand(time(0));
    //n = rand();
    for(i=0; i<n; i++)
        arr[i] = rand();
    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    //n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;

    cout<<"Array after sorting:\t";
    //int k = sizeof(arr)/sizeof(arr[0]);
    sort(arr, arr+n);

    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}
