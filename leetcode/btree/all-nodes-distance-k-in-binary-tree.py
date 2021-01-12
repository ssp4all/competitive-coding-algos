https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = Non

#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:    return []
        parent = dict()
        def dfs(node, p):
            if not node:
                return 
            parent[node] = p
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        
        q = [(target, 0)]
        seen = {target}
        for i, (n, d) in enumerate(q):
            if d == K:
                return [n.val] + [nnn.val for nnn, dd in q[i+1:]]
            for nn in [n.left, n.right, parent[n]]:
                if not nn or nn in seen:
                    continue
                q.append((nn, d + 1))
                seen.add(n)
        return []