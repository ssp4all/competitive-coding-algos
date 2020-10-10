https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
"""

from collections import deque
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:    return 0
        dq = preorder.split(",")
        if dq[0] == "#" and len(dq) > 1 :    return 0
        elif dq[0] == "#" and len(dq) == 1:   return 1
        dq = deque(dq)
        slots = 1
        while dq:
            x = dq.popleft()
            if x != "#":
                slots += 1
            else:
                slots -= 1
            if slots <= 0 and dq:
                return 0
        return slots == 0
        