https://leetcode.com/problems/relative-sort-array/
https://leetcode.com/problems/custom-sort-string

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1 and arr2: return arr1
        
        x = Counter(arr1)
        op = []
        for i in arr2:
            op += [i]*x[i]
            del x[i]
        for i, j in sorted(x.items()):
            op += [i]*j
        # print(op)
        return op

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {j:i for i, j in enumerate(arr2)}
        return sorted(arr1, key=lambda x:(d.get(x, 1000+x)))

"""
For string
"""
class Solution:
    def customSortString(self, s: str, t: str) -> str:
        if not s and not t: return s
        d = {j:i for i, j in enumerate(s)}
        print(d)
        return "".join(sorted(t, key= lambda x:(d.get(x, 26+ord(x)))))