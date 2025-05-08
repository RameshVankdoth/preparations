class bst:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst(data)

    def traverse(self):
        elements = []
        if self.left:
            elements += self.left.traverse()

        elements.append(self.data)

        if self.right:
            elements += self.right.traverse()

        return elements


tree = bst(5)
tree.add_child(1)
tree.add_child(9)
tree.add_child(7)
tree.add_child(2)
tree.add_child(3)

print(tree.traverse())

# Update
