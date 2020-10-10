https://leetcode.com/problems/reorder-list/

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:    return None
        cache = {}
        cur = head
        i = 1
        while cur:
            cache[i] = cur
            i += 1
            cur = cur.next
            
        l = len(cache)
        i, j = 1, l
        
        head2 = ListNode(0)
        cur = head2
        while i <= j:
            cur.next = cache[i]
            cur = cur.next
            
            cur.next = cache[j]
            cur = cur.next
            cur.next = None
            i += 1
            j -= 1
            
        return head    


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:    return None
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(cur, prev):
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
            
        head2 = reverse(slow.next, None)
        slow.next = None
        
        while head and head2:
            t1 = head.next
            t2 = head2.next
            head2.next = head.next
            head.next = head2
            head = t1
            head2 = t2