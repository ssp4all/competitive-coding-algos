https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
Given a binary search tree, write a function kthSmallest 
to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:    return -1
    
        def helper(node):
            nonlocal k
            if not node:    return float('-inf')
            x = helper(node.left)
            if x != float('-inf'):
                return x
            k -= 1
            if (k == 0):
                return node.val
            x = helper(node.right)
            return x
        x = helper(root)
        return x
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:    return -1
        s = []
        node = root
        while s or node:
            if node:
                s += [node]
                node = node.left
            else:
                if not s:
                    continue
                node = s.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right