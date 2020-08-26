#include<stdio.h>
void main()
{
    int a=10;
    int b=20;
    int t;
    printf("numbers before swapping a=%d\n b=%d\n",a,b);
    t=a;
    a=b;
    b=t;
    printf("number after swapping a=%d\n b=%d\n",a,b);
}
