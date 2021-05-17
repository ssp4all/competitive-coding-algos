https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the
 values of the kth node from the beginning and the kth node 
 from the end (the list is 1-indexed).
"""

# One pass solution
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:    return head 
        
        slow, fast = head, head 
        
        for _ in range(k - 1):
            fast = fast.next 
        
        first = fast 
        
        while fast.next:
            slow, fast = slow.next, fast.next 
        
        slow.val, first.val = first.val, slow.val 
        
        return head