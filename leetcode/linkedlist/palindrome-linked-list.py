https://leetcode.com/problems/palindrome-linked-list/

"""
Given the head of a singly linked list,
return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true
"""


#idea is to 
# first find middle then reverse the second half
# then check for same values
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        def reverse(head):
            prev = None 
            cur = head 
            while cur:
                next = cur.next 
                cur.next = prev 
                prev = cur
                cur = next
            return prev 
        
        slow, fast = head, head 
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next 
        
        slow = reverse(slow)
        cur = head
        while slow and cur:
            if cur.val != slow.val:
                return 0 
            slow, cur = slow.next, cur.next
        
        return 1