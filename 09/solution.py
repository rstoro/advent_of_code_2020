#!/usr/bin/env python3


class SummationBuffer(object):
    def __init__(self, size):
        self.__size = size
        self.__vals = []
        self.__sums = []
        self.__pointer = 0


    def __len__(self):
        return len(self.__vals)


    def __str__(self):
        return ','.join(map(str, zip(self.__vals, self.__sums)))


    def __min__(self):
        return min( val for i in range(self.__size) for val in self._sums[i] )


    def __max__(self):
        return max( val for i in range(self.__size) for val in self._sums[i] )


    def __retroactively_sum(self, val):
        # this is going to walk each value and append the new sum to the list
        # appending is relative to values in the buffer, not the max buffer size
        for i in range(len(self.__vals) - 1):
            cur_pointer = (self.__pointer + i) % len(self.__vals)
            self.__sums[cur_pointer].append(self.__vals[cur_pointer] + val)


    def push(self, val):
        if len(self.__vals) == self.__size:
            self.__vals[self.__pointer] = val
            self.__sums[self.__pointer] = []
        else:
            self.__vals.append(val)
            self.__sums.append([])

        # NOTE: make sure to update pointer before summing
        self.__pointer = (self.__pointer + 1) % self.__size
        self.__retroactively_sum(val)


    def get(self):
        return map(str, zip(self.__vals, self.__sums))


    def get_sums(self):
        return [ num for i in range(len(self.__sums)) for num in self.__sums[i] ]
    

    def get_vals(self):
        return self.__vals[:]   #do not pass by ref, pass a copy
    

if __name__ == '__main__':
    # given
    with open('input.txt', 'r') as f:
        cypher = [ int(l.strip()) for l in f.readlines() ]

    preamble = 25
    summation_buffer = SummationBuffer(preamble)

    # part 1
    invlaid_val = None
    for val in cypher:
        if len(summation_buffer) == preamble and val not in summation_buffer.get_sums():
            invalid_val = val
            break
        summation_buffer.push(val)

    print(invalid_val)

    # part 2
    weakness = []
    for i in range(len(cypher) - 1):
        val = cypher[i]
        j = i+1
        while (val := val + cypher[j]) <= invalid_val and j < len(cypher):
            if val == invalid_val:
                weakness.extend(cypher[i:j+1])
                break
            j+=1

    print(min(weakness) + max(weakness))
