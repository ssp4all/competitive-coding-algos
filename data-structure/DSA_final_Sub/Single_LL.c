#include<stdio.h>

struct node
{
    int data;
    struct node *next;
};

int n,d,c=0,d2,d3,d4,pos,i;

struct node *createnode();
void display();
int count();
int search(int);
void insertb();
void inserta();
void insertpos();
void delete();
void deleteatpos();
void merge();
void divide();
void display_2();
void display_1();
void display_3();
void reverse();
void display_r(struct node *);

struct node *start,*start1,*end,*temp,*temp2,*temp1,*p,*p2,*ptr,*start2,*p,*q,*r,*s;

void main()
{
    do
    {
        printf("\n\n***   MENU   ***\n");
        printf("\n1:Create");
        printf("\n2:Add At End");
        printf("\n3:Add Before a Node");
        printf("\n4:Add After a Node");
        printf("\n5:Display");
        printf("\n6:Count");
        printf("\n7:Search");
        printf("\n8:Delete By Value");
        printf("\n9:Delete By Position");
        printf("\n10:Insert at Position");
        printf("\n11:Divide at Position");
        printf("\n12:Merge at Position");
        printf("\n13:Reverse LL");
        printf("\n99:Stop");
        printf("\nEnter Your Choice :");
        scanf("%d",&n);
        switch(n)
        {
            case 1:
                    printf("\nEnter Linked List data :");
                    temp=createnode();
                    scanf("%d",&(temp->data));
                    start=temp;
                    end=temp;
                    temp->next=NULL;
                    printf("\n Linked List is Created Successfully");
                    display();
                    break;
            case 2:
                    printf("\n Add Element in LL :");
                    temp=createnode();

                    scanf("%d",&(temp->data));
                    temp->next=NULL;
                    end->next=temp;
                    end=temp;
                    display();
                    break;
            case 3:
                    insertb();
                    break;

            case 4:
                    inserta();
                    break;
            case 5:

                    display();
                    break;

            case 6:
                    printf("\n No. of Nodes in the LL are : %d ",count());
                    break;
            case 7:

                    printf("\n Enter a element to be searched :  ");
                    scanf("%d",&d);
                    temp=start;
                    if(temp == NULL)
                    {
                        printf("\n LL is Empty ...!!!");
                    }
                    else
                    {
                        if( search(d)== 1)
                        {
                            printf("\n Data Found");

                        }
                        else
                        {
                            printf("\n Data NOT found");

                        }
                    }
                    break;
            case 8:
                    delete();
                    break;
            case 9:
                    deleteatpos();
                    break;
            case 10:
                    insertpos();
                    break;
            case 11 :
                    divide();
                    break;
            case 12 :
                    merge();
                    break;
            case 13 :
                    reverse();
                    break;
            case 99:
                    printf("\n THANK YOU VERY MUCH ... ");
                    break;
            default:
                    printf("\nInvalid Input\n\n");
                    break;
        }

    }while(n != 99);
}
struct node *createnode()
{
    return(struct node *)malloc(sizeof(struct node));

}

void display()
{
    temp=start;
    if(temp == NULL)
    {
        printf("\n LL is Empty");

    }
    else
    {

        printf("\n Current Status is : ");
        p=start;
        while(p->next!=NULL)
        {
            printf("%d -> ",(p->data));
            p=p->next;
        }
        printf("%d",(p->data));
    }

}

int search(int d)
{
    temp=start;
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

void delete()
{


            printf("\n Enter  Node to be Deleted : ");
            scanf("%d",&d2);
            if(search(d2) == 1)
            {
                while( temp != NULL && temp->data != d2)
                {
                    temp=temp->next;
                }

                if(temp == start)
                {
                    start=temp-> next;
                    temp->next=NULL;
                    free(temp);
                    printf("\n Node Deleted Successfully");
                    display();
                }
                else
                {

                    ptr=start;
                    while(ptr->next != temp )
                    {
                        ptr=ptr->next;
                    }
                    ptr->next=temp->next;
                    temp->next=NULL;
                    free(temp);
                    printf("\n Node Deleted Successfully");
                    display();
                }

            }
            else
            {
                printf("\n Invalid Node");
            }
}

void deleteatpos()
{
    printf("\n Enter Position at which node is to be Deleted : ");
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

        }
        else
        {
            if(temp == start || pos == 1)
            {
                start=temp-> next;
                temp->next=NULL;
                free(temp);
                printf("\n Node Deleted Successfully");
                display();

            }
            else
            {

                ptr=start;
                while(ptr->next != temp )
                {
                    ptr=ptr->next;
                }
                ptr->next=temp->next;
                temp->next=NULL;
                free(temp);
                printf("\n Node Deleted Successfully");
                display();

            }
        }

    }
    else
    {
        printf("\n Invalid position");
    }
}

int count()
{
    int c=0;

    p=start;
    while(p != NULL)
    {
        c++;
        p=p->next;
    }
    return c;
}

void insertb()
{
    printf("\n Enter a Node Before which node is to be inserted : ");
    scanf("%d",&d3);
    if(search(d3) == 1)
    {
        temp=start;
        while(temp != NULL && temp->data != d3)
        {
            temp=temp->next;
        }
        if(temp == NULL)
        {
            printf("\n LL is Empty");
            return;
        }
        else
        {
            printf("\n Enter a Node Data : ");
            p=createnode();
            scanf("%d",&(p->data));
            if(temp == start)
            {
                p->next=start;
                start=p;
            }
            else
            {
                ptr=start;
                while(ptr ->next != temp)
                {
                    ptr=ptr->next;
                }
                p->next=ptr->next;
                ptr->next=p;
            }

        }
    }
    else
    {
        printf("\n Invalid Node");
        return;
    }
    display();

}
void inserta()
{
    printf("\n Enter a Node After which node is to be inserted : ");
    scanf("%d",&d4);
    if(search(d4) == 1)
    {
        temp=start;
        while(temp != NULL && temp->data != d4)
        {
            temp=temp->next;
        }

            printf("\n Enter a Node Data : ");
            p=createnode();
            scanf("%d",&(p->data));
            p->next=temp->next;
            temp->next=p;
    }

    else
    {
        printf("\n Invalid Node");
        return;
    }
    display();


}
void insertpos()
{
    printf("\n Enter Position at which node is to be Inserted : ");
    scanf("%d",&pos);
    if(pos > 0 && pos <= count())
    {

        printf("\n Enter a Node Data : ");
        p=createnode();
        scanf("%d",&(p->data));

        if(pos==1)
        {
            p->next=start;
            start=p;
        }
        else
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

                p->next=temp->next;
                temp->next=p;

            }
        }
    }

    else
    {
        printf("\n Invalid position");
        return;
    }
    display();
}

void divide()
{
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
void merge()
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
    display_3();
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
void display_3()
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
void reverse()
{
    void display_r(struct node *s)
    {
        if(s != NULL)
        {
            display_r(s->next);
            printf("%d ->",s->data);
        }
    }
    display_r(start);
}
