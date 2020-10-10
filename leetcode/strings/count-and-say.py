https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 0: return "1"
        
        record = ["1"]
        
        if n < len(record):
            return record[n-1]
        
        for i in range(1, n):
            temp = ""
            last = record[i-1]
            anchor = 0
            for ind, digit in enumerate(last):
                char = last[ind]
                if ind+1 == len(last) or digit != last[ind+1]:
                    freq = ind - anchor + 1
                    temp += (str(freq) + char)
                    anchor = ind + 1
            record.append(temp)
        # print(record)
        return record[n-1]
        