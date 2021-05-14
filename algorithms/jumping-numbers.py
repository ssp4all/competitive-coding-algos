https://www.geeksforgeeks.org/print-all-jumping-numbers-smaller-than-or-equal-to-a-given-value/

# find all jumping numbers 
# A jumping number is where adjacent numbers differ by 1 

import collections 

LIMIT = 20
ans = set()  

def bfs(start):
    dq = collections.deque([start])
    while dq:
        num = dq.popleft()
        if num > LIMIT: continue
        last_digit = num % 10  

        if last_digit == 0:
            curr = num * 10 + last_digit + 1
            dq += [curr]
            ans.add(curr)

        elif last_digit == 9:
            curr = num * 10 + last_digit - 1
            dq += [curr]
        else:
            curr1 = num * 10 + last_digit + 1
            curr2 = num * 10 + last_digit - 1
            dq += [curr1, curr2]
            ans.add(curr1) 
            ans.add(curr2)

for i in range(1, 10):
    bfs(i) #start

print(ans)

##########################################################################

https://leetcode.com/problems/numbers-with-same-consecutive-differences/

"""
Return all non-negative integers of length n such that the 
absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading
 eros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
"""


# TC:O( 9 * 2 ^ N - 1 ), SC:O(2 ^ N)
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        #BFS         
        def bfs(num, ans):
            
            dq = deque([(num, n - 1)])
            while dq:
                no, digits = dq.popleft()
                if digits == 0:
                    ans.add(no)
                    continue 
                last_digit = no % 10 
                next_digits = [last_digit + k, last_digit - k]
                
                for dig in next_digits:
                    if 0 <= dig < 10:
                        dq += [(no * 10 + dig, digits - 1)]
                        
        ans = set()
        for i in range(1, 10):
            bfs(i, ans)
            
        return ans