https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {
                "2": ['a', 'b', 'c'],
                "3": ['d', 'e', 'f'],
                "4": ['g', 'h', 'i'],
                "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'],
                "7": ['p', 'q', 'r', 's'],
                "8": ['t', 'u', 'v'],
                "9": ['w', 'x', 'y', 'z']
            }
        
        def backtrack(comb, ND):
            if not ND:
                op.append(comb)
            else:
                for letter in d[ND[0]]:
                    backtrack(comb+letter, ND[1:])
        op = []
        backtrack("", digits)
        return op

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {
                "2": ['a', 'b', 'c'],
                "3": ['d', 'e', 'f'],
                "4": ['g', 'h', 'i'],
                "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'],
                "7": ['p', 'q', 'r', 's'],
                "8": ['t', 'u', 'v'],
                "9": ['w', 'x', 'y', 'z']
            }
        
        n = len(digits)
        ip = []
        for i in range(n):
            ip.append(d[digits[i]])
        op = []
        
        def product(a, b):
            for i in a:
                for j in b:
                    op.append(i+j)
        if len(digits) > 1:
            product(ip[0], ip[1])
        else:
            return ip[0]
        for i in range(2, n):
            product(op[:], ip[i])
        stop = -1
        for i in range(len(op)):
            if len(op[i]) < len(digits):
                stop = i
        return op[stop+1:]
        