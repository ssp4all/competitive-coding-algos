#include<stdio.h>
void main()
{
    char g;
float b;
printf("enter your gender(m or f)=");
scanf("%c",&g);
printf("enter balance=");
scanf("%f",&b);
if(g =='f')
{
    if(b>5000)
        printf("new balance=%f",(b+b*0.05));
    else
        printf("new balance=%f",(b+b*0.02));

}
else
{
     if(b>7000)
        printf("new balance=%f",(b+b*0.07));
     else
        printf("new balance=%f",(b+b*0.05));
}


}
