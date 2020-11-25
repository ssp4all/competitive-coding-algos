/*Monica wants to buy exactly one keyboard and one USB drive from her favorite electronics store.
The store sells different brands of keyboards and  different brands of USB drives.
Monica has exactly  dollars to spend, and she wants to spend as much of it as possible
(i.e., the total cost of her purchase must be maximal).
Given the price lists for the store's keyboards and USB drives,
 find and print the amount money Monica will spend.
 If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead++.
*/
#include<stdio.h>
int main()
{
    int amt,kb,usb;
    scanf("%d%d%d",&amt,&kb,&usb);
    int i,k[1000],u[1000],j;

    for(i=0;i<kb;i++)
        scanf("%d",&k[i]);

    for(i=0;i<usb;i++)
        scanf("%d",&u[i]);
    int max=-1;
    for(i=0;i<kb;i++)
    {
        for(j=0;j<usb;j++)
        {
            int temp;
            temp = k[i] + u[j];
            if(temp>amt)
                break;
            if(temp > max)
            {
                max=temp;
            }
        }
    }
    printf("%d",max);
    return 0;
}
/*
/*
//Problem: https://www.hackerrank.com/challenges/electronics-shop
//Java 8
/*
Initial Thoughts:
We can compare all pairs and if they are > max and <= s
then we set it as the new max and return after checking
all pairs
Optimization:
If we sort 1 in descending and the other in ascending
order we only have to visit each element once, because
we can make use of the fact that the sum of the element
following the current will be greater/less than the
current sum depending on the direction we iterate from
Time Complexity: O(n+m (log (n+m))) //We sort in n+m (log (n+m)) then iterate in n+m
Space Complexity: O(1) //We consider the arrays as given
*/
/*
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int n = in.nextInt();
        int m = in.nextInt();
        Integer[] keyboards = new Integer[n];
        for(int keyboards_i=0; keyboards_i < n; keyboards_i++){
            keyboards[keyboards_i] = in.nextInt();
        }
        int[] pendrives = new int[m];
        for(int pendrives_i=0; pendrives_i < m; pendrives_i++){
            pendrives[pendrives_i] = in.nextInt();
        }

        Arrays.sort(keyboards, Collections.reverseOrder());//Descending order
        Arrays.sort(pendrives);//Ascending order

        int max = -1;
        for(int i = 0, j = 0; i < n; i++){
            for(; j < m; j++){
                if(keyboards[i]+pendrives[j] > s) break; //This prevents j from incrementing
                if(keyboards[i]+pendrives[j] > max)
                    max = keyboards[i]+pendrives[j];
            }
        }
        System.out.println(max);
    }
}
*/
