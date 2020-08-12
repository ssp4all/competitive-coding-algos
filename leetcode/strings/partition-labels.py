https://leetcode.com/problems/partition-labels

"""
763. Partition Labels
Medium

2542

120

Add to List

Share
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s: return []
        n = len(s)
        # print(n)
        cache = defaultdict(list)
        for ind, ch in enumerate(s):
            if len(cache[ch]) > 1:
                cache[ch][1] = ind
            else:
                cache[ch] = [ind, ind]
        x = list(cache.values())   
        print(x)
        #interval generated now merge them
        prevA, prevB = x[0]
        
        l, r = 1, len(x) - 1
        while l <= r:
            a, b = x[l]
            if prevA <= a <= prevB:
                x[l - 1] = [min(a, prevA), max(b, prevB)]
                prevA, prevB = [min(a, prevA), max(b, prevB)]
                del x[l]
                r -= 1
            else:
                prevA, prevB = x[l]
                l += 1
    
        return [j - i + 1 for i, j in x]
        