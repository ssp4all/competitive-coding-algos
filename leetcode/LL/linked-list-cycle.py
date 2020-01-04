https://leetcode.com/problems/linked-list-cycle

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return 0
        one, two = head, head.next
        while one and two:
            if one == two:
                return 1
            if one.next:
                one = one.next
            else: 
                return 0
            if two.next:
                two = two.next.next
            else: 
                return 0
        return 0

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return 0
        cur = head
        visited = set()
        while cur:
            if cur in visited:
                return 1
            else:
                visited.add(cur)
            cur = cur.next   
        return 0