#include<stdio.h>
void main()
{ int n,t,sum=0;
printf("enter a number");
scanf("%d",&n);
while(n>0)
{
t=n%10;
sum=sum+t;
n=n/10;
}
printf("the sum of a number=%d",sum);

}
