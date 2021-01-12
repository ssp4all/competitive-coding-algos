/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 https://leetcode.com/problems/cousins-in-binary-tree/

/*
In a binary tree, the root node is at depth 0, 
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have 
the same depth, but have different parents.

We are given the root of a binary tree with unique values, 
and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the 
values x and y are cousins.

 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// DFS 
class Solution {
    TreeNode xP = null, yP = null;
    int xD = -1, yD = -1;
    
    public boolean isCousins(TreeNode root, int x, int y) {
        if (root == null)
            return false;
        dfs(root, x, y, 0, root);
        return xP != yP && xD == yD ? true : false;            
    }
    
    public void dfs(TreeNode root, int x, int y, int depth, TreeNode p){
        if (root == null)
            return;
        if (root.val == x ){
            xD = depth;
            xP = p;
        }
        if (root.val == y){
            yD = depth;
            yP = p;
        }
        dfs(root.left, x, y, depth + 1, root);
        dfs(root.right, x, y, depth + 1, root);
    }
}

//BFS
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Temp{
    TreeNode node;
    int d, p;
    public Temp(TreeNode node, int d, int p){
        this.node = node;
        this.d = d;
        this.p = p;
    }
}
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        if (root == null)
            return false;
        Queue q = new LinkedList();
        Temp t = new Temp(root, 0, -1);
        q.add(t);
        TreeNode node = null;
        int xd = -1, yd = -2, xp = -1, yp = -1;        
        while (!q.isEmpty()){
            Temp ele = (Temp)q.poll();
            if (ele.node == null)
                continue;
            if (ele.node.val == x){
                xd = ele.d;
                xp = ele.p;
            }
            if (ele.node.val == y){
                yd = ele.d;
                yp = ele.p;
            }
            Temp t1 = new Temp(ele.node.left, ele.d + 1, ele.node.val);
            Temp t2 = new Temp(ele.node.right, ele.d + 1, ele.node.val);
            q.add(t1);
            q.add(t2);
        }
        return (xd == yd && xp != yp) ? true : false;        
    }
}