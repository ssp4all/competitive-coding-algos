
#include<stdio.h>
void main()
{
    int a=10;
    int b=20;
    printf("num before swapping a=%d\n b=%d\n",a,b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("num after swapping a=%d \n b=%d\n",a,b);
}

