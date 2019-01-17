#include<stdio.h>

struct queue
{
    int data;
    struct queue *next;
};

struct queue *temp,*front=NULL,*rear=NULL,*p;

struct queue *createnode();
void insert(int);
void display();
int count();
void search();

void main()
{
    int n,b,ele,i;
    do
    {
        printf("\n\n\n *** MENU  ***");
        printf("\n1:Create");
        printf("\n2:Insert");
        printf("\n3:Delete");
        printf("\n4:Display");
        printf("\n5:Count");
        printf("\n6:Search");
        printf("\n7:Exit");
        printf("\n\n Enter Your Choice : ");
        scanf("%d",&n);
        switch(n)
            {
                case 1 : //create a queue
                {
                   printf("\n Enter a Element to Create a Q : ");
                   temp=createnode();
                   scanf("%d",&(temp->data));
                   temp->next=NULL;

                   front=temp;
                   rear=temp;

                   printf("\n Queue Created Successfully");
                   display();
                   break;
                }
                case 2 :     //insert
                {
                    if(front == NULL)
                    {
                        printf("\n First Create A Q");
                    }
                    else
                    {
                       printf("\n Enter a Element in the Q : ");
                       temp=createnode();
                       scanf("%d",&(temp->data));
                       temp->next=NULL;
                       rear->next=temp;
                       rear=temp;
                       display();
                    }
                   break;
                }

                case 3 :    //delete
                {
                    temp=front;
                    if(temp == NULL)
                    {
                        printf("\n Q is EMPTY");
                    }
                    else
                    {
                        front=temp-> next;
                        temp->next=NULL;
                        free(temp);
                        printf("\n Element Removed SUCCESFULLY");
                        display();

                    }

                    break;
                }

                case 4 :    //display
                {

                    display();
                    break;
                }

                case 5:
                {
                    printf("\n NO of Elements in the Q are :%d  ",count());
                    break;

                }

                case 6:
                {
                   search();
                   break;
                }

                case 7:
                {
                    printf("\n THANK YOU VERY MUCH....!!!");
                    break;
                }
                default :
                {
                    printf("\n Invalid Input");
                    break;
                }


            }
    }while(n != 7 );
}

struct queue *createnode()
{
    return(struct queue *)malloc(sizeof(struct queue));

}

void display()
{
    temp=front;
    if(temp == NULL)
    {
        printf("\n Q is EMPTY");
    }
    else
    {
        printf("\nCurrent Status of Q is : ");
        while(temp->next != NULL)
        {
            printf("%d\t",temp->data);
            temp=temp->next;
        }
        printf("%d",temp->data);
    }
}

int count()
{
    int c=0;
    p=front;
    while(p != NULL)
    {
        c++;
        p=p->next;
    }
    return c;
}

void search()
{
    temp=front;
    int x;
    printf("\n Enter a Element to be Searched : ");
    scanf("%d",&x);
    while(temp->next != NULL && temp->data != x)
    {
        temp=temp->next;
    }
    if(x == temp->data)
    {
        printf("\n Data FOUND");
    }
    else
    {
        printf("'\n Data NOT Found");
    }
}
