#include <bits/stdc++.h>
using namespace std;

int main() {
    // Complete the code.
    int num=0;
    char str[10];
    cin>>num;
    if(num<10){
        switch(num){
            case 0: 
                strcpy( str, "zero");
                break;
            case 1: 
                strcpy( str, "one");
                break;
            case 2: 
                strcpy( str, "two");
                break;
            case 3: 
                strcpy( str, "three");
                break;
            case 4: 
                strcpy( str, "four");
                break;
            case 5: 
                strcpy( str, "five");
                break;
            case 6: 
                strcpy( str, "six");
                break;
            case 7: 
                strcpy( str, "seven");
                break;
            case 8: 
                strcpy( str, "eight");
                break;
            case 9: 
                strcpy( str, "nine");
                break;
        }
    }
    if(num>9)
        cout<<"Greater than 9";
    else
        cout<<str;
}