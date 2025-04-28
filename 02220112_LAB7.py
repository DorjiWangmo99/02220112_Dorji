class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print("Created new Binary Tree")
        print(f"Root: {self.root}")

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def height_start(self):
        return self.height(self.root)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def size_start(self):
        return self.size(self.root)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def count_leaves_start(self):
        return self.count_leaves(self.root)

    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if (node.left is None and node.right is None):
            return True
        if (node.left is not None) and (node.right is not None):
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_full_binary_tree_start(self):
        return self.is_full_binary_tree(self.root)

    def is_complete_binary_tree(self, node, index, node_count):
        if node is None:
            return True
        if index >= node_count:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, node_count) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, node_count))

    def is_complete_binary_tree_start(self):
        node_count = self.size_start()
        return self.is_complete_binary_tree(self.root, 0, node_count)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    tree = BinaryTree(node1)
    print(f"Tree Height: {tree.height_start()}")
    print(f"Total Nodes: {tree.size_start()}")
    print(f"Leaf Nodes Count: {tree.count_leaves_start()}")
    print(f"Is Full Binary Tree: {tree.is_full_binary_tree_start()}")
    print(f"Is Complete Binary Tree: {tree.is_complete_binary_tree_start()}")
