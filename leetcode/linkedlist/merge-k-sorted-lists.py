https://leetcode.com/problems/merge-k-sorted-lists

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        ip = []
        for i in lists:
            while i:
                ip.append(i)
                i = i.next
        ip.sort(key = lambda x:x.val)
        n = len(ip)
        for i in range(n-1):
            ip[i].next = ip[i+1]
        if n>0: ip[-1].next = None
        return ip[0] if n > 0 else None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        ip = []
        for i in lists:
            while i:
                ip.append(i.val)
                i = i.next
        print(ip)
        cur = head = ListNode(0)
        
        for i in sorted(ip):
            cur.next = ListNode(i)
            cur = cur.next
        return head.next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        heap = []
        for l in lists:
            if l:
                heappush(heap, (l.val, id(l), l))
        head = cur = ListNode(0)
        
        while heap:
            val, ind, node = heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heappush(heap, (node.val, id(node), node))
        return head.next