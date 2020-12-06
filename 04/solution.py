#!/usr/bin/env python3
from re import findall as re_findall

if __name__ == '__main__':
    # given
    fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
    ignored = ['cid']
    with open('input.txt', mode='r') as f:
        # TODO: can this be converted into a FSM?
        passports = [ dict(kv.split(':') for kv in p.strip().replace('\n',' ').split(' '))
                for p in re_findall(r'[\s\S]+?(?:\n\n|(?!\n)$)', ''.join(f.readlines())) ]

    # conditions
    fields_valid = lambda fs, i, ks: all(f in ks if f not in i else True for f in fs )
    birthyear_valid = lambda byr: 1920 <= int(byr) <= 2002 and len(byr) == 4
    issueyear_valid = lambda iyr : 2010 <= int(iyr) <= 2020 and len(iyr) == 4
    expiration_valid = lambda eyr: 2020 <= int(eyr) <= 2030 and len(eyr) == 4
    height_valid = lambda hgt: 150 <= int(hgt.split('cm')[0]) <= 193 \
            if 'cm' in hgt else 59 <= int(hgt.split('in')[0]) <= 76
    haircolor_valid = lambda hcl: hcl[0] == '#' and len(hcl[1:]) == 6 \
            and all(c in '0123456789abcdef' for c in hcl[1:])
    eyecolor_valid = lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    passport_id_valid = lambda pid: len(pid) == 9
    country_id_valid = lambda cid: True #override

    validation_map = { 'byr': birthyear_valid, 'iyr': issueyear_valid,
            'eyr': expiration_valid, 'hgt': height_valid, 'hcl': haircolor_valid,
            'ecl': eyecolor_valid, 'pid': passport_id_valid, 'cid': country_id_valid }
    
    # part 1
    s1 = sum(fields_valid(fields, ignored, passport.keys()) for passport in passports)
    print(s1)

    # part 2
    s2 = sum(all(validation_map[k](p[k]) if k not in ignored else True for k in p.keys())
            for p in passports if fields_valid(fields, ignored, p.keys()))
    print(s2)


