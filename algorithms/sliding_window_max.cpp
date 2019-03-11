//Dynamic Programming approach
// Suraj Pawar
#include <bits/stdc++.h>
using namespace std;
#define endl "\n" 
#define lld long long int
#define LTM 1000

lld arr[LTM]; 
lld LR[LTM]; 
lld RL[LTM]; 
lld max_val[LTM]; 

lld n,w,i,k;   

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    lld t;
    cin>>t;

    while(t--){
        
        cin>>n>>w;    
        k=n-w+1; // 'K' is number of Windows
            
        for(i=1;i<=n;i++)
            cin>>arr[i];
        
        for(i=1;i<=n;i++){
            if(i%w==1)
                LR[i]=arr[i];
            else
				LR[i]=max(LR[i-1],arr[i]);               
		}

        
        for(i=n;i>=1;i--){
            if(i%w==0 || i==n )
                RL[i]=arr[i];
            else
                RL[i]=max(RL[i+1],arr[i]);
        }
        
        for(i=1;i<=k;i++)    // maximum
            max_val[i]=max(RL[i],LR[i+w-1]);
    
        for(i=1;i<=k;i++)
            cout<<max_val[i]<<" ";
        cout<<endl; 
    }
    return 0;
}
