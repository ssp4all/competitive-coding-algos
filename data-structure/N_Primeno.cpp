#include<stdio.h>
#include<conio.h>
void main()
{
  int i=2,j,n;
  clrscr;
  printf("enter a no\n");
  scanf("%d",&n);
  while(i<=n)
 {
	for(j=2;j<=i;j++)
	{	if(i%j!=0)
		j++;
	}

  if(i==j)
  printf("%d\t",i);
  else
  printf(" ");
  i++;
  }
  getch();
}

