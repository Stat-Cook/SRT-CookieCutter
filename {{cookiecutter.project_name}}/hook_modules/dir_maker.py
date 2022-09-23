import os

class DirMaker:

    def __init__(self, parent, prefix):
        self.parent = parent
        self.prefix = prefix
        self.children = []

    def __repr__(self):
        return f"DirMaker(Target={self.parent}/{self.prefix}...)"

    @property
    def n_children(self):
        return len(self.children)

    def make_child(self, value):
        new_prefix = f"{self.prefix}.{self.n_children + 1}"
        target = f"{self.parent}/{new_prefix} {value}"

        os.makedirs(target)

        child = DirMaker(target, new_prefix)
        self.children.append(child)

        return child

    def make_children(self, values):
        return [self.make_child(i) for i in values]
