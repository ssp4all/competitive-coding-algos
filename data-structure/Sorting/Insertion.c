#include<stdio.h>

void Insertion(int [],int);

void main()
{
    int n,i;
    int a[5];
    printf("Enter No of Elements : ");
    scanf("%d",&n);
    printf("Enter %d Array Elements : ",n);
    for(i=0;i<n;i++)
    {
        scanf("\t%d",&a[i]);
    }
    printf("\nEntered  Array Elements are as follow : ");
    for(i=0;i<n;i++)
    {
        printf("%d\t",a[i]);
    }

    Insertion(a,n);
    printf("\n Sorted Array List is as follow : ");
    for(i=0;i<n;i++)
    {
        printf("\t%d ",a[i]);
    }

}

void Insertion(int a[],int n)
{
    int i,j,temp;
    for(i=0;i<n;i++)
    {
        temp=a[i];
        for(j=i-1;j>=0 && a[j]>temp ;j--)
        {
            a[j+1]=a[j];
        }
       // a[j+1]=temp;
    }

}
