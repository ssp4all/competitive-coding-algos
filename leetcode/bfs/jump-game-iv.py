https://leetcode.com/problems/jump-game-iv/

"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

"""
# TC: O(N), SC: O(N)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1



  """
	[1,1,1] -> {1:[]}  [2,1]
	[1,2,3,4,2.2]
	[7,7,7,11] ->{2, 1}
	v = {0, 2}
  """