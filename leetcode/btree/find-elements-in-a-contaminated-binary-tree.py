https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree

"""
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
 
"""

class FindElements:

    # TC:O(N), SC:O(H)
    def __init__(self, root: TreeNode):
        if not root:    return
        self.in_tree = set()
        queue = [(root, 0)]
        for node, d in queue:
            if not node:    continue
            self.in_tree.add(d)
            queue += [(node.left, 2 * d + 1), (node.right, 2 * d + 2)]
    #TC:O(1) 
    def find(self, target: int) -> bool:
        return target in self.in_tree


# Upsolving 
# TC:O(lgN), SC:O(1)

"""
Idea here is to add 1 to target then 
it will like 
            0 (1)
    1 (10)              2 (11)
3 (100)       4(101)   5 (110)      6 (111)

"""
def find(self, target: int) -> bool:
        binary = bin(target + 1)[3:]                  
        # remove the useless first `1`
        index = 0
        root = self.root                                    
        # use a new pointer `root` to traverse the tree
        while root and index < len(binary): 
            # traverse the binary number from left to right
            if root.val == target:
                return True
            if  binary[index] == '0':  # if it's 0, we have to go left
                root = root.left
            else:  # if it's 1, we have to go right
                root = root.right
            index += 1
        return False