#include<stdio.h>
#define NUMLETS 50

void mergesort(int a[],int i,int j);
void merge(int a[],int l1,int u1,int l2,int u2);

int main()
{
    int a[NUMLETS],n,i;
    printf("Enter no of elements:");
    scanf("%d",&n);

    printf("Enter array elements:");

    for(i=0;i<n;i++)
        scanf("%d",&a[i]);

    mergesort(a,0,n-1);

    printf("\nSorted array is :");
    for(i=0;i<n;i++)
        printf("%d ",a[i]);

    return 0;
}

void mergesort(int a[],int i,int j)
{
    int mid;

    if(i<j)
    {
        mid=(i+j)/2;
        mergesort(a,i,mid);        //left recursion
        mergesort(a,mid+1,j);    //right recursion
        merge(a,i,mid,mid+1,j);    //merging of two sorted sub-arrays
    }
}

void merge(int a[],int l1,int u1,int l2,int u2)
{
    int aux[NUMLETS];    //temporary array used for merging
    int i,j,k;
    i=l1;    //beginning of the first list
    j=l2;    //beginning of the second list
    k=0;

    while(i<=u1 && j<=u2)    //while elements in both lists
    {
        if(a[i]<a[j])
            aux[k++]=a[i++];
        else
            aux[k++]=a[j++];
    }

    while(i<=u1)    //copy remaining elements of the first list
        aux[k++]=a[i++];

    while(j<=u2)    //copy remaining elements of the second list
        aux[k++]=a[j++];

    //Transfer elements from aux[] back to a[]
    for(i=l1,j=0;i<=u2;i++,j++)
        a[i]=aux[j];
}
