class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    # ფოთლის კვანძების დაბეჭდვის ფუნქცია
    def printLeafNodes(self):
        print("Leaf nodes are:")
        self._printLeafNodes(self.root)

    def _printLeafNodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.key)

        self._printLeafNodes(node.left)
        self._printLeafNodes(node.right)

    # კიდეების რაოდენობის დათვლის ფუნქცია
    def countEdges(self):
        return self._countEdges(self.root)

    def _countEdges(self, node):
        if node is None:
            return 0

        left_edges = self._countEdges(node.left)
        right_edges = self._countEdges(node.right)

        return left_edges + right_edges + (1 if node.left or node.right else 0)


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(14)
tree.insert(16)
tree.insert(9)
tree.insert(4)

tree.printLeafNodes()
print("Number of edges in the tree:", tree.countEdges())
