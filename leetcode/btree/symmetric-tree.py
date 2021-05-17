https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:    return 1
        l, r = deque([root.left]), deque([root.right])
        while l and r:
            a, b = l.popleft(), r.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return 0
            l += [a.left, a.right]
            r += [b.right, b.left]
        if not l and not r:
            return 1
        return 0     
    
#         def helper(a, b):
#             if not a and not b:
#                 return 1
#             if not a or not b:
#                 return 0
#             return a.val == b.val and \
#                 helper(a.left, b.right) and helper(a.right, b.left)
        
#         return helper(root.left, root.right)
            

##################################
upsolving find maxiums symmetric-tree 

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:    return 1 
        maxi = None
        maxiS = 0
        def check(node, s):
            nonlocal maxi, maxiS
            
            if not node:    return 0
            left, right = [""], [""]
            le = check(node.left, left)
            ri = check(node.right, right)
            size = le + ri + 1
            if left[0] == right[0]:
                if maxiS < size:    
                    maxi = node 
                    maxiS = size
            
            s[0] += "*" + left[0] + "*"
            s[0] += "*" + str(node.val) + "*"
            s[0] += "*" + right[0] + "*"
            return size
            
        org = [""]
        check(root, org)
        return maxi