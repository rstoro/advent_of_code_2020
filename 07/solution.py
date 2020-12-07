#!/usr/bin/env python3
from operator import methodcaller


if __name__ == '__main__':
    # given
    bag_map = {}
    with open('input.txt', 'r') as f:
        while l := f.readline():
            bag_type, bag_contains = l.strip().rstrip('.').split(' contain ')
            bag_map[bag_type.rstrip('s')] = { c[1].rstrip('s'): int(c[0])
                    for c in map(methodcaller('split', ' ', 1), bag_contains.split(', '))
                    if c[0] != 'no' }

    # part 1
    walk = lambda l, b, s: any( True if lb == s else walk(l, lb, s) for lb in l[b] )
    print(sum( walk(bag_map, key, 'shiny gold bag') for key in bag_map ))

    # part 2
    # thank you Mike Day for the simplified sum :)
    # count = lambda l, b: sum(l[b][lb] + ( l[b][lb] * count(l, lb) ) for lb in l[b])
    count = lambda l, b: sum(l[b][lb] * ( 1 + count(l, lb) ) for lb in l[b])
    print(count(bag_map, 'shiny gold bag'))

