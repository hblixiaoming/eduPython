class Node:
    def __init__(self, l_child, r_child, data):
        self.l_child = l_child
        self.r_child = r_child
        self.data = data

    def __repr__(self):
        return self.data


def init_tree():
    d = Node(None, None, 'd')
    e = Node(None, None, 'e')
    f = Node(None, None, 'f')
    g = Node(None, None, 'g')
    b = Node(d, e, 'b')
    c = Node(f, g, 'c')
    a = Node(b, c, 'a')
    return a


def pre_traverse(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_traverse(node.l_child)
    pre_traverse(node.r_child)


def pre_traverse_loop(node):
    if node is None:
        return
    stack = []
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        print(n.data, end=' ')
        if n.r_child is not None:
            stack.append(n.r_child)
        if n.l_child is not None:
            stack.append(n.l_child)


def in_traverse(node):
    if node is None:
        return
    in_traverse(node.l_child)
    print(node.data, end=' ')
    in_traverse(node.r_child)


def in_traverse_loop(node):
    if node is None:
        return
    stack = []
    stack.append(node)




def post_traverse(node):
    if node is None:
        return
    post_traverse(node.l_child)
    post_traverse(node.r_child)
    print(node.data, end=' ')


def level_traverse(node):
    if node is None:
        return
    queue = []
    queue.insert(0, node)
    while len(queue) != 0:
        n = queue.pop()
        print(n, end=' ')
        if n.l_child is not None:
            queue.insert(0, n.l_child)
        if n.r_child is not None:
            queue.insert(0, n.r_child)
            pass
        pass


if __name__ == '__main__':
    root = init_tree()
    print('-----pre_traverse----- ')
    pre_traverse(root)
    print()
    print('-----pre_traverse_loop----- ')
    pre_traverse_loop(root)
    print()
    print('-----in_traverse----- ')
    in_traverse(root)
    print()
    print('-----post_traverse----- ')
    post_traverse(root)
    print()
    print('-----level_traverse----- ')
    level_traverse(root)
