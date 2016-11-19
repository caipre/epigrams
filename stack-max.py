#!/usr/bin/env python3

# 9.1: Implement a stack with a max function

import random

class Stack(object):
    def __init__(self):
        self.items = None

    def push(self, item):
        if self.items:
            self.items.append(item)
        else:
            self.items = [item]

    def pop(self):
        if not self.items:
            return
        self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def empty(self):
        return not self.items

class MaxStack(object):
    def __init__(self):
        self._max = Stack()
        self.stack = Stack()

    def push(self, item):
        self.stack.push(item)

        max = self._max.peek()
        if self._max.empty():
            self._max.push((item, 1))
        else:
            max, count = self._max.peek()
            if item == max:
                self._max.pop()
                self._max.push((max, count + 1))
            elif item > max:
                self._max.push((item, 1))


    def pop(self):
        if self.stack.empty():
            return

        if not self._max.empty():
            item = self.stack.peek()
            max, count = self._max.peek()
            assert item <= max
            if item == max:
                self._max.pop()
                if count > 1:
                    self._max.push((max, count - 1))

        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def max(self):
        pair = self._max.peek()
        if pair:
            return pair[0]
        return None

ms = MaxStack()
for i in 1, 5, 5, 2, 2, 8, 8, 9, 23, 8, 4, 23, 32:
    ms.push(i)
    print(ms.stack.items)
    print(ms._max.items)
    print()

while not ms.stack.empty():
    ms.pop()
    print(ms.stack.items)
    print(ms._max.items)
    print()
