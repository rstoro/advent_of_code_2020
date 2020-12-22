#!/usr/bin/env python3
from re import match as re_match
from re import compile as re_compile


if __name__ == '__main__':
    # given
    rules, messages = [], []
    with open('input.txt', 'r') as f:
        while l := f.readline().strip():
            rules.append( l.split(': ')[1].replace( '"', '').split(' ') )

        while l:= f.readline():
            messages.append(l.strip())
    
    gen_regex = lambda pointer, rules: pointer if not pointer.isnumeric() \
            else f'(?:{ "".join(gen_regex(p, rules) for p in rules[int(pointer)]) })'

    # part 1
    regexp = re_compile(f'^{ gen_regex("0") }$')
    matches = [ re_match(regexp, message) for message in messages ]
    print(sum(1 for match in matches if match != None))


