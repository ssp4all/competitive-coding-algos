https://leetcode.com/problems/remove-linked-list-elements

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head        
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        cur = ListNode(0)
        cur.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

"""Recursive"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head: return head
        head.next = self.removeElements(head.next, val)
        return (head.next if head.val == val else head)
    