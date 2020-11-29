class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, key):
        self.root = Node(key)   
    
    def insert(root, node):
        if not root:
            return node
        elif root.val > node.val:
            root.left = insert(root.left, node)
        else:
            root.right = insert(root.right, node)
        return root
    
    def find_min(root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur
    
    def delete(root, key):
        if not root:    return root
        if root.key > key:
            root.left = delete(root.left, key)
        elif root.key < key:
            root.right = delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            else:
                temp = find_min(root.right)
                root.key = temp.key
                root.right = delete(root.right, temp.key)

        return root


    def search(root, node):
        if root.val == node.val:
            return root
        elif root.val > node.val:
            return search(root.left, node)
        else:
           return search(root.right, node)
        return None

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        print(root.val)
        inorder(root.right)
