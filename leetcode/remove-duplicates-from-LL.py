# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        first = head
        second = head.next if head else None
        while second != None:
            if first.val == second.val:
                first.next = second.next
                second = second.next
            else:
                first = second
                second = second.next
                
                
        return head