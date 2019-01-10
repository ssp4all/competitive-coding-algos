#include<iostream>
using namespace std;


void bubble_sort(int arr[], int n){
    int i, j, temp;
    for(i=0; i<n-1; i++){
        for(j=0; j<n-i-1; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
int main(){
    cout<<"Bubble sort by Suraj Pawar"<<endl;
    int i, n=5;
    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    int arr[n] = {5,4,3,2,1};

    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    bubble_sort(arr, n);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}
