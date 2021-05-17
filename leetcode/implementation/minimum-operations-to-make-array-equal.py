
https://leetcode.com/problems/minimum-operations-to-make-array-equal/


"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for 
all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n 
and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 
and arr[y] += 1). The goal is to make all the elements of the array equal. 
It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number 
of operations needed to make all the elements of arr equal.

Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]

"""

class Solution:
    def minOperations(self, n: int) -> int:
        tar = [] 
        sum_ = 0
        
        for i in range(n):
            tar += [2 * i + 1]
            sum_ += 2 * i + 1 
        
        sum_ /= n 
        ans = 0
        for i in range(n // 2 + (1 if n % 2 != 0 else 0)):
            ans += abs(tar[i] - sum_)
        
        return int(ans)
        

#upsolving 
class Solution {
    public int minOperations(int n) {
    // Take care of overflow if n is too large.
        if(n%2==1){
            n/=2;
            return (n*(n+1));
        }        
        n/=2;
        return n*n;
    }
}