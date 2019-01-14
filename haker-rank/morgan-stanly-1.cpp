#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,m,k;
    scanf("%d %d %d",&n,&m,&k);
    int currency[n],bitcoins[n],d2[n];
    for(int i=0;i<n;i++)
        scanf("%d",&currency[i]);
    
    for(int i=0;i<n;i++)
        scanf("%d",&bitcoins[i]);
    int d1 = m*k;
    
    for(int i=0;i<n;i++)
    {
        d2[i] = m * bitcoins[i]*currency[i];
    }
    for (int i = 0; i < n-1; i++)      
    {
        for (int j = 0; j < n-i-1; j++) 
       {
           if (d2[j] < d2[j+1])
           {
               int temp = d2[j];
               d2[j] = d2[j+1];
               d2[j+1] = temp;
           }
       }
    }
    int ans = max(d1,d2[0]);
    printf("%d",ans);    
    return 0;
}
