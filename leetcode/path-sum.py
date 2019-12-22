# https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: return False
        
        def dfs(node, prev, sum):
            if node is None:
                return False
            
            t = node.val + prev
            if node.left is None and node.right is None:
                if t == sum:
                    return True
                else:
                    return False
                
            if dfs(node.left, t, sum) or dfs(node.right, t, sum):
                return True
            return False
        
        return dfs(root, 0, sum)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: return False
        
        # if root.val == sum: return True
        
        sum -= root.val
        
        if root.left is None and root.right is None and sum == 0:
            return True
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
        