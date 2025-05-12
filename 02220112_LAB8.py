class Node:
    def __init__(self, data, color='red', left=None, right=None, parent=None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(data=value, left=self.NIL, right=self.NIL, parent=None)
        self._bst_insert(new_node)
        self._fix_insert(new_node)

    def _bst_insert(self, z):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = 'red'

    def _fix_insert(self, z):
        while z.parent and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._left_rotate(z.parent.parent)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, value):
        node = self.root
        while node != self.NIL:
            if node.data == value:
                break
            elif value < node.data:
                node = node.left
            else:
                node = node.right

        if node == self.NIL:  
            print(f"Value {value} not found in the tree.")
            return

        self._delete_node(node)

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:  # Case 1: No left child, transplant with right child
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:  # Case 2: No right child, transplant with left child
            x = z.left
            self._transplant(z, z.left)
        else:  # Case 3: Node has two children, replace with in-order successor
            y = self._tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color  # Copy the color of z

        if y_original_color == 'black':  # If the original node was black, fix the tree
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _tree_minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:  # Case: x is a left child
                w = x.parent.right
                if w.color == 'red':  
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root 
            else: 
                w = x.parent.left
                if w.color == 'red':  
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root  
        x.color = 'black'  

    def search(self, value):
        return self._search_tree_helper(self.root, value)

    def _search_tree_helper(self, node, key):
        if node == self.NIL or key == node.data:
            return node != self.NIL
        if key < node.data:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def get_black_height(self):
        return self._get_black_height(self.root)

    def _get_black_height(self, node):
        height = 0
        while node != self.NIL:
            if node.color == 'black':
                height += 1
            node = node.left
        return height

rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.insert(50)
rb_tree.delete(10)
print(rb_tree.get_black_height())

def print_tree(node, indent="", last=True, NIL=None):
    if node != NIL:
        print(indent, end='')
        if last:
            print("R----", end='')
            indent += "     "
        else:
            print("L----", end='')
            indent += "|    "
        s_color = "RED" if node.color == 'red' else "BLACK"
        print(f"{node.data}({s_color})")
        print_tree(node.left, indent, False, NIL)
        print_tree(node.right, indent, True, NIL)

print_tree(rb_tree.root, NIL=rb_tree.NIL)
