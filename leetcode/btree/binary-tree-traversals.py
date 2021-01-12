https://leetcode.com/problems/binary-tree-postorder-traversal/

# Various tree traversal algorithms (iteratively)

# inorder
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return [] 
        arr = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack += [cur]
                cur = cur.left
            cur = stack.pop()
            arr += [cur.val]
            cur = cur.right
        return arr

# preorder
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return [] 
        arr = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                arr += [cur.val]
                stack += [cur]
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return arr
        
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return [] 
        arr = []
        stack = [root]
        cur = None
        while cur or stack:
            cur = stack.pop()
            arr += [cur.val]
            stack += [cur.right, cur.left]
        return arr

# post
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return [] 
        arr = []
        stack = [root]
        cur = None
        while cur or stack:
            cur = stack.pop()
            if not cur: continue
            arr += [cur.val]
            stack += [cur.left, cur.right]
        return arr[::-1]