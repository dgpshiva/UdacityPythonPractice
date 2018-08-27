class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def bst_search(self, node, value):
        if node != None:
            if node.value == value:
                return True
            elif value < node.value:
                node = node.left
                return self.bst_search(node, value)
            elif value > node.value:
                node = node.right
                return self.bst_search(node, value)
        else:
            return False

    def bst_insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                return
            else:
                node = node.left
                self.bst_insert(node, value)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
                return
            else:
                node = node.right
                self.bst_insert(node, value)

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        else:
            return traversal

        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
