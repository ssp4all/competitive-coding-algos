https://leetcode.com/problems/increasing-order-search-tree/

"""
Given the root of a binary search tree, 
rearrange the tree in in-order so that the leftmost
 node in the tree is now the root of the tree, and every 
 node has no left child and only one right child.


"""
# Time O(N), Space O(N)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root):
            if not root:    return
            yield from inorder(root.left)
            yield root.val 
            yield from inorder(root.right)
            
        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right 
        return ans.right



# Time O(N) and space O(H)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root):
            if not root:    return
            inorder(root.left)
            root.left = None
            self.cur.right = root
            self.cur = root
            inorder(root.right)
            
        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right