#!/usr/bin/env python3
from collections import defaultdict


def conway_cubes(points, validator, cycles=6):
    # prime the default dict with the next iterations values
    for point in list(points.keys()):
        tmp = [ points[p] for p in validator(*point) ]
        del tmp

    # run
    activate_stack, deactivate_stack = [], []
    for i in range(1, cycles+1):
        for point in list(points.keys()):
            count = sum( int(points[p]) for p in validator(*point) )
            
            if points[point] == ACTIVE and not (count == 2 or count == 3):
                deactivate_stack.append(point)
            elif points[point] == INACTIVE and count == 3:
                activate_stack.append(point)

        for _ in range(len(activate_stack)):
            points[activate_stack.pop()] = ACTIVE
        for _ in range(len(deactivate_stack)):
            points[deactivate_stack.pop()] = INACTIVE
    
    return sum(points.values())


if __name__ == '__main__':
    # static
    ACTIVE = True
    INACTIVE = False

    # given
    points = defaultdict(bool)
    with open('input.txt', 'r') as f:
        z, y = 0, 0
        while l := f.readline():
            for (x, val) in enumerate(l.strip()):
                points[(x, y, z)] = ACTIVE if val == '#' else INACTIVE
            y += 1

    # part 1
    validator = lambda x, y, z: ( (c_x, c_y, c_z) 
            for c_z in range(z-1, z+2) 
            for c_y in range(y-1, y+2) 
            for c_x in range(x-1, x+2) 
            if (c_x, c_y, c_z) != (x, y, z) )

    print(conway_cubes(points.copy(), validator))

    # part 2
    points = defaultdict(bool, { (x, y, z, 0):v for ((x, y, z), v) in points.items() })
    validator = lambda x, y, z, w: ( (c_x, c_y, c_z, c_w) 
            for c_z in range(z-1, z+2) 
            for c_y in range(y-1, y+2) 
            for c_x in range(x-1, x+2) 
            for c_w in range(w-1, w+2) 
            if (c_x, c_y, c_z, c_w) != (x, y, z, w) )

    print(conway_cubes(points.copy(), validator))


