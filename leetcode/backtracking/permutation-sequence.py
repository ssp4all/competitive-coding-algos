https://leetcode.com/problems/permutation-sequence/

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ip = [i for i in range(1, n + 1)]
        n = len(ip)
        def helper(ip, st, ans):
            if n - st == 1:
                ans[len(ans) + 1] = tuple(ip)
                if not k:
                    return ans

            for i in range(st, n):
                ip[st], ip[i] = ip[i], ip[st]
                if len(ans) == k:
                    return ans
                ans = helper(ip, st + 1, ans)
                ip[st], ip[i] = ip[i], ip[st]
            return ans

        x = helper(ip, 0, dict())
        print(x)
        return "".join(map(str, x[k]))

# Optimal
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ip = []
        fact = 1
        for i in range(1, n + 1):
            ip += [i]
            fact *= i
        print(ip, fact)
        ind = k - 1
        ans = []
        for i in range(n):
            fact //= (n - i)
            loc = (ind // fact)
            ans += [str(ip[loc])]
            del ip[loc]
            ind -= (loc * fact)
            # print(ip, fact, loc, ans, ind)
            
        return "".join(ans)