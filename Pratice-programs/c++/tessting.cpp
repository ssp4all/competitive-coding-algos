#include<iostream>
using namespace std;
int main()
{
    int i=0;
    for(i=0;i<5;i++)
        cout<<i;
    cout<<endl;
    for(i=0;i<5;++i)
        cout<<i;

    if (0>0)
        cout<<"T";
    else
        cout<<"F";
   return 0;
}
