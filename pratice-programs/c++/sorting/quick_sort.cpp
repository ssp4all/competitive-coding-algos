#include<bits/stdc++.h>
using namespace std;

int partition(int arr[], int beg, int end){
    int loc, left, right, flag=0, temp;
    loc = left = beg;
    right = end;
    while(flag != 1){
        while((arr[loc] <= arr[right]) && (loc != right))
            right--;
        if(loc == right)
            flag = 1;
        else if(arr[loc] > arr[right]){
            temp = arr[loc];
            arr[loc] = arr[right];
            arr[right] = temp;
            loc = right;
        }
        if(flag != 1){
            while((arr[loc] >= arr[left]) && (loc != left))
                left++;
            if(loc == left)
                flag = 1;
            else if(arr[loc] < arr[left]){
                temp = arr[loc];
                arr[loc] = arr[left];
                arr[left] = temp;
                loc = left;
            }
        }
    }
    return loc;
}

void quick_sort(int arr[], int beg, int end){
    int loc;
    if(beg < end){
        loc = partition(arr, beg, end);
        quick_sort(arr, beg, loc-1);
        quick_sort(arr, loc+1, end);
    }
}
int main(){
    cout<<"Quick-sort by Suraj Pawar"<<endl;
    int i, n=50;
    int arr[n];
    srand(time(0));
    for(i=0; i<n; i++)
        arr[i] = rand();

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

