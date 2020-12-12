#!/usr/bin/env python3
from collections import defaultdict


if __name__ == '__main__':
    # given
    instructions = []
    with open('input.txt', 'r') as f:
        while l := f.readline():
            instruction = l.strip()
            instructions.append( (instruction[0], int(instruction[1:])) )

    get_dir = lambda n: { 0: 'E', 90: 'S', 180: 'W', 270: 'N' }[n % 360]

    # part 1
    facing = 0
    dists = defaultdict(int)
    for (action, value) in instructions:
        if action in ['N', 'S', 'E', 'W']:
            dists[action] += value
        elif action in ['L', 'R']:
            facing = facing + value if action == 'R' else facing - value
        else:
            dists[get_dir(facing)] += value

    print(abs(dists['E'] - dists['W']) + abs(dists['N'] - dists['S']))

    # part 2
    dists = defaultdict(int)
    wp = [ (0, 10), (90, 0), (180, 0), (270, 1) ]    # (E, 10), (N, 1)
    for (action, value) in instructions:
        if action in ['N', 'S', 'E', 'W']:
            wp = [ (f, d+value) if action == get_dir(f) else (f, d) for (f, d) in wp ]
        elif action in ['L', 'R']:
            wp = [ (f+value, d) if action == 'R' else (f-value, d) for (f, d) in wp ]
        else:
            for (facing, dist) in wp:
                dists[get_dir(facing)] += dist * value

    print(abs(dists['E'] - dists['W']) + abs(dists['N'] - dists['S']))
