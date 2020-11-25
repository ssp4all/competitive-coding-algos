#include <bits/stdc++.h>
using namespace std;

int max_of_four(int a, int b, int c, int d){
	int i, max1;
	max1 = max(a,b);
	max1 = max(max1,c);
	max1 = max(max1,d);
	return max1;
}
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

