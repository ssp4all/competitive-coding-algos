# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, alpha = [], []
        for i in logs:
            # print(i.split()[1])
            if i.split()[1].isdigit():  
                digits.append(i)  
            else:
                alpha.append(i)

        print(digits, alpha)

        alpha.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        ans = alpha + digits 
        
        return ans