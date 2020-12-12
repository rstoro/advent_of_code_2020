#!/usr/bin/env python3


def path_combinations():
    a, b, c = 0, 1, 1
    while True:
        yield a
        a, b, c = b, c, a+b+c


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        adapters = sorted( int(l.strip()) for l in f.readlines() )

    # part 1
    difs, prev = [], 0
    for joltage in adapters:
        difs.append(joltage-prev)
        prev = joltage
    difs.append(3)
    print(difs.count(1) * difs.count(3))

    # part 2
    # possible      1 2 3 4 5 6 ...
    # combinations  1 1 2 4 7 13 ...
    # formula       nk = n↓k-1 + n↓k-2 + n↓k-3
    pcs_gen = path_combinations()
    count, total, pcs = 0, 1, []
    for dif in difs:
        count += 1

        if dif == 3:
            while len(pcs) <= count:
                pcs.append(next(pcs_gen))

            total *= pcs[count]
            count = 0

    print(total)

