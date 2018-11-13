#include<stdio.h>

void bubble(int [],int);

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
    bubble(a,n);
    printf("\n Sorted Array List is as follow : ");
    for(i=0;i<n;i++)
    {
        printf("\t%d ",a[i]);
    }
}
void bubble(int a[],int n)
{
    int i,j,temp;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i;j++)
        {
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
}
