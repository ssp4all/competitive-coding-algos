https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ip1 = list(map(int, list(num1)))
        ip2 = list(map(int, list(num2)))
        
        r1, r2 = len(ip1) - 1, len(ip2) - 1
        if r1 < r2:
            ip1, ip2 = ip2, ip1
            r1, r2 = r2, r1
        carry = 0
        while (r1 >= 0 and r2 >= 0):
            summ = ip1[r1] + ip2[r2] + carry
            if (summ) >= 10:
                ip1[r1] = (summ) % 10
                carry = 1
            else:
                ip1[r1] = summ
                carry = 0
            r1 -= 1
            r2 -= 1
            
        while carry and r1 >= 0:
            summ = ip1[r1] + carry
            if summ >= 10:
                summ %= 10
                ip1[r1] = summ
            else:
                ip1[r1] = summ
                carry = 0
            r1 -= 1
            if not carry:   break
        if carry and r1 < 0:
            ip1.insert(0, 1)
        return "".join(map(str, ip1))
        
            
            
            
            
            