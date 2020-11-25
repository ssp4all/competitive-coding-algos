#include<stdio.h>
int main()
{
    int i=1,j,c,n;
    printf("\n Enter a No");
    scanf("%d",&n);
    while(c<=n)
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
                printf("%d\t",i);
                c++;
            }
            else
            {
                printf("");
            }
        
        i++;
    }
return 0 ;
}
