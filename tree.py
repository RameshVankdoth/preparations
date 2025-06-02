class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def traverse(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for i in self.children:
                i.traverse()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


root = TreeNode("Electronics")
laptop = TreeNode("Laptop")
tv = TreeNode("tv")
mobile = TreeNode("mobile")
root.add_child(laptop)
root.add_child(tv)
root.add_child(mobile)
asus = TreeNode("ASUS")
laptop.add_child(asus)

root.traverse()
root.remove_child(tv)
root.traverse()
