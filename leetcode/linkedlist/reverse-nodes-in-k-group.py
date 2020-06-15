https://leetcode.com/problems/reverse-nodes-in-k-group/

"""
Given a linked list, reverse the nodes of a linked list k 
at a time and return its modified list.

k is a positive integer and is less than or equal to the 
length of the linked list. If the number of nodes is not a 
multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:    return head
        
        def helper(head, k):
            prev, cur = None, head
            while k:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                k -= 1
            return prev
        cur = head
        l = 0
        while cur and l < k:
            cur = cur.next
            l += 1
        if l == k:
            rhead = helper(head, k)
            head.next = self.reverseKGroup(cur, k)
            return rhead
        return head
        
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:    return head
        
        head2 = jump = ListNode(-1)
        left = right = head
        while True:
            cnt = 0
            while cnt < k and right:
                cnt += 1
                right = right.next
            if cnt == k:
                pre, cur = right, left
                for _ in range(k):
                    next = cur.next
                    cur.next = pre
                    pre = cur
                    cur = next
                jump.next = pre
                jump = left
                left = right
                    
            else:
                return head2.next
            