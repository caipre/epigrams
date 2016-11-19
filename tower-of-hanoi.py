#!/usr/bin/env python3

def hanoi(nrings):
    pegs = [[i for i in range(nrings)], [], []]
    calculate_hanoi_steps(nrings, pegs, 0, 1, 2)
    calculate_hanoi_steps(nrings, pegs, 1, 2, 0)

def calculate_hanoi_steps(nrings, pegs, from_peg, to_peg, use_peg):
    if nrings <= 0:
        return

    calculate_hanoi_steps(nrings - 1, pegs, from_peg, use_peg, to_peg)

    ring = pegs[from_peg].pop()
    pegs[to_peg].append(ring)
    print('move {} from {} to {}'.format(ring, from_peg, to_peg))

    calculate_hanoi_steps(nrings - 1, pegs, use_peg, to_peg, from_peg)

hanoi(5)
