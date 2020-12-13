#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    # given
    with open('input.txt', 'r') as f:
        depart_t = int(f.readline().strip())
        b_ids = [ int(b_id) 
                if b_id != 'x' else 0
                for b_id in f.readline().strip().split(',') ]

    # part 1
    b_id, t = None, depart_t
    while not b_id and (t := t + 1):
        b_id = next(( b_id for b_id in b_ids if b_id and not t % b_id ), None)

    print(( t - depart_t ) * b_id)

    # part 2
    offset_ids = [ (i, b_ids[i]) for i in range(len(b_ids)) if b_ids[i] != 0 ]
    t, jmp, match_i = 1, 1, 0
    while not all((t+offset) % val == 0 for (offset, val) in offset_ids) and (t := t+jmp):
        if all( (t+offset) % val == 0 for (offset, val) in offset_ids[:match_i+1] ):
            jmp *= offset_ids[match_i][1]
            match_i += 1

    print(t)


