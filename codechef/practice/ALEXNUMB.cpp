//The first line of the input contains an integer T denoting the number of test cases.
//The description of T test cases follows.
//The first line of each test case contains a single integer n denoting the number of numbers Alexandra has.
//The second line contains n space-separated distinct integers a1, a2, ..., an denoting these numbers.
#include<stdio.h>
int main()
{
    int t;
    long long int n,ans;//as numbers are too big
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld\n",&n);
        ans=(n*(n-1))/2;//calculate pairs only nC2
        printf("%lld\n",ans);
        if(t==0)
            break;
        char c;
        do
        {
            c=getchar();//no fuck given to the numbers
        }
        while(c != '\n');
    }
    return 0;
}
