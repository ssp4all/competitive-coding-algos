https://leetcode.com/problems/add-two-numbers-ii/

"""
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        
        while l1:
            stack1 += [l1.val]
            l1 = l1.next
        
        while l2:
            stack2 += [l2.val]
            l2 = l2.next

        cur = ListNode(0)
        sum = 0
        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            sum += v1 + v2
            cur.val = sum % 10
            head = ListNode(sum // 10)
            head.next = cur
            cur = head
            sum //= 10
        return cur.next if cur.val == 0 else cur


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverse(node):
            if not node or not node.next:   return node
            cur = node
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        head1 = reverse(l1)
        head2 = reverse(l2)
        carry = 0
        Dummy = cur = ListNode(-999)
        while head1 or head2 or carry:
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0
            carry, v = divmod(v1 + v2 + carry, 10)
            cur.next = ListNode(v)
            cur = cur.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        
        return reverse(Dummy.next)

