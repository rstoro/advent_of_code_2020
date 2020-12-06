#!/usr/bin/env python3


if __name__ == '__main__':
    # given
    cases = []
    with open('input.txt', 'r') as f:
        for l in f.readlines():
            rule, password = l.strip().split(':')
            rule_range, rule_chr = rule.split(' ')
            start, end = rule_range.split('-')
            cases.append((int(start), int(end), rule_chr, password))

    # part 1
    count_is_valid = lambda s, e, c, p: s <= p.count(c) <= e
    solution_one = sum(int(count_is_valid(*case)) for case in cases)
    print(solution_one)

    # part 2
    position_is_valid = lambda s, e, c, p: (p[s] == c) ^ (p[e] == c)
    solution_two = sum(int(position_is_valid(*case)) for case in cases)
    print(solution_two)
