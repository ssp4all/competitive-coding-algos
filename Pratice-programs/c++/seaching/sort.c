#include<stdio.h>
int main(){

int main(){
    cout<<"Sort by Suraj Pawar"<<endl;
    int i, n=15;

    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    int arr[n] = {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5};

    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    sort(arr, 0, n-1);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}

    return 0;
}

