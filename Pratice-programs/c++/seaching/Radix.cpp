#include<bits/stdc++.h>
using namespace std;

int digits(int arr[], int n){
    int *k, counter=0;
    //finds no of digits in maximum element in an array
    k = max_element(arr, arr+n);
    //cout<<*k;
    while(*k > 0){
        *k = *k/10;
        counter++;
    }
    return counter;
}
void radix_sort(int arr[], int n){

    int counter, i, remainder, div=1, pass;
    int bucket[10][10], bucket_counter[10];

    counter = digits(arr, n);

    //finds no of digits in maximum element in an array
    //cout<<counter<<endl;
    for(pass=0; pass<counter; pass++){

        for(i=0; i<10; i++)
            bucket_counter[i]= 0;

        for(i=0; i<n; i++){
            remainder = (arr[i]/div)%10;
            bucket[remainder][bucket_counter[remainder]] = arr[i];
            bucket_counter[remainder] += 1;
        }
        //collect all the numbers stored after a pass
        int i=0, k, j;
        for(k=0; k<10 ; k++){
            for(j=0; j<bucket_counter[k]; j++){
                arr[i] = bucket[k][j];
                i++;
            }
        }
        div = div*10;
    }
}
int main(){
    cout<<"Radix-sort by Suraj Pawar"<<endl;
    int i, n;
    //int arr[n] = {3,5,35,7,1,0,8,72,3,2};
    int arr[] = {9,2};
    n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Given array is:\t";
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
    cout<<"Array after sorting:\t";
    radix_sort(arr, n);
    for(i=0; i<n; i++)
        cout<<arr[i]<<"\t";

    return 0;
}

