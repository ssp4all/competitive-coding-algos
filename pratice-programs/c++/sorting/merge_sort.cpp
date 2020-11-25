#include<iostream>
using namespace std;
int n=15;
void merge(int arr[], int beg, int mid, int end){
    int i=beg, j=mid+1, index=beg, temp[n], k;
    while((i <= mid) && (j <= end)){
        if( arr[i] < arr[j]){
            temp[index] = arr[i];
            i++;
        }
        else{
            temp[index] = arr[j];
            j++;
        }
        index++;
    }
    if(i>mid){
        while(j<=end){
            temp[index] = arr[j];
            j++;
            index++;
        }
    }
    else{
        while(i<=mid){
            temp[index] = arr[i];
            i++;
            index++;
        }
    }
    for(k=beg; k<index; k++)
        arr[k] = temp[k];
 }
void merge_sort(int arr[], int beg, int end){
    int mid;
    if(beg < end){
        mid = (beg+end)/2;
        merge_sort(arr, beg, mid);
        merge_sort(arr, mid+1, end);
        merge(arr, beg, mid, end);
    }
}

int main(){
    cout<<"Merge sort by Suraj Pawar"<<endl;
    int i;

    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    int arr[n] = {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5};

    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    merge_sort(arr, 0, n-1);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}
