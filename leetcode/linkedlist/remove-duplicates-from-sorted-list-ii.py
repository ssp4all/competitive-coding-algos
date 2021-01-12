https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:    return head 
        
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                head = head.next 
                pre.next = head
            else:
                pre = pre.next
                head = head.next

        return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:    return head 
        
        st = [[float('inf'), 1]] 
        cur = head 
        while cur:      
            val, f = st[-1]
            if st and cur.val != val:
                if f > 1:
                    st.pop()
                st += [[cur.val, 1]]
            else:
                st[-1][1] += 1
            cur = cur.next
        while st and st[-1][1] > 1:
            st.pop()
        print(st)
        
        dummy = cur = ListNode(-1)
        for val, _ in st[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
        
        