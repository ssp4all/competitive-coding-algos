class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
		def leftBoundary(root):
			if root:
				if root.left:
					print(root.val)
					leftBoundary(root.left)
				elif root.right:
					print(root.val)
					leftBoundary(root.right)

		def leaves(root):
			if root:
				leaves(root.left)
				if root.left is None and root.right is None:
					print(root.val)
				leaves(root.right)
			
		def rightBoundary(root):
			if root:
				if root.right:
					rightBoundary(root.right)
					print(root.val)
				elif root.left:
					rightBoundary(root.left)
					print(root.val)
			
		if not root: return root
		print(root.val)
		leftBoundary(root.left)
		leaves(root.left)
		leaves(root.right)
		rightBoundary(root.right)