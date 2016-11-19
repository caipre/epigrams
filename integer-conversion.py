#!/usr/bin/env python3

# 7.1 Interconvert Strings and Integers
#   Implement the atoi and itoa functions.

def atoi(s):
    sum = 0
    for c in s:
        ordc = ord(c)
        if 0x30 <= ordc <= 0x39:
            n = ordc - 0x30
            sum = (sum * 10) + n

    if sum > 0 and s[0] == '-':
        sum *= -1

    return sum

def itoa(i):
    if i == 0: return '0'
    rstr = ''
    neg = i < 0
    i = abs(i)
    while i > 10:
        rstr += chr((i % 10) + 0x30)
        i //= 10
    rstr += chr(i + 0x30)
    if neg:
        rstr += '-'
    return rstr[::-1]

assert atoi('0') == 0
assert atoi('1') == 1
assert atoi('-1') == -1
assert atoi('-0') == 0
assert atoi('123') == 123
assert atoi('-123') == -123
assert atoi('1,234') == 1234
assert atoi('1.234') == 1234


assert itoa(0) == '0'
assert itoa(1) == '1'
assert itoa(-1) == '-1'
assert itoa(-0) == '0'
assert itoa(123) == '123'
assert itoa(-123) == '-123'
assert itoa(1234) == '1234'
