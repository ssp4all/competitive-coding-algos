https://leetcode.com/problems/parallel-courses/

"""
There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.
"""

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0 for i in range(n)]
        
        # Build a graph and set the indegree of the corresponding nodes
        # using pre-1 as nodes are labeled 1 to n
        for pre,course in relations:
            graph[pre-1].append(course-1)
            indegree[course-1]+=1
        
        # Find the starting nodes (nodes with indegree=0)
        starting_nodes = deque([idx for idx,x in enumerate(indegree) if x==0])
        # If we don't find a single node with 0 indegree that means that there is a cycle in the graph
        if not starting_nodes:
            return -1
        # Start a basic BFS from all the starting nodes
        ans = 0
        # courses not taken yet are represented by remaining
        # increment ans whenever new level starts
        remaining = n
        while starting_nodes:
            ans+=1
            remaining-=len(starting_nodes)
            for i in range(len(starting_nodes)):
                current_node = starting_nodes.popleft()
                for child in graph[current_node]:
                    indegree[child]-=1
                    # Topo sort Kahn's
                    if indegree[child]==0:
                        starting_nodes.append(child)
        # If we have visited all the nodes in the graph then we return the ans else -1
        return ans if remaining == 0 else -1
            