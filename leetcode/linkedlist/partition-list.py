https://leetcode.com/problems/partition-list/


"""
Given the head of a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:    return head 
        
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        cur = head 
        
        while cur:
            if cur.val < x:
                before.next = cur 
                before = before.next 
            else:
                after.next = cur 
                after = after.next
            cur = cur.next
        after.next = None
        
        before.next = after_head.next 
        return before_head.next