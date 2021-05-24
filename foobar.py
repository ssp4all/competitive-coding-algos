print(list(set(x).symmetric_difference(set(y)))[0])

def solution(l):
    after_sort = sorted([map(int, e) for e in [e.split(".") for e in l]])
    res = [('.'.join(str(vv) for vv in v)) for v in after_sort]
    return res

#@author: Suraj Pawar

from math import *

def solution(total_lambs):
    # Your code here
    if not(10 <= total_lambs <= 10**9):  # edge case
        return 0

    phi, tau, eps = (1 + sqrt(5)) / 2, (1 - sqrt(5)) / 2, pow(10, -10)

    max_hunchmen = int(round(log((total_lambs + 1) * sqrt(5) + eps, phi))) - 2
    
    c1 = pow(phi, max_hunchmen + 2)
    c2 = pow(tau, max_hunchmen + 2)
    fibo_num = int(
        round( (c1 - c2) / sqrt(5)))
    
    if total_lambs + 1 == fibo_num:
        total_lambs = fibo_num
    elif total_lambs + 1 < fibo_num:
        max_hunchmen -= 1
    
    if (total_lambs + 1) & 1 == 1:
        min_hunchmen = int(log((total_lambs + 1), 2))
    else:
        min_hunchmen = int(round(log((total_lambs + 1), 2)))

    ans = abs(max_hunchmen - min_hunchmen)
    return ans
            
    
-------------------------------------------		
// package com.google.challenges; 

public class Solution {   
    public static int solution(int total_lambs) 
    {
        if (total_lambs < 10)
            return 0;
        int sum=1,a=1,b=1,temp,generous=0,stingy=1;
        while(true)
        {            
            sum+=b;
            if(sum>total_lambs)
                break;
            temp=b;
            b=a+b;
            a=temp;
            stingy++;
        }
        sum=0;
        a=1;
        while(true)
        {            
            sum+=a;
            if(sum>total_lambs)
                break;
            a=a*2;
            generous++;
        }
        sum-=a;
        if((total_lambs-sum)>=((a/2)+(a/4)))
            generous++;
        //System.out.println(stingy+" "+generous);
        return (stingy-generous);

        // Your code goes here.

    } 
}
-----------------------------------------------------------
# print(stingy - generous)
    # if not(10 <= total_lambs <= 10**9):  # edge case
    #     return 0

    # phi, tau, eps = (1 + sqrt(5)) / 2, (1 - sqrt(5)) / 2, pow(10, -10)

    # max_hunchmen = int(round(log((total_lambs + 1) * sqrt(5) + eps, phi))) - 2
    
    # c1 = pow(phi, max_hunchmen + 2)
    # c2 = pow(tau, max_hunchmen + 2)
    # fibo_num = int(
    #     round( (c1 - c2) / sqrt(5)))
    
    # if total_lambs + 1 == fibo_num:
    #     total_lambs = fibo_num
    # elif total_lambs + 1 < fibo_num:
    #     max_hunchmen -= 1
    
    # if (total_lambs + 1) & 1 == 1:
    #     min_hunchmen = int(log((total_lambs + 1), 2))
    # else:
    #     min_hunchmen = int(round(log((total_lambs + 1), 2)))

    # ans = abs(max_hunchmen - min_hunchmen)
    # return ans
            
    
        # # return 3
    # # def generous(lambs):
    # #     return int(log2(lambs + 1))

    # # def stingy(lambs):
    # #     for henchmen, total_pay in enumerate(accumulate(fibonacci())):
    # #         if total_pay > lambs:
    # #             return henchmen
    # # def fibonacci():
    # #     a, b = 1, 1
    # #     while True:
    # #         yield a
    # #         a, b = b, a + b
    # # return stingy(lambs) - generous(lambs)
    # # Your code here
    # if not(10 <= total_lambs <= 10**9):  # edge case
    #     return 0
    # generous, stingy = 0, 1
    # #fibo
    # a, b, c = 1, 1, 1
    # while 1:
    #     c += b
    #     if c > total_lambs:
    #         break
    #     a, b = b, a + b
    #     stingy += 1
    
    # c = 0
    # a = 1
    # while 1:
    #     c += a
    #     if c > total_lambs:
    #         break
    #     a *= 2
    #     generous += 1
    
    # c -= a
    # if ((total_lambs - c) >= ((a / 2) - (a / 4))):
    #     generous += 1
    
    # return stingy - generous
    # print(stingy - generous)