https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        
        cur = head
        #insert new nodes
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        
        cur = head
        while cur:
            # print(cur.val)
            if cur.random == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next
            cur = cur.next.next
    
        cur = head
        head2 = temp = cur.next
        while cur.next and temp.next:
            cur.next = cur.next.next
            temp.next = temp.next.next
            cur = cur.next
            temp = temp.next
        
        return head2
            