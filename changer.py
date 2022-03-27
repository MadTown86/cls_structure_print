class Tree:
    origin = "flower"

    def addleaves(self, leaf):
        self.leaf = leaf


class Leaf(Tree):
    def __init__(self, name):
        self.name = name

    def addleaves(self, leaf, flower):
        Tree.addleaves(self, leaf + flower)


X = Leaf("bbq")

print(X.origin)
X.addleaves("Charlie ", "Brown")
print(X.leaf)