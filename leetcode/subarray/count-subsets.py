https://leetcode.com/discuss/interview-question/275785/facebook-phone-screen-count-subsets

"""
Input:

Given an array A of
-positive
-sorted
-no duplicate
-integer

A positive integer k

Count of all such subsets of A,
Such that for any such subset S,
Min(S) + Max(S) = k
subset should contain atleast two elements
"""

ip = [2, 4, 5, 7]
k = 8
cnt = 0
n = len(ip)
ip.sort()

l, r = 0, n - 1
while l <= r:
    print(ip[l :  r + 1])
    sum_ = ip[l] + ip[r]
    if sum_ == k:
        cnt += (1 << (r - l))
        l += 1
        r -= 1
    elif sum_ < k:
    	l += 1 
    else:
        r -= 1
print(cnt)