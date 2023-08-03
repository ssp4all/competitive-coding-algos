class IntervalTree:
    class Node:
        def __init__(self, interval):
            self.interval = interval
            self.left = None
            self.right = None
            self.max_end = interval[1]

    def __init__(self):
        self.root = None

    def insert(self, interval):
        def recursive_insert(node, interval):
            if node is None:
                return self.Node(interval)
            if interval[0] < node.interval[0]:
                node.left = recursive_insert(node.left, interval)
            else:
                node.right = recursive_insert(node.right, interval)
            node.max_end = max(node.max_end, interval[1])
            return node

        self.root = recursive_insert(self.root, interval)

    def is_present(self, point):
        def recursive_search(node, point):
            if node is None:
                return False
            if node.interval[0] <= point <= node.interval[1]:
                return True
            if node.left is not None and node.left.max_end >= point:
                return recursive_search(node.left, point)
            return recursive_search(node.right, point)

        return recursive_search(self.root, point) 

tree = IntervalTree()
tree.insert((-100, 500))
tree.insert((8, 9))
print(tree.is_present(4))  # True
print(tree.is_present(8))  # True
print(tree.is_present(-99))  # False