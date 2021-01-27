#include<stdio.h>
int main()
{
    int a=10;
    int b=20;
    printf("num before swapping a=%d b=%d",a,b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("num after swapping a=%d \n b=%d\n",a,b);
}


