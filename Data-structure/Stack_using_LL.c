#include<stdio.h>

typedef struct stack
{
    int data;
    struct stack *next;
};

struct stack *top,*temp;

int search(int d);
void display();

void main()
{

	int i,n,d,a,x;
       do
       {
            printf("\n\n***   MENU   ***\n");
            printf("\n1:Create");
            printf("\n2:Push");
            printf("\n3:Pop");
            printf("\n4:Peek");
            printf("\n5:Display");
            printf("\n6:Search");
            printf("\n99:Exit");
            printf("\n Enter Your Choice : ");
			scanf("%d",&n);

			switch(n)
			{

                case 1:
                        printf("\n Enter a data to Create a Stack : ");
                        temp=(struct stack *)malloc(sizeof(struct stack));
                        scanf("%d",&(temp->data));
                        temp->next=NULL;
                        top=temp;
                        printf("\n Stack Created Successfully");
                        display();
                        break;

                case 2:
                        printf("\n Enter a data to PUSH in the Stack : ");
                        temp=(struct stack *)malloc(sizeof(struct stack));
                        scanf("%d",&(temp->data));
                        temp->next=top;
                        top=temp;
                        display();
                        break;

                case 3:
                        temp=top;
                        if(temp == NULL)
                        {
                            printf("\n Stack is EMPTY");
                        }
                        else
                        {
                            top=top->next;
                            temp->next=NULL;
                            free(temp);
                            display();
                        }
                        break;

                case 4:
                        temp=top;
                        if(temp == NULL)
                        {
                            printf("\nStack is Empty ");
                        }
                        else
                        {

                            printf("\nElement at the Top of Stack is : ");
                            printf("%d",temp->data);
                        }
                        display();
                        break;

                case 5:
                        display();
                        break;

                case 6:
                        printf("\n Enter Element to Search : ");
                        scanf("%d",&x);
                        a=search(x);
                        if(a == 0)
                        {
                            printf("\nData NOT Found");
                        }
                        else
                        {
                            printf("\nData Found ");
                        }
                        break;


                case 99:
                        printf("\n Thank You Very Much");
                        break;

                default:
                        printf("Invalid Input\n ");
                        break;
		   }

	  }while(n != 99);

}

int search(int d)
{
    temp=top;
    while( temp != NULL && temp->data != d)
    {
        temp=temp->next;
    }
    if(temp == NULL )
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

void display()
{
    temp=top;
    if(temp == NULL)
    {
        printf("\n Stack is Empty ");
    }
    else
    {
        printf("\nCurrent Status of Stack is : ");
        while(temp->next != NULL)
        {
            printf("\n%d",temp->data);
            temp=temp->next;
        }
        printf("\n%d",temp->data);
    }
}
