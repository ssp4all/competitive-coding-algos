https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head
        map = {}
        cur = head
        i = 0
        while cur:
            if cur in map:
                return cur
            map[cur] = i
            cur = cur.next
            i += 1
        return None          
"""
Without extra space
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        one, two = head, head.next
        while one != two:
            try:
                one = one.next
                two = two.next.next
            except:
                return None
        one = one.next
        two = head
        while one != two:
            one = one.next
            two = two.next
        return one