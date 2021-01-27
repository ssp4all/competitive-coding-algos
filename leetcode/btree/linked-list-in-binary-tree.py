https://leetcode.com/problems/linked-list-in-binary-tree

"""
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond
 to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
"""

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def check(head, node):
            if not head:    return 1
            if not node:    return 0
            return node.val == head.val and \
                        (check(head.next, node.left,) or \
                            check(head.next, node.right))
        if not head: return 1
        if not root: return 0

        return check(head, root) or \
                    self.isSubPath(head, root.left) or \
                        self.isSubPath(head, root.right)