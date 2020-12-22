#!/usr/bin/env python3


def parse_rule(rule, rules):
    new_rule = []

    for sub_rule in rule:
        new_sub_rule = ['']

        for val in sub_rule:
            if type(val) == int:
                rule_from_val = parse_rule(rules[val], rules) 

                revisioned_sub_rules = []
                for prefix in new_sub_rule:
                    for sub_rules_from_val in rule_from_val:
                        for suffix in sub_rules_from_val:
                            revisioned_sub_rules.append(prefix + suffix)

                new_sub_rule = revisioned_sub_rules[:]
            else:
                new_sub_rule = [ val ]
            
        new_rule.append(new_sub_rule)

    rules[rules.index(rule)] = new_rule
    return new_rule


if __name__ == '__main__':
    # given
    rules, messages = [], []
    with open('input_example.txt', 'r') as f:
        while l := f.readline().strip():
            new_r = ( r.replace('"', '').split(' ') 
                    for r in l.split(': ')[1].split(' | ') )
            rules.append([ list(map(int, r)) if r[0].isnumeric() else r for r in new_r ])

        while l:= f.readline():
            messages.append(l.strip())
    
    # part 1
    rule_zero = parse_rule(rules[0], rules[:])[0]
    print(rule_zero)
    print(sum(message in rule_zero for message in messages))
