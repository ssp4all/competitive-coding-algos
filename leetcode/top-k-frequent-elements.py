https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return nums
        x = Counter(nums)
        ip = [(freq, item) for item, freq in x.items()]
        return [i[1] for i in nlargest(k, ip)]

        """Better"""
        y = x.most_common(k)
        return [i for i, j in y]