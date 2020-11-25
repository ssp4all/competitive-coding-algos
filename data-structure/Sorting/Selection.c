#include<stdio.h>

void Selection(int [],int);

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
    Selection(a,n);
    printf("\n Sorted Array List is as follow : ");
    for(i=0;i<n;i++)
    {
        printf("\t%d ",a[i]);
    }
}
void Selection(int a[],int n)
{
    int i,j,k,temp;
    for(i=0;i<n;i++)
    {
        k=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[k])
                k=j;
        }
        if(k != j)
        {
            temp=a[i];
            a[i]=a[k];
            a[k]=temp;
        }
    }
}

