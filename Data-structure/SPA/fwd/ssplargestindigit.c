#include<stdio.h>
void main()
{
int n,t,large;
printf("enter a number");
scanf("%d",&n);
large=n%10;
while(n>0)
{
    t=n%10;
if(t>large)
large=t;
n=n/10;
}
printf("largest digit is =%d",large);
}
