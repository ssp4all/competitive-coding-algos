// Suraj Pawar- ssp4all

#include <bits/stdc++.h>
# define lld long long int
int main() {
	int t;
	lld n, a, b, k, i;
	scanf("%d",&t);
	while(t--){
		lld pa = 0;
		lld pb = 0;
		scanf("%lld %lld %lld %lld",&n,&a,&b,&k);
		for(i=1; i<(n+1); i++){
			if(i%a == 0 && i%b == 0){
			}
			else if(i%a == 0 && i%b != 0)
				pa++;
			else if(i%a != 0 && i%b == 0)
				pb++;
			if((pa+pb)>=k){
				printf("Win\n");
				break;
			}
		}
		if((pa+pb)<k)
			printf("Lose\n");
	}
}