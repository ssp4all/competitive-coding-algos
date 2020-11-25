https://leetcode.com/problems/maximum-width-of-binary-tree/

"""
Given a binary tree, write a function to get the maximum width of the given tree. 
The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, where the null 
nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
"""

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:    return 0
        
        dq = collections.deque([(root, 0, 0)])
        ans = 0
        prev = 0
        left = 0
        while dq:
            # print(dq)
            n, d, p = dq.popleft()
            if not n:  
                continue
            
            if prev != d:
                prev = d
                left = p
            ans = max(ans, p - left +1)
            dq.extend([(n.left, d + 1, 2 * p), (n.right, d + 1, 2 * p + 1)])
        # print(lev)
        return ans

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:    return 0
        
        q = [(root, 1)]
        ans = 0
        while q:
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            new_list = []
            for node, d in q:
                if node.left:   new_list += [(node.left, 2 * d)]
                if node.right:  new_list += [(node.right, 2 * d + 1)]
            q = new_list
        return ans