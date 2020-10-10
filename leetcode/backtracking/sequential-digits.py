https://leetcode.com/problems/sequential-digits/

"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            cur =  i
            nxt = i + 1
            while cur <= high and nxt < 10:
                cur = cur * 10 + nxt
                if low <= cur <= high:
                    ans += [cur]
                nxt += 1
        return sorted(ans)

#backtracking below - idea is to keep appeding number

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        def check(cur):
            if len(cur) > 1 and int(cur[-1]) - int(cur[-2]) == 1:
                return 1
            return 0
        
        def backtrack(cur, ans):
            num = int("".join(cur))
            if low <= num <= high and check(cur):
                ans += [num]
            
            if int(cur[-1]) > 8:
                return
            
            last_digit = int(cur[-1]) + 1
            if num * 10 + last_digit <= high:
                backtrack(cur + [str(last_digit)], ans)
        
        for i in range(1, 10):
            backtrack([str(i)], ans)
        return sorted(ans)