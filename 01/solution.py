#!/usr/bin/env python3
from functools import reduce


def get_summation_equal_to(numbers, summation, amount_of_numbers=2):
    for i in range(0, len(numbers)):
        guess = summation - numbers[i]
        if amount_of_numbers - 2 != 0:
            rest = get_summation_equal_to(
                    numbers=numbers[:i] + numbers[i+1:], 
                    summation=guess, 
                    amount_of_numbers=amount_of_numbers-1)
            if rest:
                return *rest, numbers[i]
        elif guess in numbers:
            return numbers[i], guess


if __name__ == '__main__':
    # given
    with open('input.txt', 'r') as f:
        ns = [ int(l) for l in f.readlines() ]

    mult = lambda a, b: a* b

    # part 1
    solution_one = get_summation_equal_to(ns, 2020)
    print(f'Solution 1: { reduce(mult, solution_one) }')

    # part 2
    solution_two = get_summation_equal_to(ns, 2020, 3)
    print(f'Solution 2: { reduce(mult, solution_two) }')



