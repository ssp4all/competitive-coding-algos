#include<stdio.h>
#include<math.h>
void main()
{
    float a,b,c,x1,x2,d;
    printf("enter coeff. of eq\n");
    scanf("%f%f%f",&a,&b,&c);
    d=(b*b-4*a*c);
    if(d>=0)
   {
    x1=(-b+sqrt(d))/(2*a);
    x2=(-b-sqrt(d))/(2*a);
    printf("roots are x1=%f\t x2=%f",x1,x2);
   }
    else
    printf("roots are invalid\n");

}
