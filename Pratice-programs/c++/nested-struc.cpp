#include<iostream>
using namespace std;
int main()
{
    typedef struct dob{
        int day;
        int month;
        int year;
    };

    typedef struct student{
        int roll;
        char first[20];
        char last[20];
        dob date;
    };
    student std1;

    cout<<"\nEnter the Roll:";
    cin>>std1.roll;

    cout<<"\nEnter the First:";
    cin>>std1.first;

    cout<<"\nEnter the Last:";
    cin>>std1.last;

    cout<<"\nEnter the Date:";
    cin>>std1.date.day>>std1.date.month>>std1.date.year;


    cout<<"\nRoll\tName\tDate"<<endl;
    cout<<std1.roll<<"\t"<<std1.first<<" "<<std1.last<<"\t"<<std1.date.day<<"/"<<std1.date.month<<"/"<<std1.date.year;
    return 0;

}
