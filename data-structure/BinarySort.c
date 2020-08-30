// PROGRAM FOR BINARY SEARCH SORT
#include<stdio.h>
#include<conio.h>

int main()
{
	int i,n,a[100];
	int ele,retValue;

	//int a[] = {25,57,48,37,12,92,86,33};
	// n = 8;

	printf("\n Enter no of elements :");
    scanf("%d", &n);

    printf("\n Enter the nos : ");
    for (i = 0; i < n; i++)
       scanf("%d", &a[i]);

	quick(a,0,n-1); // SORT USING ANY ALGORITHM

	printf("\n\nENTER ELEMENT TO BE SEARCHED : \t");
	scanf("%d",&ele);



	retValue = binSearch(a,ele,0,n-1);

	if(retValue == -1)
	{
		printf("\n\nELEMENT IS NOT PRESENT IN THE ARRAY !");
	}
	else
	{
		printf("\n\nELEMENT IS PRESENT IN THE ARRAY !!!");
		printf("\n\nAT LOCATION %d IN THE SORTED ( NOT IN ORIGINAL) ARRAY ",retValue);
	}
}
int partition( int x[], int lb, int ub)
{
	int a, down, temp, up;

	a = x[lb]; // the element whose final position is to be sought

	up = ub;
	down = lb;

	while(down < up)
	{
		while( x[down] <= a && down < ub)
			down++;
		while ( x[up] > a)
			up--;
		if(down < up)
		{
			temp = x[down];
			x[down] = x[up];
			x[up] = temp;
		}// end if
	}//end while
	x[lb] = x[up];
	x[up] = a;
	return up;
}

void quick(int x[],int lb, int ub)
{
	int pivot;
	if(lb>=ub)
		return;
	pivot = partition(x,lb,ub);
		// element at position 'pivot' has got its final position
	quick(x,lb,pivot-1);
	quick(x,pivot+1,ub);
}
int binSearch(int a[],int ele,int low, int high)
{
	int mid;

	if(low>high)
		return -1;
	mid = (low + high) /2;
	if(ele == a[mid])
		return(mid);
	if(ele < a[mid])
		return ( binSearch(a,ele,low,mid-1) );
	else
		return ( binSearch(a,ele,mid+1,high) );
}
