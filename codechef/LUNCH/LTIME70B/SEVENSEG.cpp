/*Corrupted Seven-Segment Display*/

#include<stdio.h>

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int segments[10][7] = { {0, 1, 2, 4, 5, 6 }, { 2, 5 }, { 1, 2, 3, 4, 6 }, { 1, 2, 3, 5, 6 }, { 0, 2, 3, 5 }, { 0, 1, 3, 5, 6 }, { 0, 1, 3, 4, 5, 6 }, { 1, 2, 5 }, { 0, 1, 2, 3, 4, 5, 6 }, { 0, 1, 2, 3, 5, 6 } };
	int sizes[10] = { 6, 2, 5, 5, 4, 5, 6, 3, 7, 6 };
	int dead[10], x[10], y[10];
	int dead_count, i, j, k, max_count, min_count, N, T;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &N);
		for (i = 0; i < N; i++)
			scanf("%d %d", &x[i], &y[i]);
		min_count = 8;
		max_count = -1;
		for (i = 0; i < 128; i++)
		{
			for (j = 0; j < 7; j++)
				dead[j] = 0;
			for (j = 0; j < 7; j++)
				if ((i & (1 << j)) == 0)
					dead[j] = 1;
			cout<<i<<": ";
			for (j = 0; j < 7; j++)
				cout<<dead[j]<<" ";
			cout<<endl;		
			for (j = 0; j < N; j++)
			{
				dead_count = 0;
				for (k = 0; k < sizes[x[j]]; k++)
					if (dead[segments[x[j]][k]])
						dead_count++;
				cout<<dead_count<<endl;
				if (y[j] != sizes[x[j]] - dead_count)
					break;
			}
			if (j == N)
			{
				cout<<"yeah"<<endl;
				dead_count = 0;
				for (j = 0; j < 7; j++)
					if (dead[j])
						dead_count++;
				if (min_count > dead_count)
					min_count = dead_count;
				if (max_count < dead_count)
					max_count = dead_count;
				cout<<min_count<<" "<<max_count<<endl;
			}
		}
		if (min_count == 8)
			printf("invalid\n");
		else
			printf("%d %d\n", min_count, max_count);
	}
	return 0;

}
