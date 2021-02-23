https: // leetcode.com/problems/alien-dictionary/

"""
There is a new alien language that uses the English alphabet. 
However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, 
where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. 
If the given input is invalid, return "". If there are multiple valid solutions, 
return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
"""

# TC:O(time to build adjacency)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        temp = set("".join(words))
        graph = defaultdict(set)

        indegree = {i: 0 for i in temp}

        for pair in zip(words, words[1:]):
            for i, j in zip(*pair):
                if i != j:
                    graph[i].add(j)
                    indegree[j] += 1
                    break

        que = deque(list(filter(lambda t: (indegree[t] == 0), temp)))
        # print(graph, que)
        ans = ""
        while que:
            i = que.popleft()
            ans += i
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    que.append(j)
        return ans * (len(ans) == len(temp))
