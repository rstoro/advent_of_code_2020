#!/usr/bin/env python3
from re import findall as re_findall
from re import compile as re_compile
from collections import defaultdict

if __name__ == '__main__':
    # helpers
    modify_bit = lambda b_i, b, n: (n & ~(1 << b_i)) | ((b << b_i) & (1 << b_i))
    re_nums = re_compile(r'[0-9]+')

    # given
    mem = defaultdict(int)
    with open('input.txt', 'r') as f:
        while l := f.readline().strip():
            if l[:4] == 'mask':
                mask = l.split(' = ')[1][::-1]
                overwrites = [ (i, int(mask[i])) 
                        for i in range(len(mask)) 
                        if mask[i] != 'X' ]
            else:
                mem_loc, mem_val = tuple(map(int, re_findall(re_nums, l)))
                for (bit_i, bit_val) in overwrites:
                    mem_val = modify_bit(bit_i, bit_val, mem_val)
                mem[mem_loc] = mem_val

    print(sum(mem.values()))



