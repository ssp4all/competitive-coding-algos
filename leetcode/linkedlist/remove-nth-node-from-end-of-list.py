https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

#two pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:    return head
        l = 0
        cur = head
        
        while cur:
            cur = cur.next
            l += 1
        
        tar = l - n + 1
        if tar == 1:
            return head.next
        # print(tar, l, n)
        cur = head
        l = 1
        while cur.next:
            print(l+1, cur.val)
            if l + 1 == tar:
                cur.next = cur.next.next
                break
            cur = cur.next
            l += 1
        return head
       

#from editorial
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:    return head
        
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(1, n + 2):
            second = second.next
            
        while second:
            second, first = second.next, first.next
        
        first.next = first.next.next
        return dummy.next