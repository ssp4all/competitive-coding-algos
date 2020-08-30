#include<stdio.h>

void MergeSort(int [],int,int);
void Merge(int [],int,int,int);

void main()
{
    int n,i;
    int a[500];
    printf("\nEnter No of Elements : ");
    scanf("%d",&n);
    printf("\nEnter %d Array Elements : ",n);
    for(i=0;i<n;i++)
    {
        scanf("\t%d",&a[i]);
    }
    printf("\nEntered  Array Elements are as follow : ");
    for(i=0;i<n;i++)
    {
        printf("%d\t",a[i]);
    }
    MergeSort(a,0,n-1);
    printf("\n Sorted Array List is as follow : ");
    for(i=0;i<n;i++)
    {
        printf("\t%d ",a[i]);
    }
}

void MergeSort(int a[],int i,int j)
{
    int k;
    if(i<j)
    {

        k=(i+j)/2;
        MergeSort(a,i,k);
        MergeSort(a,k+1,j);
        Merge(a,i,k,j);
    }
}

void Merge(int a[],int l,int m,int u)
{
    int c[100],i,j,k;
    i=l;
    j=m+1;
    k=0;
    while(i<=m && j<=u)
    {
        if(a[i]<a[j])
        {
            c[k]=a[i];
            i++;
            k++;
        }
        else
        {
            c[k]=a[j];
            k++;
            j++;
        }
    }
    while(i <= m)
    {
        c[k]=a[i];
        i++;
        k++;
    }
    while(j <= u)
    {
        c[k]=a[j];
        k++;
        j++;
    }
    for(i=l,j=0;i<=u;i++,j++)
    {
        a[i]=c[j];
    }
}



















