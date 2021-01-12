#include<stdio.h>
void main()
{int n,n1,t,sum=0;
printf("enter a number");
scanf("%d",&n);
n1=n;
while(n>0)
{
t=n%10;
sum=sum+(t*t*t);
n=n/10;
}
if(n1==sum)
printf("armstrong number");
else
printf("not armstorng number");
}
