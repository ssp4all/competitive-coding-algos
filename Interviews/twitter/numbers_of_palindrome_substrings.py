#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(S):
    # Write your code here
    N = len(S) 
    ans = set([]) # needed as we ned to remember old elements
    S = S +'#' # used to traverse last element
    for center in range(2*N - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans.add(S[left:right+1])
            left -= 1
            right += 1
    return len(ans)
if __name__ == '__main__':