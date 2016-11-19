#!/usr/bin/env python3

import random

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = ListNode(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node

    def status(self):
        print(self.head.data, '->', self.tail.data, self.data())

    def data(self):
        ds = []
        node = self.head
        while node:
            ds.append(node.data)
            node = node.next
        return ds

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(a, b):
    ll = a if a.head.data <= b.head.data else b

    aptr = a.head
    bptr = b.head
    ptr = ll.head

    while aptr and bptr:
        if aptr.data <= bptr.data:
            ptr.next, aptr = aptr, aptr.next
        else:
            ptr.next, bptr = bptr, bptr.next
        ptr = ptr.next

    if aptr: ptr.next = aptr
    if bptr: ptr.next = bptr

    while ptr.next:
        ptr = ptr.next

    ll.tail = ptr

    return ll

list_a = LinkedList()
list_a.append(2)
list_a.append(5)
list_a.append(7)
list_a.status()

list_b = LinkedList()
list_b.append(3)
list_b.append(11)
list_b.status()

list_m = merge_lists(list_a, list_b)
list_m.status()
