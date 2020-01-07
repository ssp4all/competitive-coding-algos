https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        cur = head
        prev = None
        # print(type(cur))
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # head = prev
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        cur = head
        prev = None
        
        def reverse(cur, prev):
            if not cur: 
                return prev

            next = cur.next
            cur.next = prev
            return reverse(next, cur)
            
        return reverse(cur, prev)
         