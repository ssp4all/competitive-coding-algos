# https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1 or not l2: return l1 or l2
        
        cur1 = l1
        cur2 = l2
        carry = 0
        head = ListNode(0)
        temp = head
        while cur1 and cur2:
            addi = cur1.val + cur2.val + carry
            carry = 0
            if addi >= 10:
                carry = 1
                addi %= 10
            temp.next = ListNode(addi)
            temp = temp.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        temp.next = cur1 or cur2
        while carry != 0:
            if temp.next is None and carry != 0:
                temp.next = ListNode(carry)
                carry = 0
            elif temp.next is not None and carry != 0:
                temp = temp.next
                addi = temp.val + carry
                carry = 0
                if addi >= 10:
                    carry = 1
                    addi %= 10
                temp.val = addi
        return head.next 
            
            
"""Optimized """
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1 or not l2: return l1 or l2
        
        cur1 = l1
        cur2 = l2
        carry = 0
        temp = head = ListNode(0)

        while cur1 and cur2 or carry:
            v1 = (cur1.val if cur1 else 0)
            v2 = (cur2.val if cur2 else 0)
            carry, addi = divmod(v1 + v2 + carry, 10)            
            temp.next = ListNode(addi)
            temp = temp.next
            cur1 = (cur1.next if cur1 else None)
            cur2 = (cur2.next if cur2 else None)
        return head.next
            
            