#include<iostream>
using namespace std;


void insertion_sort(int arr[], int n){
    int i, j, temp;
    for(i=0; i<n-1; i++){
        temp = arr[i+1];
        j = i;
        while((temp < arr[j]) && j >= 0){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp;
    }
}
int main(){
    cout<<"Insertion sort by Suraj Pawar"<<endl;
    int i, n=10;
    int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    //int arr[n] = {1,2,3,5,4};

    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    insertion_sort(arr, n);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}
