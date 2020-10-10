#include<stdio.h>
void main()
{
int n,t,small;
printf("enter a number");
scanf("%d",&n);
small=n%10;
while(n>0)
{
    t=n%10;
if(t<small)
small=t;
n=n/10;
}
printf("smallest digit is =%d",small);
}
