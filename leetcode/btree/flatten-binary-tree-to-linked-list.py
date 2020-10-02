https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def helper(node):
            nonlocal prev
            if not node:    return 
            helper(node.right)
            helper(node.left)
            node.right = prev
            node.left = None
            prev = node
        helper(root)
        return root