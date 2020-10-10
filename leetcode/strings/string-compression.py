https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        n = len(chars)
        anchor, write = 0, 0
        for read, char in enumerate(chars):
            if read + 1 == n or chars[read+1] != char:
                chars[write] = chars[read]
                write += 1
                if read > anchor:
                    for dig in str(read-anchor+1):
                        chars[write] = dig
                        write += 1
                anchor = read + 1
        return write

# https://leetcode.com/problems/count-and-say/
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
        return record[n-1]
        