https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
"""
Given an array of numbers, verify whether it is the correct preorder 
traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
"""

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if not preorder: return 0
        l = float('-inf')
        s = []
        for i in preorder:
            if i < l:   return 0
            while s and i > s[-1]:
                l = s.pop()
            s.append(i)
        return 1

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return 0
        h = float('inf')
        s = []
        for i in reversed(postorder):
            if i > h:   return 0
            while s and i < s[-1]:
                h = s.pop()
            s.append(i)
        return 1