https://leetcode.com/problems/shortest-distance-to-a-character/
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

"""More cool """
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, j in enumerate(S):
            if j == C: prev = i
            ans.append( i - prev)
        print(ans)
        prev = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev-i)
        return ans