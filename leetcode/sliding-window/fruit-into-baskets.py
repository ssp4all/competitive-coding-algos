https://leetcode.com/problems/fruit-into-baskets/
"""
[1,1,6,5,6,6,1,1,1,1]
[0,1,6,6,4,4,6]
[3,3,3,1,2,1,1,2,3,3,4]
[1,2,1]
[1,2,3,2,2]
[1,2,3,4,5,6]
[1,2,1,2,1,2,3]
"""

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:    return 0
        
        n = len(tree)
        anchor = 0
        bucket = {}
        ans = 0
        for i, val in enumerate(tree):
            if val not in bucket and len(bucket) < 2:
                bucket[val] = [i, i]
            elif val in bucket:
                bucket[val][1] = i
            elif val not in bucket and len(bucket) == 2:
                mv = min(bucket.items(), key=lambda x:x[1][1])
                del bucket[mv[0]]
                anchor = mv[1][1] + 1   
                bucket[val] = [i, i]
            ans = max(ans, i - anchor + 1)
        return ans
    
   