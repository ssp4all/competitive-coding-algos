#include<iostream>
using namespace std;

int smallest(int arr[], int k, int n){
    int pos = k, small = arr[k], i;
    for(i=k+1; i<n; i++){
        if(arr[i] < small){
            small = arr[i];
            pos = i;
        }
    }
    return pos;
}

void selection_sort(int arr[], int n){
    int i=0, pos, temp;
    for(i=0; i<n; i++){
        pos = smallest(arr, i, n);
        temp = arr[i];
        arr[i] = arr[pos];
        arr[pos] = temp;
    }
}
int main(){
    cout<<"Binary search by Suraj Pawar"<<endl;
    int i, n=10;
    int arr[n] = {3,5,35,7,2,0,2,72,3,2};

    cout<<"Given array is:";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting..";
    selection_sort(arr, n);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    return 0;
}
