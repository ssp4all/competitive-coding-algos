
/**
    cpp program to solve capgemni techchallenge 50
*/
#include<iostream>
#define ll long long
using namespace std;


ll total_power(ll a[],ll n ,ll k)//it will return wrt kingdom power
{
    ll b[n],power[n];

    for(ll i=0;i<n;i++)
        power[i] =0;

    for(ll i=0;i<n;i++)
    {
        //copy main array to another array
        for(ll j=0;j<n;j++)
            b[j] = a[j];
        //sort array b
        for(ll k=0;k<n-1;k++)
        {
            ll temp=0;
            for(ll m=0;m<n-1-k;m++)
            {
                if(b[m]>b[m+1])
                {
                    temp = b[m];
                    b[m] = b[m+1];
                    b[m+1] = temp;
                }
            }
        }
        //cout <<"\n";

        ll z=1;
        ll p = a[i];
        while(p--)
        {
            power[i] = power[i] + b[n-z];
            z++;
            //cout<<power[i]<<"\t";
        }
        //cout<<"\n";
        //cout<<power[i]<<"\t";
    }
//    calculate smallest effective value near k
    ll min_power=0,mini=0,diff=99999999;
    for(ll i=0;i<n;i++)
    {
        mini=power[i]-k;
        if(mini>0)
        {
            if(mini < diff )
            {
                diff = mini;
                min_power = power[i];
            }
        }
    }

    if(min_power > k)
        return min_power;
    else
        return -1;
}
// Driver code
int main()
{
    ll k,n,i,f;
    cin>>k>>n;//TAKE kingdom power and no of cities
    ll a[n];
    for(i=0;i<n;i++)
        cin>>a[i];//store F-number in array
    //calculation
    f=total_power(a,n,k);
    cout<<f;
    return 0;
}
