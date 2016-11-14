#!/usr/bin/env python3

import logging
import random

# logging.basicConfig(level=logging.DEBUG)

# 6.1: Dutch National Flag Partitioning
#   The (naive) quicksort algorithm is suboptimal for lists with many
#   repeated elements. To address this shortcoming, Dutch National Flag
#   partitioning groups together values which compare equal to the pivot.

def partition(array, i):
    def swap(a, b):
        array[a], array[b] = array[b], array[a]

    pivot = array[i]
    logging.debug('pivot {}'.format(pivot))

    idx = 0
    smaller = 0
    larger = len(array) - 1

    while idx <= larger:
        logging.debug(array)
        logging.debug(' ' + ' ' * (3*(smaller)) + 's'
                          + ' ' * (3*(idx-smaller)-1) + 'i'
                          + ' ' * (3*(larger-idx)-2) + 'l' + '\n')

        if array[idx] < pivot:
            swap(idx, smaller)
            smaller += 1
            idx += 1
        elif array[idx] == pivot:
            idx += 1
        else:
            swap(idx, larger)
            larger -= 1

    logging.debug(array)

if __name__ == '__main__':
    array = []
    for _ in range(10):
        array.append(random.randint(0, 4))

    partition(array, random.randint(0, len(array) - 1))
