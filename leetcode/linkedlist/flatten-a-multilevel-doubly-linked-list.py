https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
You are given a doubly linked list which in addition to the 
next and previous pointers, it could have a child pointer, 
which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, 
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, 
doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:
The multilevel linked list in the input is as follows:
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:    return head
        cur = head
        while cur:
            if not cur.child:
                cur = cur.next
                continue
            p = temp = cur.child
            while temp:
                p = temp
                temp = temp.next
            p.next = cur.next
            if cur.next:
                cur.next.prev = p
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
        return head