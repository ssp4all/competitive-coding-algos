#include<bits/stdc++.h>
using namespace std;

void printSubsequences(int arr[], int n);
int main()
{
    int arr[5] = {0, 1, 2};
    int n = 3;
    printSubsequences(arr, n);
    return 0;

}
void printSubsequences(int arr[], int n)
{
    unsigned int opsize = pow(2, n);
	int t = 0;
    for (int counter = 0; counter < opsize; counter++)
    {
        for (int j = 0; j < n; j++)
        {
			
			// cout<<"counter: "<<counter<<" "<<"j: "<<(1<<j)<<endl;
			// cout<<"op :"<<(counter & (1<<j))<<endl;
            if (counter & (1<<j)){
				// cout<<"yeah ";
                cout << arr[j] << " ";
				
       		}
		}
		++t;
        cout << endl;
    }
	cout<<t<<endl;
}