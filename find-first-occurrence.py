#!/usr/bin/env python3

def find_first_occurrence(lst, key):
    lft = 0
    rht = len(lst) - 1
    while lft <= rht:
        idx = lft + ((rht - lft) // 2)
        print(lft, idx, lst[idx], rht)
        if lst[idx] == key:
            ret = idx
            rht = idx - 1
        elif lst[idx] < key:
            lft = idx + 1
        else:
            rht = idx - 1
    print(ret)
    return ret


lst = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
assert find_first_occurrence(lst, 108)
assert find_first_occurrence(lst, 285)

