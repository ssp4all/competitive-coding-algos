https://leetcode.com/problems/group-anagrams
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        n =  len(strs)
        d = defaultdict(list)
        # dict = {}
        for i in strs:
            d[tuple(sorted(i))].append(i)
            
        return d.values()
       
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        d = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord('a')] += 1
            d[tuple(count)].append(i)
            
        return d.values()