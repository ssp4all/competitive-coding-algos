https://www.geeksforgeeks.org/count-number-increasing-subsequences-size-k/

"""
Given an array arr[] containing n integers. The problem is to count
 number of increasing subsequences in the array of size k.

Examples:

Input : arr[] = {2, 6, 4, 5, 7}, 
            k = 3
Output : 5
The subsequences of size '3' are:
{2, 6, 7}, {2, 4, 5}, {2, 4, 7},
{2, 5, 7} and {4, 5, 7}.

Input : arr[] = {12, 8, 11, 13, 10, 15, 14, 16, 20}, 
            k = 4
Output : 39
"""

arr = [1, 2, 3]
n = len(arr)
k = 3

dp = [[0]* n for _ in range(k)]

for i in range(n):
    dp[0][i] = 1

for i in range(1, k):
    for j in range(i, n):
        for k in range(i - 1, j):
            if arr[k] < arr[j]:
                dp[i][j] += dp[i - 1][j]

count = sum(dp[-1])
print(count)