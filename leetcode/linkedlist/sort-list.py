https://leetcode.com/problems/sort-list/

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:    return head
        
        def merge(l1, l2):
            if not l1 and not l2:   return l1
            if not l1 or not l2:  return l1 or l2
            
            head2 = temp = ListNode(0)
            
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            if l1 or l2:
                temp.next = l1 or l2
            return head2.next
            
            
        def sort_(cur):
            if not cur or not cur.next: return cur
            
            slow, fast = cur, cur
            pre = None
            
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            if pre:
                pre.next = None
            # print(cur.val)
            l1 = sort_(cur)
            l2 = sort_(slow)
            return merge(l1, l2)
        
        return sort_(head)