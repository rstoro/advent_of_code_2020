#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    # given
    seats = []
    with open('input.txt', 'r') as f:
        while l := f.readline():
            seats.append( list(l.strip()) )
    
    # run
    EMPTY, FLOOR, OCCUPIED = ('L', '.', '#')
    rows, cols, iterations = len(seats), len(seats[0]), 1000

    check = lambda l, v: 1 if l and l[v] == OCCUPIED else 0
    for i in range(iterations):
        new_seats = [ r[:] for r in seats ]

        for r in range(rows):
            for c in range(cols):
                left = check([ v 
                        for v in seats[r][:c] 
                        if v != FLOOR ], -1)
                right = check([ v 
                        for v in seats[r][c+1:] 
                        if v != FLOOR ], 0)
                up = check([ seats[j][c] 
                        for j in range(r)
                        if seats[j][c] != FLOOR ][::-1], 0)
                down = check([ seats[j][c] 
                        for j in range(r+1, rows) 
                        if seats[j][c] != FLOOR ], 0)
                left_up = check([ seats[r-j][c-j] 
                        for j in range(1, min(r+1, c+1))
                        if seats[r-j][c-j] != FLOOR], 0)
                left_down = check([ seats[r+j][c-j] 
                        for j in range(1, min(rows-r, c+1))
                        if seats[r+j][c-j] != FLOOR], 0)
                right_up = check([ seats[r-j][c+j] 
                        for j in range(1, min(r+1, cols-c))
                        if seats[r-j][c+j] != FLOOR], 0)
                right_down = check([ seats[r+j][c+j] 
                        for j in range(1, min(rows-r, cols-c))
                        if seats[r+j][c+j] != FLOOR], 0)

                count = sum([up,down,left,right,left_down,left_up,right_down,right_up])

                if seats[r][c] == OCCUPIED and count >= 5:
                    new_seats[r][c] = EMPTY
                elif seats[r][c] == EMPTY and count == 0:
                    new_seats[r][c] = OCCUPIED

        seats = [ r[:] for r in new_seats ]
        print(sum(seats[r].count(OCCUPIED) for r in range(rows)))

