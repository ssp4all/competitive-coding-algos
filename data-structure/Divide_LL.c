#include<stdio.h>

struct node
{
    int data;
    struct node* next;
};

struct node *temp,*temp1,*temp2,*end,*start,*start1,*start2,*p;
int count();
void display();

struct node* createnode();

void main()
{
    int n;
    int i;
    int pos;
    printf("\nEnter No. of Nodes : ");
    scanf("%d",&n);

    printf("\nEnter Linked List data :");
    temp=createnode();
    scanf("%d",&(temp->data));
    start=temp;
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
    display();

    printf("\n Enter Position at which LL is to be Divided : ");
    scanf("%d",&pos);
    if(pos > 0 && pos <= count())
    {

        temp=start;
        for(i=1; i<=pos-1 ;i++)
        {
            temp=temp -> next;
        }
        if(temp == NULL)
        {
            printf("\n LL is Empty");
            return;

        }
        else
        {
            start2=temp->next;

            temp->next=NULL;
        }
    }
    temp1=start2;
    if(temp1 == NULL)
    {
        printf("\n LL is Empty");

    }
    else
    {

        printf("\n Current Status of LL 1 is : ");
        p=start2;
        while(p->next != NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d",(p->data));
    }
    display();


}
struct node* createnode()
{
    return((struct node *)malloc(sizeof(struct node)));
}

void display()
{
    temp2=start;
    if(temp2 == NULL)
    {
        printf("\n LL  is Empty");

    }
    else
    {

        printf("\n Current Status of LL  2 is : ");
        p=start;
        while(p->next != NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d",(p->data));
    }

}
int count()
{
    int c;

    p=start;
    while(p !=NULL)
    {
        c++;
        p=p->next;
    }
    return c;
}
