#!/usr/bin/env python3


def flatten_deep(l):
    # NOTE: this is equivalent to raising a StopIteration after yielding the value
    #       which allows us to take advantage of the 'from' keyword while yielding
    if type(l) != list and type(l) != tuple:
        yield l
        return 

    for i in range(len(l)):
        yield from flatten_deep(l[i])


def evaluate_rule(rule):
    # NOTE: every rule has one of the following structures
    #       (a AND b)               [a, b]
    #       (a AND b AND c)         [a, b, c]
    #       (a AND b) OR (c AND d)  [[a, b], [c, d]]

    # DEBUG
    new_rule = []
    for subrule in rule:
        # (a AND b)
        if len(subrule) == 1:
            new_subrule = subrule[0]
        # (a AND b) OR (c AND d)
        elif len(subrule) == 2:
            prefixes, suffixes = subrule
            new_subrule = [ prefix + suffix
                    for prefix in prefixes
                    for suffix in suffixes ]
        # (a AND b AND c)
        elif len(subrule) == 3:
            prefixes = []
            for suffixes in subrule:
                prefixes = [ prefix + suffix
                        for prefix in prefixes or [ '' ]
                        for suffix in suffixes ]
            new_subrule = prefixes
        # no idea
        else:
            print('uh-oh')

        new_rule.extend( new_subrule )

    return new_rule


if __name__ == '__main__':
    # given
    rules, solved_rules, messages = {}, {}, []
    with open('input.txt', 'r') as f:
        while l := f.readline().strip():
            key, rule = l.split(': ')
            if rule[0].isnumeric():
                subrules = [ r.split(' ') for r in rule.split(' | ') ]
                parsed_subrules = [ list(map(int, subrule)) for subrule in subrules ]
                rules[int(key)] = parsed_subrules
            else:
                solved_rule = rule.replace('"', '')
                solved_rules[int(key)] = solved_rule

        while l:= f.readline():
            messages.append(l.strip())


    # format all rules
    while rules:
        # HACK: tuple() is copying the dictionary so we 
        # can modify the size durring subscription
        for solved_key, solved_rule in tuple(solved_rules.items()):
            for rule_key, rule in tuple(rules.items()):
                for subrule in rule:
                    for subrule_i, val in enumerate(subrule):
                        if val == solved_key:
                            subrule[subrule_i] = solved_rule

                if all( type(v) == str for v in flatten_deep(rule) ):
                    solved_rules[rule_key] = evaluate_rule(rule)
                    del rules[rule_key]

    # this is now empty
    del rules

    # part 1
    print(sum(message in solved_rules[0] for message in messages))

