#!/usr/bin/env python3

def two_sum(lst, target):
    i = 0
    j = len(lst) - 1
    while i < j:
        s = lst[i] + lst[j]
        if s == target:
            return True
        elif s < target:
            i += 1
        else:
            j -= 1
    return False

def three_sum(lst, target):
    for i, d in enumerate(lst):
        if two_sum(lst[0:i] + lst[i+1:], target - d):
            return True
    return False

assert three_sum([1, 2, 3], 6)
assert not three_sum([1, 2, 3], 7)
