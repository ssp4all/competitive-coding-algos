# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        # if len(s) == 1: return False
        if len(s) % 2 != 0: return False
        stack = []
        for i in s:
            if i in ['{', '(', '[']:
                stack.append(i)
            elif i in ['}', ']', ')']:
                if len(stack) == 0: return False
                x = stack.pop()
                if x == '(' and i != ')':
                    return False
                elif x == '[' and i != ']':
                    return False
                elif x == '{' and i != '}':
                    return False
        return len(stack) == 0
        #     return True   
        # else:
        #     return False