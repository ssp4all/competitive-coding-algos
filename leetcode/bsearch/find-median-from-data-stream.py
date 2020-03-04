https://leetcode.com/problems/find-median-from-data-stream

from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ip = []

    def addNum(self, num: int) -> None:
        x = bisect_left(self.ip, num)
        
        self.ip.insert(x, num)

    def findMedian(self) -> float:
        
        if not self.ip: return 0
        
        n = len(self.ip)
        if n & 1:
            return self.ip[n // 2]
        else:
            t = n // 2
            a = self.ip[t]
            b = self.ip[t - 1]
            # print(a, b)
            return (a + b) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()