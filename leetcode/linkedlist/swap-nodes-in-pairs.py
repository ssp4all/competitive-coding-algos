https://leetcode.com/problems/swap-nodes-in-pairs/

"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:    return head
        
        cur = head
        if cur.next:
            head = cur.next
        else:
            return head
        while cur and cur.next:
            next = cur.next
            tmp = cur.next.next
            next.next = cur
            if tmp and tmp.next:
                cur.next = tmp.next
            else:
                cur.next = tmp
            cur = tmp
        return head

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:    return head
        
        next = head.next
        head.next = self.swapPairs(head.next.next)
        next.next = head
        return next