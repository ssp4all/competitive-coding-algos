#include<stdio.h>

void push(char);
void display();
char pop();
void peek();
int top=-1;

int stack[5];

void main()
{
	int ch;
	int n,i;

       do
       {
			printf("\n***********MENU*************\n");
			printf("\n\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.stop\n");
            printf("\n Enter Your Choice : ");
			scanf("%d",&n);

			switch(n)
			{
			case 1:
        			printf("\nenter a char to push : ");
                    fflush(stdin);
                    scanf("%d",&ch);
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
                    printf("\n THANK YOU VERY MUCH...!!! ");
                    break;

			default:
                    printf("Invalid input\n ");
                    break;
		   }

	  }while(n !=5);


}
void push(char ch)
{
	if(top == 4)
	{
		printf("Stack is OVERFLOW\n");
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
		printf("\n%d\n",stack[i]);
	}
}
char pop()
{
	if(top==-1)
    {
        printf("stack is UNDERFLOW\n");
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
            printf("stack is EMPTY\n");
		}
	else
		{
            printf("top element is=%d\n",stack[top]);
		}
}

