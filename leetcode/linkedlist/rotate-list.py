
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        cur = head
        n = 1

        while cur.next:
            cur = cur.next
            n += 1
        k %= n
        
        cur.next = head
        for _ in range(n-k):
            cur = cur.next
        
        head2 = cur.next
        cur.next = None
        return head2