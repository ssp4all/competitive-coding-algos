https://leetcode.com/problems/insertion-sort-list/

"""
Sort a linked list using insertion sort.
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:    return head
        
        head2 = pre = ListNode()
        cur = head
        
        while cur:
            next = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            
            cur.next = pre.next
            pre.next = cur
            pre = head2
            cur = next
        return head2.next


 class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        li = []
        
        work = head
        while work:
            li.append(work.val)
            work = work.next
            
        li.sort()
        
        work = head
        
        for i in range(len(li)):
            work.val = li[i]
            work = work.next
            
        return head