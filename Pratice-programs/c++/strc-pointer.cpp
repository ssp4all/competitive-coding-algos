#include<iostream>
using namespace std;
int main()
{
    typedef struct{
        int roll;
        char name[100];
    }student;

    student stud, *pstud;
    pstud = &stud;
    cout<<"Enter Roll no. and name:";
    cin>>(pstud->roll);

    cout<<(pstud->roll);


    return 0;
}
