https://leetcode.com/problems/super-palindromes/


"""
Let's say a positive integer is a super-palindrome 
if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented 
as strings, return the number of super-palindromes 
integers in the inclusive range [left, right].

Example 1:

Input: left = "4", right = "1000"
Output: 4
"""

class Solution(object):
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        ans = 0

        # count odd length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        # count even length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        return ans