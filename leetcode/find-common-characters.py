# https://leetcode.com/problems/find-common-characters
from collections import Counter
class Solution:
    def commonChars(self, a: List[str]) -> List[str]:
        if not a: return a
        
        dic = (Counter(a[0]))  
        for i in a:
            dic &= Counter(i)
        return dic.elements()