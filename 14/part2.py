#!/usr/bin/env python3
from re import findall as re_findall
from re import compile as re_compile
from collections import defaultdict

if __name__ == '__main__':
    # helpers
    modify_bit = lambda b_i, b, n: (n & ~(1 << b_i)) | ((b << b_i) & (1 << b_i))
    re_nums = re_compile(r'[0-9]+')

    # given
    mem = defaultdict(list)
    with open('input.txt', 'r') as f:
        while l := f.readline().strip():
            if l[:4] == 'mask':
                mask = [ int(n) if n != 'X' else -1 for n in l.split(' = ')[1][::-1] ]
                overwrites = [ (i, mask[i]) for i in range(len(mask)) if mask[i] == 1 ]
                floatings = [ i for i in range(len(mask)) if mask[i] == -1 ]
            else:
                mem_loc, mem_val = tuple(map(int, re_findall(re_nums, l)))
                for (bit_i, bit_val) in overwrites:
                    mem_loc = modify_bit(bit_i, bit_val, mem_loc)

                mem_locs = []
                for bit_i in floatings:
                    mem_loc = modify_bit(bit_i, 0, mem_loc)

                mem_locs.append(mem_loc)

                for bit_i in floatings:
                    for i in range(len(mem_locs)):
                        mem_locs.append(modify_bit(bit_i, 1, mem_locs[i]))
                    mem_locs.append(modify_bit(bit_i, 1, mem_loc))

                for loc in mem_locs:
                    mem[loc] = mem_val

    print(sum(mem.values()))



