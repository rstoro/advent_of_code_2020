#!/usr/bin/env python3
from collections import defaultdict


def evaluate(sequence, i=-1):
    total = 0
    expression = '+'
    i = [ i + 1 ]

    while i[0] < len(sequence):
        val = sequence[i[0]]

        if val == '(':
            sub_total, i[0] = evaluate(sequence, i[0])
            if expression == '+':
                total += sub_total
            elif expression == '*':
                total *= sub_total if total != 0 else sub_total
        elif val == ')':
            return total, i[0]
        elif val in '+*':
            expression = val
        else:
            if expression == '+':
                total += int(val)
            elif expression == '*':
                total *= int(val) if total != 0 else int(val)

        i[0] += 1

    return total


if __name__ == '__main__':
    # given
    expressions = []
    with open('input.txt', 'r') as f:
        while l := f.readline():
            expressions.append(list(l.strip().replace(' ', '')))

    # part 1
    print(sum(evaluate(expression) for expression in expressions))

    # part 2
    total = 0
    for expression in expressions:
        add, mul = [], []
        priority, expression_i = 0, 1
        for i in range(len(expression)):
            if expression[i] == '(':
                priority += 1
            elif expression[i] == ')':
                priority -= 1
            elif expression[i] == '+':
                add.append( (expression_i-1, expression_i, '+', priority) )
                expression_i += 1
            elif expression[i] == '*':
                mul.append( (expression_i-1, expression_i, '*', priority) )
                expression_i += 1

        points = sorted(add + mul, key=lambda abp: abp[3], reverse=True)
        attrs = [ int(n) for n in expression if n.isnumeric() ]

        # I hate myself for this
        linked = defaultdict(set)
        for p1, p2, op, _ in points:
            n1, n2 = attrs[p1], attrs[p2]
            val = n1 * n2 if op == '*' else n1 + n2

            all_p = [ p1, p2, *linked[p1], *linked[p2] ]
            for p in all_p: 
                linked[p].update(all_p)
                attrs[p] = val

        total += val

    print(total)

