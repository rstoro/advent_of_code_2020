#!/usr/bin/env python3
from functools import reduce


def alg_x(l, solution=[]):
    if not l:
        yield list(solution)
    else:
        c = min(l, key=lambda c: len(l[c]))
        for n in list(l[c]):
            # append to solution
            solution.append( (c, n) )

            # rm col
            col = []
            for k in l:
                if n in l[k]:
                    l[k].remove(n)
                    col.append(k)

            # rm row
            tmp = l.pop(c)

            # recurse
            for s in alg_x(l,  solution):
                yield s

            # readd row
            l[c] = tmp

            # readd col
            for i in col:
                l[i].add(n)

            # remove from solution
            solution.pop()


if __name__ == '__main__':
    # given
    rules, my_ticket, other_tickets = {}, [], []
    with open('input.txt', 'r') as f:
        # ticket rules
        while True:
            if not (l := f.readline().strip()):
                break

            name, instructions = l.split(': ')
            rules[name] = []
            for instruction in instructions.split(' or '):
                s, e = tuple(map(int, instruction.split('-')))
                rules[name].extend(list(range(s, e+1)))

        # my ticket
        f.readline()
        my_ticket = [ int(n) for n in f.readline().strip().split(',') ]
        
        # other tickets
        f.readline()
        f.readline()
        while (l := f.readline().strip()):
            other_tickets.append([ int(n) for n in l.split(',') ])


    # part 1
    valid_numbers = set(n for l in rules.values() for n in l )
    print(sum(n for t in other_tickets for n in t if n not in valid_numbers))

    # part 2
    valid_tickets = [ t 
            for t in other_tickets 
            if not any(n for n in t if n not in valid_numbers ) ]

    # transposition for each value to determine which rules validate
    validation_map = { field_i: [ key
            for (key, rule) in rules.items()
            if all(n in rule for n in transposition) ]
            for (field_i, transposition) in enumerate(zip(*valid_tickets)) }

    # dict of positions in relation to the ticket, and their possible validations
    position_map = {}
    for field_i, possible_rules in validation_map.items():
        for rule in possible_rules:
            if rule not in position_map:
                position_map[rule] = set()

            position_map[rule].add(field_i)

    solution = next(alg_x(position_map, []))
    decoded_ticket = { rule: my_ticket[ticket_i] for (rule, ticket_i) in solution }
    departures = (decoded_ticket[k] for k in decoded_ticket if 'departure' in k)
    mult = lambda a, b: a*b
    print(reduce(mult, departures, 1))


