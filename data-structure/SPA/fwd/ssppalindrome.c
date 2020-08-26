#include<stdio.h>
void main()
{
 int n,n1,rev=0,t;
 printf("enter a number");
 scanf("%d",&n);
 n1=n;
 while(n>0)
 {
 t=n%10;
 rev=rev*10+t;
 n=n/10;
 }
 if(rev==n1)
 printf("entered number is palindrome");
 else
 printf("entered number is not palindrome");
}
