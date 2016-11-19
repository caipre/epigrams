#!/usr/bin/env python3

def find_array_intersection(A, B):
    ai = 0
    bi = 0
    ret = []
    while ai < len(A) and bi < len(B):
        if A[ai] < B[bi]:
            ai += 1
        elif A[ai] > B[bi]:
            bi += 1
        else:
            ret.append(A[ai])
            v = A[ai]
            while ai < len(A) and A[ai] == v: ai += 1
            while bi < len(B) and B[bi] == v: bi += 1
    return ret


A = [1, 2, 3, 4, 4, 5, 7, 8, 10]
B = [3, 4, 8, 9, 9, 10, 13]
print(find_array_intersection(A, B))
