https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Inplace
class Solution:
    def oddEvenList(self, head):
        if not head:    return head
        
        h1 = c1 = head
        h2 = c2 = head.next
        
        while c1 and c2 and c2.next and c1.next:
            if c2.next:
                c1.next = c2.next
                c1 = c1.next
        
            if c1.next:
                c2.next = c1.next
                c2 = c2.next
        if c2:
            c2.next = None
        if c1:
            c1.next = h2
        return h1
# Extra
class Solution:
    def oddEvenList(self, head):
        if not head:    return head
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next

            