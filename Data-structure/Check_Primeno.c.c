#include<stdio.h>
void main()
{
    int n,j;
    printf("\n Enter a No.");
    scanf("%d",&n);
    for(j=2;j<=n;j++)
    {
        if(n%j==0)
        {
            break;
        }
    }
        if(n==j)
        {
            printf("\n Entered No. is Prime No ");
        }
        else
        {
            printf("\n Not a Prime NO.");

        }

}
