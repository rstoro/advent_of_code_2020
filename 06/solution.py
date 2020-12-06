#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    # given
    groups = [[]]
    with open('input.txt', 'r') as f:
        while l := f.readline():
            person = l.strip()
            if person:
                groups[-1].append(person)
            else:
                groups.append([])

    # part 1
    print(sum( len(set(''.join(group))) for group in groups ))

    # part 2
    # n is closest chr to ∩
    n = lambda g: reduce(lambda p1, p2: [ c for c in p1 if c in p2 ], g[0:], g[0])
    print(sum( len(n(group)) for group in groups ))
