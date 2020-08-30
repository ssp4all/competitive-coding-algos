#include<stdio.h>
void main()
{
int n,t,small,large,a;
printf("enter a no");
scanf("%d",&n);
small=n%10;
large=n%10;
while(n>0)
{
t=n%10;
if(small<t)
small=t;
{
if(large<t)
large=t;
}
n=n/10;
a=large-small;
printf("the difference is=%d",a);
}
}
