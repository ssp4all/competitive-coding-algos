class node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def non_leaf_nodes(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 0
	return 1 + non_leaf_nodes(node.left) + non_leaf_nodes(node.right)

def calc_height(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 1
	lh = calc_height(node.left)
	rh = calc_height(node.right)
	 
	if lh > rh:
		return 1 + lh
	else: 
		return 1 + rh

def preorder(node):
	if node == None:
		return
	preorder(node.left)
	print(node.data)
	preorder(node.right)

def reverse_tree(root):
	if root == None:
		return

	temp = node(0)
	temp = root.left
	root.left = root.right
	root.right = temp

	reverse_tree(root.left)
	reverse_tree(root.right)



	

if __name__ == '__main__':
	root = node(1)
	root.left = node(2)
	root.right = node(3)
	root.left.left = node(4)
	root.right.right = node(5)

	reverse_tree(root)

	# x = calc_height(root)
	# print(x)
	