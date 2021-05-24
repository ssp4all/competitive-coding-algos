https://leetcode.com/problems/\
	construct-binary-tree-from-preorder-and-inorder-traversal/
"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: return
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind + 1:])
        return root 

https://leetcode.com/problems/\
	construct-binary-tree-from-inorder-and-postorder-traversal

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.right = self.buildTree(inorder[ind + 1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root