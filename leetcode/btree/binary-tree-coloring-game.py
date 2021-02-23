https://leetcode.com/problems/binary-tree-coloring-game/

"""
1145. Binary Tree Coloring Game
Medium

Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

"""


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if not root:    return 1
        
        def count(node):
            if not node:    return 0
            return 1 + count(node.left) + count(node.right)
        
        l1, l2 = 0, 0
        def dfs(node):
            if not node:    return
            if node.val == x:   return node
            return dfs(node.left) or dfs(node.right)
        
        tar = dfs(root)
        l1, l2 = count(tar.left), count(tar.right)
        remaining = n - l1 - l2 - 1
            
        return remaining > l1 + l2 + 1 or l1 > remaining + l2 + 1 or l2 > remaining + l1 + 1