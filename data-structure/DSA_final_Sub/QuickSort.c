// PROGRAM FOR QUICK SORT
#include<stdio.h>

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
void main()
{
	int i,n=8;
	int a[] = {25,57,48,37,12,92,86,33};
	quick(a,0,7);
	printf("\n\nSORTED USING QUICK SORT ...\n\n");
	for(i=0;i<n;i++)
	{
		printf("\t%d",a[i]);
	}
}
