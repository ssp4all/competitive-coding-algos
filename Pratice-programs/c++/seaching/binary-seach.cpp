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
    int i=0, pos;
    for(i=0; i<n; i++){
        pos = smallest(arr, k, n);
    }

}
int main(){
    cout<<"Binary search by Suraj Pawar"<<endl;
    int arr[10] = {3,5,35,7,2,0,2,72,3,2};
    int i;
    cout<<"Given array is:";
    for(i=0; i<10; i++)
        cout<<arr[i]<<"\t";
    cout<<"Array after sorting.."
    selection_sort(arr, n);
    for(i=0; i<10; i++)
        cout<<arr[i]<<"\t";

}
