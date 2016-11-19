#!/usr/bin/env python3

class BinaryTree(object):
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

def check_binary_search_tree(tree):
    pass

def is_binary_search_tree(tree):
    lst = traverse(tree)
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

def traverse(tree):
    if not tree:
        return []
    return traverse(tree.left) + [tree.key] + traverse(tree.right)

tree = BinaryTree(6)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(1)
tree.left.right = BinaryTree(4)
tree.left.right.left = BinaryTree(3)
tree.left.right.right = BinaryTree(5)
tree.right = BinaryTree(9)
tree.right.left = BinaryTree(7)
tree.right.left.right = BinaryTree(8)

assert is_binary_search_tree(tree)

tree.right.left.key = 4

assert not is_binary_search_tree(tree)
