# Tree tranversal in constant space and with parent pointer 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            temp = insert(root.left, data)
            root.left = temp
            temp.parent = root
        else:
            temp = insert(root.right, data)
            root.right = temp
            temp.parent = root
        return root

root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 6)
root = insert(root, 8)


node = root 
left_done = 0
while node:
    if not left_done:
        while node.left:
            node = node.left  
    left_done = 1
    print(node.data, end='\t')
    if node.right:
        node = node.right 
        left_done = 0
    elif node.parent: # both child done, go back
        while node.parent and node.parent.right == node:
            node = node.parent 
        node = node.parent
    else:
        break 