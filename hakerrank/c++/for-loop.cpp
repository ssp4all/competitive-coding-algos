#include <bits/stdc++.h>
using namespace std;

int main() {
    // Complete the code.
    int num1, num2, i;
	char str[20];
    cin>>num1>>num2;
    for(i=num1; i<=num2; i++){
		if(i<10){
			switch(i){
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
		if(i>9){
			if(i%2 == 0)
				cout<<"even"<<endl;
			else
				cout<<"odd"<<endl;
		}
		else
			cout<<str<<endl;
    }
}