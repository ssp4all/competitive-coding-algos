//c program to Pooja would like to withdraw X $US from an ATM.
//The cash machine will only accept the transaction if X is a multiple of 5,
//and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
//For each successful withdrawal the bank charges 0.50 $US.
//Calculate Pooja's account balance after an attempted transaction.
#include<stdio.h>

int main()
{
    int amt;
    float balance;
    scanf("%d",&amt);
    scanf("%f",&balance);
    if(amt%5 == 0)
    {
        if(balance >= amt +0.5)
            printf("%.2f",balance-amt-0.5);
        else
            printf("\n%.2f",balance);
    }
    else
    {
        printf("%.2f",balance);
    }

    return 0;
}
