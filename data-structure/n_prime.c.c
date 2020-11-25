#include<stdio.h>
void main()
{
    int i=1,j,c=1;
    while(c<=10)
    {
        for(j=2;j<=i;j++)
        {
            if(i%j == 0)
            {
                break;

            }
        }
            if(i==j)
            {
                printf("\n %d",i);
                c++;
            }


        i++;
    }
}
