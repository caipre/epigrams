#!/usr/bin/env python

# 5.1: Compute Parity
#   The bitwise parity of a value is 1 when the number of set bits is odd.
#   Otherwise, the parity is 0.

def parity(x):
    p = 0
    while x:
        p ^= 1
        x &= (x - 1)
    return p

assert parity(0b0000) == 0
assert parity(0b0001) == 1
assert parity(0b1011) == 1
assert parity(0b0110) == 0
