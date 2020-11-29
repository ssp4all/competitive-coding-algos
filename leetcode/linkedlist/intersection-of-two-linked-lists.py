https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # if headA or headB in [None]: return None
        
        dict = {}
        cur = headA
        while cur:
            if cur.val not in dict:
                dict[cur] = cur.val
            cur = cur.next
        # print(dict)
        cur = headB
        while cur:
            if cur in dict:
                # if cur.val == interesectVal:
                return cur
            cur = cur.next
        return None

"""Two pointer approach"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        
        cur = headA
        n1, n2 = 1, 1
        while cur.next:
            cur = cur.next
            n1 += 1
            
        cur2 = headB
        while cur2.next:
            cur2 = cur2.next
            n2 += 1
            
        # print(n1, n2)
        if cur.val != cur2.val:
            return None
            
        skip = abs(n1-n2)
        if n1>n2:
            cur1, cur2 = headA, headB
        else:
            cur2, cur1 = headA, headB
        
        while skip != 0:
            cur1 = cur1.next
            skip -= 1
        while cur1 != cur2:
            cur1, cur2 = cur1.next, cur2.next
        return cur1