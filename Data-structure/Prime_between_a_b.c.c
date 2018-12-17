#include<stdio.h>
void main()
{
    int a,b,i,j;
    printf("\n Enter Lower and Upper Limit : ");
    scanf("%d %d",&a,&b);
    for(i=a;i<=b;i++)
    {
        for(j=2;j<=i;j++)
        {
            if(i%j==0)
            {
                break;
            }

        }
        if(i==j)
        {
            printf("\n%d\t",i);
        }
    }
}
