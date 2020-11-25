#include<stdio.h>

void Quick(int [],int,int);
int partition(int [],int,int);

void main()
{
    int n,i;
    int a[5];
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
    Quick(a,0,n-1);
    printf("\n Sorted Array List is as follow : ");
    for(i=0;i<n;i++)
    {
        printf("\t%d ",a[i]);
    }
}

void Quick(int a[],int l,int u)
{
    int j;
    if(l<u)
    {
        j=Partition(a,l,u);
        Quick(a,l,j-1);
        Quick(a,j+1,u);
    }
}

int Partition(int a[],int l,int u)
{
    int v,i,j,temp;
    v=a[l];
    i=l;
    j=u+1;
    do
    {
        do
        {
            i++;

        }while(a[i]<v && i<=u);
        do
        {
            j--;

        }while(v<a[j]);
        if(i<j)
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }


    }while(i<j);

    a[l]=a[j];
    a[j]=v;
    return j;
}


















