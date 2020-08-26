https://leetcode.com/problems/unique-binary-search-trees/

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0] * (n + 1)
        arr[0: 2] = [1] * 2
        for i in range(2, n + 1):
            for j in range(i):
                arr[i] += arr[j] * arr[i - j - 1]
        return arr[-1]