https://leetcode.com/problems/top-k-frequent-words

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words: return words
        x = Counter(words)
        y = sorted(x, key=lambda z:(-x[z], z))[:k]
        # y = nlargest(k, x, key=lambda z:(-x[z], z))
        return y

from collections import Counter
from heapq import nsmallest, heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words: return words
        x = Counter(words)
        h = [(-freq, w) for w, freq in x.items()]
        return [j for i, j in nsmallest(k, h, key=lambda z:(z[0], z[1]))]
        or
        return [i[1] for i in nsmallest(k, h)]
        or
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]