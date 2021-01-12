#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s = list(s)
    if s[8:9][0] == 'P':
        n0 = int(s[0])
        n1 = int(s[1])
        n = 10*n0+n1
        if n+12 < 24:
            n = n + 12
        n0 = int(n/10)
        n1 = n%10
        # print(s)
        # print(n0,n1)
        s[0] = n0
        s[1] = n1
    else:
        n0 = int(s[0])
        n1 = int(s[1])
        n = 10*n0+n1
        print(n)
        if n == 12:
            n = 0
        n0 = int(n/10)
        n1 = n%10
        s[0] = n0
        s[1] = n1
    
    op = s
    op.pop()
    op.pop()
    op = " ".join(str(x) for x in op)
    op = (op.replace(' ',''))
    return op
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
