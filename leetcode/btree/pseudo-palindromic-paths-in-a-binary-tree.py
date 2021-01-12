https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/


"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.


Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Input: root = [2,3,1,3,1,null,1]
Output: 2 
"""

#TC: O(N), SC:O(N) worst cast for recursion depth
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root:    return 1
        
        res = 0 # total possible permutations 
        freq = {i: 0 for i in range(1, 10)}
        
        def dfs(node, count, freq):
            nonlocal res
            freq[node.val] += 1
            count += -1 if freq[node.val] % 2 == 0 else 1
            if not node.left and not node.right: 
                if count <= 1:
                    res += 1
                freq[node.val] += 1
                return 
            if node.left:   dfs(node.left, count, freq)
            if node.right:  dfs(node.right, count, freq)
            freq[node.val] -= 1
            # count += -1 if freq[node.val] % 2 == 0 else 1
            
        
        dfs(root, 0, freq)
        return res