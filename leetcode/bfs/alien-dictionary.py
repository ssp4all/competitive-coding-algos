from collections import defaultdict, deque
# https: // leetcode.com/problems/alien-dictionary/


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
