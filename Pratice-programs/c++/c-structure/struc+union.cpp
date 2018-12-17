#include<iostream>
using namespace std;

typedef struct
{
    union
    {
        int roll;
        char name[20];
    };
    int marks;
}student;
student stud;

int main()
{
    cout<<"Enter your name:";
    cin>>stud.name;
    cout<<stud.name;
    return 0;
}
