"""
Find the Town Judge

In a town, there are N people labelled from 1 to N.  
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing 
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if not n or not trust or not trust[0]:  return 0
        model = [set() for _ in range(n + 1)]
        p = [0] * (n + 1)
        p[0] = 1
        for i, j in trust:
            model[j].add(i)
            p[i] = 1
        
        for i in range(1, n + 1):
            if p[i] == 0 and len(model[i]) == n - 1:
                return iq
        # print(p, model)
        return -1
        