#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    #given
    with open('input.txt', 'r') as f:
        hill = [ l.strip() for l in f.readlines() ]

    #alg
    collisions = lambda h,x,y: ( int(h[i][((i // y) * x) % len(h[i])] == '#') \
            for i in range(y, len(h), y) )

    #part 1
    print(sum(collisions(hill, 3, 1,)))

    #part 2
    mult = lambda a, b: a * b
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(reduce(mult, ( sum(collisions(hill, slope[0], slope[1])) for slope in slopes )))


