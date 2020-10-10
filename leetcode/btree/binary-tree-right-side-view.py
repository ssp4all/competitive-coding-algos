https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        MD = -1
        depths = {}
        stack = [(root, 0)]
        while stack:
            node, dep = stack.pop()
            if not node:
                continue
            MD = max(MD, dep)
            depths.setdefault(dep, node.val)
            
            stack.append((node.left, dep+1))
            stack.append((node.right, dep+1))
            
        return [depths[dep] for dep in range(MD+1)]