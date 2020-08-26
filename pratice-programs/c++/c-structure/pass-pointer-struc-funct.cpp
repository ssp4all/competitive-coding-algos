//Write  a program to pass pointer to a structure to a function
#include<iostream>
#include <cstdlib>
#include<bits/stdc++.h>
//#include <cstdlib>
using namespace std;

typedef struct {
        int roll;
        char name[20];
}student;

void display(student *);
int main()
{
    student *pstud;
    pstud = (student *)malloc(sizeof(student));
    cout<<"\nEnter a name:";
    cin>>pstud->name;
    cout<<"Enter a Roll No:";
    cin>>pstud->roll;
    display(pstud);
    free(pstud);

    return 0;

}
void display(student *ptr)
{
    cout<<"\nName\tRoll-No\n";
    cout<<ptr->name<<"\t"<<ptr->roll<<endl;

}
