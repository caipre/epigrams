#!/usr/bin/env python3

class NullTree(object):
    def __init__(self):
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.left = NullTree()
        self.right = NullTree()

def is_balanced(tree):
    return check_balanced(tree)[0]

def check_balanced(tree):
    if not tree:
        return True, -1

    lbalanced, lheight = check_balanced(tree.left)
    if not lbalanced: return False, -1
    rbalanced, rheight = check_balanced(tree.right)
    if not rbalanced: return False, -1

    return abs(lheight - rheight) <= 1, max(lheight, rheight) + 1

t = BinaryTree()
t.left = BinaryTree()
t.right = BinaryTree()
t.left.left = BinaryTree()
#t.left.left.left = BinaryTree()
#t.left.left.left.left = BinaryTree()
assert is_balanced(t)
