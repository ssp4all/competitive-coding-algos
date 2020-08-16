#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'consecutive' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER num as parameter.
 */

int consecutive(long N) {
    int ans = 0;
    for (int i = 1; i <= N; N -= i++)
        N % i ? ans : ++ans;
    return ans - 1; 
}
---------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#
from collections import Counter, defaultdict

def droppedRequests(requestTime):  
    if not requestTime:     return 0
    n = len(requestTime)
    if n <= 3: return 0
    count = Counter(requestTime) 
    cache = defaultdict(int)

    for i in range(requestTime[0], requestTime[-1]+1):
        cache[i] = cache[i-1] + count[i]

    for i in range(3, n):
        t1 , t2 = 0, 0
        if requestTime[i]-10 in cache: t1 = cache[requestTime[i]-10]
        if requestTime[i]-60 in cache: t2 = cache[requestTime[i]-60]
        if requestTime[i-3] == requestTime[i]: requestTime[i-3] = '$'
        elif i+1 - t1 > 20: requestTime[i] = '$'
        elif i+1 - t2 > 60: requestTime[i] = '$'
    return requestTime.count('$')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requestTime_count = int(input().strip())

    requestTime = []

    for _ in range(requestTime_count):
        requestTime_item = int(input().strip())
        requestTime.append(requestTime_item)

    result = droppedRequests(requestTime)

    fptr.write(str(result) + '\n')

    fptr.close()
