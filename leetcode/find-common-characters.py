# https://leetcode.com/problems/find-common-characters
from collections import Counter
class Solution:
    def commonChars(self, a: List[str]) -> List[str]:
        if not a: return a
        
        dic = (Counter(a[0]))  
        for i in a:
            dic &= Counter(i)
        return dic.elements()

class Solution:
    def commonChars(self, a: List[str]) -> List[str]:
		cnt  = [float('inf')] * 26
		for s in a:
			cnt2 = [0] * 26
			for c in s:
				cnt2[ord(c) - ord('a')] += 1
			cnt = [min(cnt[i], cnt2[i]) for i in range(26)]
		return [c for k, c in zip(cnt, string.ascii_lowercase) for _ in range(k)]
		