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

from collections import Counter
from heapq import heappush, heappop, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:    return nums
        n = len(nums)
        xx = Counter(nums)
        heap = []
        ip = [(freq, num) for num, freq in xx.items()]
        for i in range(len(ip)):
            if len(heap) == k:
                heappushpop(heap, ip[i])
            else:
                heappush(heap, ip[i])
        return [j for i, j in heap]