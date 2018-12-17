#include<stdio.h>

struct node
{
    char data[20];
    struct node *next;
};

int n,n1,d,c=0,d2,d3,d4,pos,i;

struct node *start,*end,*temp,*p,*ptr;

struct node *createnode();
void display();
int count();

void main()
{
    char name[20],s;
    int age,contact;
    printf("\n WELCOME TO MINI-FCEBOOK");
    printf("\n Enter your name : ");
    scanf("%s",name);
    printf("Enter your age: ");
    fflush(stdin);
    scanf("%d",&age);
    printf("Enter your Contact Number : ");
    fflush(stdin);
    scanf("&d",&contact);
    printf("Your Sex(m/f) : ");
    fflush(stdin);
    scanf("&c",&s);
    printf("\n  HUREEY ... REGISTRATION SUCCESSFULL !!!");


    do
    {
        printf("\n -------------------------");

        printf("\n\n***   MENU   ***\n");
        printf("\n1:Create FL");
        printf("\n2:Add More Friends");
        printf("\n5:Display");
        printf("\n6:Count");
        printf("\n11:Stop");
        printf("\nEnter Your Choice :");
        fflush(stdin);
        scanf("%d",&n1);
        switch(n1)
        {
            case 1:
                    printf("\nEnter Your First Friend name :");
                    temp=createnode();
                    scanf("%s",(temp->data));
                    start=temp;
                    end=temp;
                    temp->next=NULL;
                    printf("\n Friend List is Created Successfully");
                    display();
                    break;
            case 2:
                    printf("\n Add More Friends in FL :");
                    temp=createnode();

                    scanf("%s",(temp->data));
                    temp->next=NULL;
                    end->next=temp;
                    end=temp;
                    display();
                    break;
            case 5:

                    display();
                    break;

            case 6:
                    printf("\n No. of Friends : %d ",count());
                    break;
            case 11:
                    printf("\n THANK YOU VERY MUCH ... ");
                    break;

            default:
                    printf("\nInvalid Input\n\n");
                    break;
        }

    }while(n1 !=11);
}


struct node *createnode()
{
    return(struct node *)malloc(sizeof(struct node));
    return;

}

void display()
{
    temp=start;
    if(temp == NULL)
    {
        printf("\n FL is Empty");

    }
    else
    {

        printf("\n Current Status is : ");
        p=start;
        while(p->next!=NULL)
        {
            printf("%s -> ",(p->data));
            p=p->next;
        }
        printf("%s",(p->data));
    }

}

int count()
{

    p=start;
    while(p !=NULL)
    {
        c++;
        p=p->next;
    }
    return c;
}
