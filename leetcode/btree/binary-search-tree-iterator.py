https://leetcode.com/problems/binary-search-tree-iterator/

"""
Implement the BSTIterator class that represents an iterator over the 
in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
The root of the BST is given as part of the constructor. The pointer should be initialized to a
 non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, 
otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, 
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there 
will be at least a next number in the in-order traversal when next() is called.
"""
# O(N)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.op = []
        self.push(root)
        
    def push(self, root):
        if not root:    return 
        while root:
            self.op.append(root)
            root = root.left
        
    
    def next(self) -> int:
        if not self.op: return 0
        x = self.op.pop()
        self.push(x.right)
        return x.val

    def hasNext(self) -> bool:
        return self.op

# Editorial O)(1)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)
        
    def pushAll(self, node):
        while node:
            self.stack += [node]
            node = node.left 
        
    def next(self) -> int:
        # if not self.hasNext():  return 
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val

    def hasNext(self) -> bool:
        return 1 if self.stack else 0