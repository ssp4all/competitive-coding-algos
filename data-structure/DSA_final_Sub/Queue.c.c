#include<stdio.h>

int q[5];

int front=-1,rear=-1,i,n;

void insert(int);
void display( );
void delete_ele();
void count();
void search();

void main()

{
    int n,b,ele;
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
                case 1 : //crate a queue

                {
                   int a;

                   printf("\n Enter a Element in the Q : ");
                   scanf("%d",&a);
                   q[0]=a;
                   front++;
                   rear++;
                   printf("\n Queue Created Successfully");

                }
                break;
                case 2 :    //insert
                {


                    insert(b);
                }
                break;
                case 3 :    //delete
                {
                    delete_ele();
                    display();

                }
                break;
                case 4 :    //display
                {

                    display();
                }
                break;
                case 5:
                {
                    count();
                }
                break;
                case 6:
                {
                   search();
                }
                break;
                case 7:
                {
                    printf("\n THANK YOU VERY MUCH....!!!");
                }
                break;
                default :
                {
                    printf("\n Invalid Input");

                }
                break;

            }
    }while(n != 7 );

}

//--------------------------------------------
void insert(int b)
{
    int f=0,r=0;
    f=front;
    r=rear;
    if(f == -1)
    {
        printf("\n Q is NOT Created...");
    }
    else
    {
        if(r == 4)
        {
            printf("\n Q is Overflow");
            return;
        }
        printf("\n Enter Element : ");
        scanf("%d",&b);
        rear++;
        q[rear]=b;

        display();
    }
}
//---------------------------------------------

void display()
{
    int i;
    int f=0,r=0;
    f=front;
    r=rear;
    printf("\n Current Status of Q is : ");
    if(f == -1)
    {
        printf("\n Q is Empty...!");
    }
    else
    {
        for(i=f;i<=r;i++)
        {
            printf(" %d\t",q[i]);
        }
    }

}
//------------------------------------------------

void delete_ele()
{
    int f=0,r=0;
    f=front;
    r=rear;
    if(f == -1)
    {
        printf("\n Underflow...!!! Please first create a Q to delete ");
        return ;
    }
    else if(f == r)
    {
        front=-1;
        rear=-1;
    }
    else
    {
        front++;
    }

}
//-------------------------------------------------------------------
void count()
{
    int f=0,r=0;
    f=front;
    r=rear;
    int c=0;
    for(i=f;i<=r;i++)
    {
        c++;
    }
    display();
    printf("\n No of Elements in Q are : %d",c);
}
//--------------------------------------------------------------------

void search()
{
    int f=0,r=0;
    if(front == -1)
    {
        printf("\n Q is NOT created");
        return;
    }
    printf("\n Enter Element to be Searched : ");
    scanf("%d",&n);
    f=front;
    r=rear;
    while(f != r && q[f] != n)
    {
        f++;
    }
    if(q[f] == n)
    {
        printf("\n Found");
    }
    else
    {
        printf("\n  Not Found");

    }
}
