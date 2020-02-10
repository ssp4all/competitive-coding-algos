https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2: return num1 or num2
        op = []
        carry = 0
        num1, num2 = list(num1), list(num2)
        
        while len(num1) > 0 or len(num2) > 0:
            n1 = (ord(num1.pop()) - ord("0")) if len(num1) > 0 else 0
            n2 = (ord(num2.pop()) - ord("0")) if len(num2) > 0 else 0
            temp = n1 + n2 + carry
            op.append(temp % 10)
            carry = temp // 10
            
        if carry:   op.append(carry)

        return "".join([str(i) for (i) in op[::-1]])
         
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
        
            
            
            
            
        