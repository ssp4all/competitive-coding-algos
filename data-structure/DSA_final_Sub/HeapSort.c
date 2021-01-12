/*
 * C Program to sort an array using Heap Sort technique
 */

#include<stdio.h>
#include <stdlib.h>

void  max_heapify(int a[], int i, int heapsize)
{
    int tmp, largest;
    int l = (2 * i) + 1;
    int r = (2 * i) + 2;
    if ((l <= heapsize) && (a[l] > a[i]))
         largest = l;
    else
         largest = i;
    if ((r <= heapsize) && (a[r] > a[largest]))
         largest = r ;
    if (largest != i)
    {
         tmp = a[i];
         a[i] = a[largest];
         a[largest] = tmp;
         max_heapify(a, largest, heapsize);
    }
}
void  build_max_heap(int a[], int heapsize)
{
    int i;
    for (i = heapsize/2; i >= 0; i--)
    {
         max_heapify(a, i, heapsize);
    }
}
void heap_sort(int a[], int heapsize)
{
    int i, tmp;
    build_max_heap(a, heapsize);
    for (i = heapsize; i > 0; i--)
    {
        tmp = a[i];
        a[i] = a[0];
        a[0] = tmp;
        heapsize--;
        max_heapify(a, 0, heapsize);
    }
}
int main()
{
    int i, r, heapsize;
    int a[100],n;

    // int n=8;
	// int a[] = {25,57,48,37,12,92,86,33};

	printf("\n Enter no of elements :");
    scanf("%d", &n);

    printf("\n Enter the nos : ");
    for (i = 0; i < n; i++)
       scanf("%d", &a[i]);

	heapsize = n - 1;

    printf("\n");
    heap_sort(a, heapsize);
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    return 0;
}
