#!/usr/bin/env python3

from heapq import heappush, heappop

def merge_lists(stockprices):
    heap = []
    idxs = {}
    for i in range(len(stockprices)):
        tup = stockprices[i][0]
        idxs[tup[1]] = (i, 0)
        heappush(heap, tup)

    while heap:
        tup = heappop(heap)
        print(tup)

        idx, off = idxs[tup[1]]
        off += 1
        if off < len(stockprices[idx]):
            tup = stockprices[idx][off]
            idxs[tup[1]] = (idx, off)
            heappush(heap, tup)


merge_lists([
    [ (1230, 'HNDA',  8) ],
    [ (1233, 'AAPL',  9), (1234, 'AAPL', 10) ],
    [ (1234, 'MSFT', 12), (1235, 'MSFT', 12) ],
    [ (1233, 'QBRT', 10), (1235, 'QBRT', 12), (1236, 'QBRT', 12) ],
])
