https://leetcode.com/problems/delete-nodes-and-return-forest/

"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:    return []
        to_delete = set(to_delete)
        def dfs(node, heads):
            if not node:    return 
            node.left = dfs(node.left, heads)
            node.right = dfs(node.right, heads)
            if node.val in to_delete:
                if node.left:   heads += [node.left]
                if node.right:  heads += [node.right]
                return
            return node
        heads = []
        if root.val not in to_delete:   
            heads += [root]
        
        dfs(root, heads)
        return heads