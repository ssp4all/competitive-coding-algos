#include<stdio.h>

struct node
{
    int data;
    struct node *next;
};

struct node *temp,*end,*s,*start,*p,*q,*r;

void display();
void display_r(struct node*);

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
    display_r(start);


}
struct node* createnode()
{
    return((struct node *)malloc(sizeof(struct node)));
}

void display()
{
    temp=start;
    if(temp == NULL)
    {
        printf("\n LL  is Empty");

    }
    else
    {

        printf("\n Current Status of LL is : ");
        p=start;
        while(p->next != NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d\n",(p->data));
    }

}
void display_r(struct node *s)
{
    if(s != NULL)
    {
        display_r(s->next);
        printf("%d ->",s->data);
    }
}

