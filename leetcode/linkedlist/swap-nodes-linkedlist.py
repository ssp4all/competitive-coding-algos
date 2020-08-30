# https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

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
    
