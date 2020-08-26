#include<stdio.h>
void main()
{clrscr();
int a,b,c;
printf("enter three numbers=");
scanf("%d%d%d",&a,&b,&c);
printf("\n the greatest number is=%d",(a>b)?((a>c)?a:c):(b>c)?b:c);
getch();
}
