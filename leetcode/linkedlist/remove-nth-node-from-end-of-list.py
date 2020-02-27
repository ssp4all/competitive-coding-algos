https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
       

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:    return head
    	slow = fast = head

    	for _ in range(n):
    		fast = fast.next

		while fast.next:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next
		return head
