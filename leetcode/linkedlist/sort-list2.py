https://leetcode.com/problems/sort-list/


"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, list1, list2):
        if not list1 and not list2: return None
        if not list1 or not list2:  return list1 or list2
        
        head = cur = ListNode(-999)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return head.next
        
        
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:    return head
        
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left, right)