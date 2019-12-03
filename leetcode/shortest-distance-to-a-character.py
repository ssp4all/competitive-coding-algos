# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        if not S:   return []
        temp = []
        for i, c in enumerate(S):
            if c == C:
                temp.append(i)
        print(temp)
        ans = []
        tt = list(range(len(S)))
        print(tt)
        for i in tt:
            y = min(temp, key=lambda x:abs(x-i))
            ans.append(abs(y-i))
        return ans