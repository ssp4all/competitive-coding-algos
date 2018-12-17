

#include<stdio.h>

void push(char);
void display();
char pop();
void peek();
int top=-1;
char stack[5];

void main()
{
	char ch;
	int n,i;

       do
       {
			printf("\n***********MENU*************\n");
			printf("\n\n1.push\n2.pop\n3.peek\n4.display\n5.stop\n");
            printf("\n Enter Your Choice : ");
			scanf("%d",&n);

			switch(n)
			{
			case 1:
        			printf("\nenter a char to push : ");
                    fflush(stdin);
                    scanf("%c",&ch);
                    push(ch);
                    display();
                    break;

			case 2:
                    pop();
                    display();
                    break;


			case 3:
                    peek();
                    display();
                    break;

			case 4:
                    display();
                    break;

			default:
                    printf("Invalid input\n ");
                    break;
		   }

	  }while(n !=5);


}
void push(char ch)
{
	if(top==4)
	{
		printf("Stack is full\n");
	}
	else
	{
		top++;
		stack[top]=ch;
	}
}
void display()
{
	int i;
	printf("Stack =\n");
	for(i=top;i>=0;i--)
	{

		printf("        %c\n",stack[i]);
	}
}
char pop()
{
	if(top==-1)
		{
		printf("stack is underflow\n");
		return NULL ;
		}
	else

		{
		return stack[top--];
		}
}
void peek()
{
	if(top==-1)
		{
		printf("stack is empty\n");
		}
	else
		{
		printf("top element is=%c\n",stack[top]);
		}
}









