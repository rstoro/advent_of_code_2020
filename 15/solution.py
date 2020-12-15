#!/usr/bin/env python3


def memory_game(nums):
    mem = { nums[i]: i+1 for i in range(len(nums)) }

    for num in nums:
        yield num

    prev, i = 0, len(nums) + 1
    while True:
        age = i - mem[prev] if prev in mem else 0
        yield prev
        mem[prev] = i
        prev = age
        i += 1


if __name__ == '__main__':
    # given
    starting_numbers = [ 18, 8, 0, 5, 4, 1, 20 ]

    # part 1
    turn = memory_game(starting_numbers)
    for _ in range(2020-1):
        next(turn)
    print(next(turn))

    # part 2
    turn = memory_game(starting_numbers)
    for _ in range(30000000-1):
        next(turn)
    print(next(turn))

