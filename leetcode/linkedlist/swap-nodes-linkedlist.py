# https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

"""
Given a linked list and two keys in it, swap nodes for two given keys. 
Nodes should be swapped by changing links. Swapping data of nodes may be 
expensive in many situations when data contains many fields. 
It may be assumed that all keys in the linked list are distinct.
Examples: 
Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Input:  10->15->12->13->20->14,  x = 10, y = 20
Output: 20->15->12->13->10->14

Input:  10->15->12->13->20->14,  x = 12, y = 13
Output: 10->15->13->12->20->14
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Main:
    def swap_nodes(head, x, y):
        if not head:    return 
        prevX, prevY = None, None
        
        i = head
        # find i and j
        while i and i.data != x:
            prevX = i
            i = cur.next

        j = head
        while j and j.data != y:
            prevY = j
            j = j.next

        # check for edge cases
        if not prevX:
            j = head
        else:
            prevX.next = j
            
        if not prevY:
            i = head
        else:
            prevY.next = i

        # swap the nodes
        temp = j.next
        j.next = i.next
        i.next = temp
        # done
    
