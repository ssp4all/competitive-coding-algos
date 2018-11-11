#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	int *ptr = (int*) malloc(0);
	if(ptr==NULL)
	{
		cout << "Null pointer";
	}
	else
	{
		cout << "Address = " << ptr << endl;
	}

	free(ptr);
	return 0;
}

