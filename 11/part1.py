#!/usr/bin/env python3
from functools import reduce


if __name__ == '__main__':
    # given
    seats, board_len = [], 0
    with open('input.txt', 'r') as f:
        while l := f.readline():
            seats.extend( list(l.strip()) )
            if board_len == 0:
                board_len = len(seats)

    board_size = len(seats)
    iterations = 1000

    # run
    NONE, TOP_EDGE, LEFT_EDGE, RIGHT_EDGE, BOTTOM_EDGE = (0, 1, 2, 4, 8)
    EMPTY, FLOOR, OCCUPIED = ('L', '.', '#')
    is_upper_edge = lambda i, bl, bs: TOP_EDGE if i < bl else NONE
    is_left_edge = lambda i, bl, bs: LEFT_EDGE if i % bl == 0 else NONE
    is_right_edge = lambda i, bl, bs: RIGHT_EDGE if (i + 1) % bl == 0 else NONE
    is_lower_edge = lambda i, bl, bs: BOTTOM_EDGE if i > bs - bl - 1 else NONE
    edge_map = [ is_upper_edge, is_left_edge, is_right_edge, is_lower_edge ]
    get_light_location = lambda i, bl ,bs: reduce(lambda a, b: a ^ b, \
            ( f(i, bl, bs) for f in edge_map ), 0)
    
    # print board
    print(f'step 0')
    for l in range(0, board_size, board_len):
        print(''.join(seats[l:l+board_len]))
    print()

    for k in range(iterations):
        
        new_seats = seats[:]
        for i in range(board_size):
            locations = []
            light_location = get_light_location(i, board_len, board_size)

            if light_location == TOP_EDGE:
                locations = [ i-1, i+1, i-1+board_len, i+board_len, i+1+board_len ]
            elif light_location == LEFT_EDGE:
                locations = [ i-board_len, i+1-board_len, i+1, 
                        i+board_len, i+1+board_len ]
            elif light_location == TOP_EDGE ^ LEFT_EDGE:
                locations = [ i+1, i+board_len, i+1+board_len ]
            elif light_location == RIGHT_EDGE:
                locations = [ i-board_len, i-1-board_len, i-1, 
                        i+board_len, i+board_len-1 ]
            elif light_location == TOP_EDGE ^ RIGHT_EDGE:
                locations = [ i+1+board_len, i+board_len, i-1 ]
            elif light_location == BOTTOM_EDGE:
                locations = [ i-1, i+1, i-1-board_len, i-board_len, i+1-board_len ]
            elif light_location == LEFT_EDGE ^ BOTTOM_EDGE:
                locations = [ i-board_len, i+1-board_len, i+1 ]
            elif light_location == RIGHT_EDGE ^ BOTTOM_EDGE:
                locations = [ i-board_len, i-1-board_len, i-1 ]
            elif light_location == NONE:
                locations = [ i-board_len-1, i-board_len, i-board_len+1,
                        i-1, i+1, i+board_len-1, i+board_len, i+board_len+1 ] 
            else:
                assert(False)   #TODO: throw real exception
            
            count = sum(1 if seats[j] == OCCUPIED else 0 for j in locations)
            if seats[i] == OCCUPIED and count >= 4:
                new_seats[i] = EMPTY
            elif seats[i] == EMPTY and count == 0:
                new_seats[i] = OCCUPIED

        seats = new_seats[:]

        # print board
        print(f'step { k + 1}')
        for l in range(0, board_size, board_len):
            print(''.join(seats[l:l+board_len]))
        print(sum(1 if seats[l] == OCCUPIED else 0 for l in range(board_size)))
        print()

