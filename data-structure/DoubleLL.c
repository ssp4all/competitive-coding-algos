#include<stdio.h>

struct node
{
    int data;
    struct node *next,*prev;
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
struct node *start,*end,*temp,*p,*ptr;

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
        printf("\n11:Stop");
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
                    temp->prev=NULL;
                    printf("\n Double Linked List is Created Successfully");
                    display();
                    break;
            case 2:
                    temp=createnode();
                    printf("\nEnter data : ");
                    scanf("%d",&(temp->data));
                    temp->next=NULL;
                    temp->prev=start;
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
            case 11:
                    printf("\n THANK YOU VERY MUCH ... ");
                    break;

            default:
                    printf("\nInvalid Input\n\n");
                    break;
        }

    }while(n !=11);
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
        while(p->next != NULL)
        {
            printf("<- %d -> ",(p->data));
            p=p->next;
        }
        printf("<- %d ->",(p->data));
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
            temp->prev=NULL;
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
            if(temp->next != NULL)                  //NOT A LAST NODE
            {
                ptr->next->prev=temp->prev;
                return;
            }


            temp->next=NULL;
            temp->prev=NULL;

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
                temp->prev=NULL;
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
                if(temp->next != NULL)                  //NOT A LAST NODE
                {
                    ptr->next->prev=temp->prev;
                    return;
                }

                temp->next=NULL;
                temp->prev=NULL;

                free(temp);
                printf("\n Node Deleted Successfully");
                display();

            }
        }

    }
    else
    {
        printf("\n Invalid position");
        return;
    }
}
int count()
{
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
    printf("\n Enter a Node data Before which node is to be inserted : ");
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

        }
        else
        {
            printf("\n Enter a Node Data : ");
            p=createnode();
            scanf("%d",&(p->data));
            if(temp == start)
            {
                p->next=temp;
                temp->prev=p;
                p->prev=NULL;
                temp->next=NULL;
                start=p;
            }
            else
            {
                ptr=start;
                while(ptr->next != temp)
                {
                    ptr=ptr->next;
                }
                p->next=temp;
                p->prev=ptr;
                ptr->next=p;
                temp->prev=p;
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
            p->prev=temp;
            p->next=temp->next;
            temp->next=p;
            temp->next->prev=p;

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
            p->prev=NULL;
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
                printf("\n LL is Empty ");
            }
            else
            {

                p->prev=temp;
                p->next=temp->next;
                temp->next=p;
                temp->next->prev=p;

            }
        }
    }

    else
    {
        printf("\n Invalid position");
    }
    display();
}

