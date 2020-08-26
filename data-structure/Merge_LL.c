#include<stdio.h>

struct node
{
    int data;
    struct node* next;
};

struct node *temp,*temp1,*temp2,*temp3,*end,*start1,*start2,*p,*p2;

void display_1();
void display_2();
void display();
struct node* createnode();

void main()
{
    int n;
    int i;
    printf("\nEnter No. of Nodes in LL 1: ");
    scanf("%d",&n);

    printf("\nEnter Linked List 1 data :");
    temp=createnode();
    scanf("%d",&(temp->data));
    start1=temp;
    end=temp;
    temp->next=NULL;
    printf("\n Linked List is Created Successfully\n");
    for(i=2;i<=n;i++)
    {
         printf("Enter the %dth element to be added : ",i);
         temp=createnode();
         scanf("%d",&(temp->data));
         temp->next=NULL;
         end->next=temp;
         end=temp;
    }
   // display_1();

    int n2;
    printf("\nEnter No. of Nodes in LL 2: ");
    scanf("%d",&n2);

    printf("\nEnter Linked List 2 data :");
    temp=createnode();
    scanf("%d",&(temp->data));
    start2=temp;
    end=temp;
    temp->next=NULL;
    printf("\n Linked List is Created Successfully\n");
    for(i=2;i<=n2;i++)
    {
         printf("Enter the %dth element to be added : ",i);
         temp=createnode();
         scanf("%d",&(temp->data));
         temp->next=NULL;
         end->next=temp;
         end=temp;
    }
    display_2();

    p=start1;
    while(p->next != NULL)
    {
        p=p->next;
    }
    p->next=start2;
    display();



}




struct node* createnode()
{
    return((struct node *)malloc(sizeof(struct node)));
}

void display_1()
{
    temp=start1;
    if(temp == NULL)
    {
        printf("\n LL  is Empty");

    }
    else
    {

        printf("\n Current Status of LL  1 is : ");
        p=start1;
        while(p->next != NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d",(p->data));
    }

}


void display_2()
{
    temp=start2;
    if(temp == NULL)
    {
        printf("\n LL  is Empty");

    }
    else
    {

        printf("\n Current Status of LL  2 is : ");
        p2=start2;
        while(p2->next != NULL)
        {
            printf("%d -> ",(p2->data));
            p2=p2->next;
        }
        printf("%d",(p2->data));
    }

}

void display()
{
    temp=start1;
    if(temp == NULL)
    {
        printf("\n LL  is Empty");

    }
    else
    {

        printf("\n Current Status of Merged LL is : ");
        p=start1;
        while(p->next != NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d",(p->data));
    }
}
