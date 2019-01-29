class TreeNode:
    __slots__ = {'key', 'parent', 'left', 'right', 'color'}

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'
        pass

    pass


class RBTree:
    def __init__(self):
        self.nil = TreeNode(0)
        self.root = self.nil
        pass

    def parent(self, node):
        return node.parent

    def grandParent(self, node):
        return node.parent.parent

    def uncle(self, node):
        if node.parent == self.grandParent(node).left:
            return self.grandParent(node).right
        else:
            return self.grandParent(node).left
        pass

    pass
