# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        if head is None:
            return
        temp = head
        while temp != None and temp.next != None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else: temp = temp.next
        return head