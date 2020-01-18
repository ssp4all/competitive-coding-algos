https://leetcode.com/problems/string-compression/

# from collections import Counter
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
            
        
        
        