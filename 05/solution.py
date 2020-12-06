#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    # given
    with open('input.txt', 'r') as f:
        boarding_passes = ( l.strip() for l in f.readlines() )

    # alg
    binary_map = [ ('B', '1'), ('F','0'), ('R', '1'), ('L', '0') ]
    repl = lambda bp, bm: reduce(lambda s, kv: s.replace(*kv), bm, bp)
    calc = lambda bin1, bin2: (int(bin1, 2) * 8) + int(bin2, 2)
    get_seat_id = lambda bp: calc(repl(bp[:7], binary_map), repl(bp[7:], binary_map))

    # calc
    seat_ids = set(get_seat_id(boarding_pass) for boarding_pass in boarding_passes)

    # part 1
    print(max(seat_ids))

    # part 2
    print([ i for i in range(min(seat_ids), max(seat_ids)) if i not in seat_ids ][0])




