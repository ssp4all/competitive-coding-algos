// A C++ program to demonstrate STL sort() using 
// our own comparator 
#include<bits/stdc++.h> 
using namespace std; 

// An interval has start time and end time 
typedef struct Interval{ 
	int start, end; 
}arr; 

// Compares two intervals according to staring times. 
bool compareInterval(arr i1, arr i2){ 
	if ( i1.start == i2.start )
		return (i1.end < i2.end); 
 	else
		return (i1.start < i2.start); 
} 

int main(){ 
	
	// Interval arr[] = { {6,8}, {1,9}, {1,4}, {4,7} }; 
	int n, x, y;
	cin>>n;
	arr arr[n]; 
	for(int i=0; i<n; ++i){
		cin>>x>>y;
		arr[i].start = x;
		arr[i].end = y;
	}
	sort(arr, arr+n, compareInterval); 

	cout << "Intervals sorted by start time : \n"; 
	for (int i=0; i<n; ++i) 	
		cout << "[" << arr[i].start << "," << arr[i].end 
			<< "] "; 

	return 0; 
} 
