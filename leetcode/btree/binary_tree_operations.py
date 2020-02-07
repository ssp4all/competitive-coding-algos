class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def non_leaf_nodes(node):
	"""Count non-leaf nodes"""
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 0
	return 1 + non_leaf_nodes(node.left) + non_leaf_nodes(node.right)

def count_leaf_nodes(node):
	"""Count leaf nodes """
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 1
	return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

def print_ancestor(node, key):
 	"""Ancestors of a given node """
	if node is None:
		return False
	if node.data == key:
		return True
	if print_ancestor(node.left, key) or print_ancestor(node.right, key):
		print(node.data)
		return True
	return False

def diameter(node):
	if node == None:
		return 0
	lh = calc_height(node.left)
	rh = calc_height(node.right)

	ld = diameter(node.left)
	rd = diameter(node.right)

	return max(lh+rh+1, max(ld, rd))

	"""Optimized"""
	class Solution:
	    def diameterOfBinaryTree(self, root: TreeNode) -> int:
	        if not root: return 0
	        self.ans = 0
	        def calc(root):
	            if not root: return 0
	            lh = calc(root.left)
	            rh = calc(root.right)
	            self.ans = max(self.ans, lh+rh+1)
	            return max(lh, rh) + 1
	        calc(root)
	        return self.ans - 1

def calc_height(node):
	if node == None:
		return 0
	return 1 + max(calc_height(node.left), calc_height(node.right))
	# if node.left == None and node.right == None:
	# 	return 1
	# lh = calc_height(node.left)
	# rh = calc_height(node.right)
	 
	# if lh > rh:
	# 	return 1 + lh
	# else: 
	# 	return 1 + rh




class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return []
        op = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            op.append(cur.val)
            cur = cur.right
        return op

	    def inorder(node):
			if node == None:
				return
			inorder(node.left)
			print(node.data)
			inorder(node.right)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return root
        s, op = [root], []
        while s:
            root = s.pop()
            op.append(root.val)
            if root.left:
                s.append(root.left)
            if root.right:
                s.append(root.right)
        return op[::-1]
        
        def postorderTraversal(root):
            if not root:    return
            postorderTraversal(root.left)
            postorderTraversal(root.right)
            op.append(root.val)
        postorderTraversal(root)
        return op
       
class Solution:
	def preorder(node):
		if not node:
			return
		print(node.data)
		preorder(node.left)
		preorder(node.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:    return
        op, stack = [], [root]
        cur = root
        while cur or stack:
            cur = stack.pop()
            if not cur: continue
            op.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return op

def LCA(node, n1, n2):
	""" Lowest common ancestor of a given two nodes"""
	if node is None:
		return None

	if node.data == n1 or
		node.data == n2:
		return node.data

	left = LCA(node.left, n1, n2)
	right = LCA(node.right, n1, n2)

	if left and right:
		return node.data

	return left if left is not None else right

def LCA_for_BST(node, n1, n2):
	""" Lowest common ancestor of a given two nodes"""
	if node is None:
		return None
	if node.data > n1 and node.data > n2:
		return LCA_for_BST(node.left, n1, n2)
	elif node.data < n1 and node.data < n2:
		return LCA_for_BST(node.right, n1, n2)

	return node

	"""Iterative"""
	while root:
		if p.val < root.val and q.val < root.val:
			root = root.left
		elif p.val > root.val and q.val > root.val:
			root = root.right
		else:
			return root
	

def reverse_tree(node):
	"""Reverse a binary tree """
	if node == None:
    	return None
               
    le = reverse_tree(node.left)
    ri = reverse_tree(node.right)
    # print(le, ri)
    node.left = ri
    node.right = le
    
    return node

if __name__ == '__main__':
	root = node(1)
	root.left = node(2)
	root.right = node(3)
	root.left.left = node(4)
	root.right.right = node(5)

	reverse_tree(root)