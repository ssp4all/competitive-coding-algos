#include<stdio.h>
void main()
{
int n,rev=0,t;
printf("enter a number");
scanf("%d",&n);
while(n>0)
{
t=n%10;
rev=rev*10+t;
n=n/10;
}
printf("reverse is=%d",rev);
}
