#!/usr/bin/env python3


class Handheld(object):
    NOP = 0
    JMP = 1
    ACC = 2
    OP_MAP = { 'nop': NOP, 'jmp': JMP, 'acc': ACC }


    def __init__(self):
        self._instructions = []
        self._acc = 0
        self._i = 0

    
    def load_firmware(self, firmware):
        self._instructions = []
        for instruction in firmware:
            op, arg = instruction.split(' ')
            premise, amount = arg[0], int(arg[1:])
            self._instructions.append( (self.OP_MAP[op], premise, amount) )


    def run(self):
        self._i = 0
        self._acc = 0
        seen = []

        while self._i != len(self._instructions):
            if self._i in seen:
                break

            seen.append(self._i)
            self.step(self._get_instruction())

        return self._acc


    def firmware_is_valid(self):
        seen = []

        while self._i != len(self._instructions):
            if self._i in seen:
                self._acc = 0
                return False

            seen.append(self._i)
            self.step(self._get_instruction())

        self._acc = 0
        return True


    def step(self, instruction):
        op, premise, amount = instruction

        if op == self.NOP:
            self._set_i(self._i + 1)
        elif op == self.ACC:
            self._acc = self._acc + amount if premise == '+' else self._acc - amount
            self._set_i(self._i + 1)
        elif op == self.JMP: 
            self._set_i(self._i + amount if premise == '+' else self._i - amount)


    def _get_instruction(self):
        return self._instructions[self._i]


    def _set_i(self, i):
        self._i = i


if __name__ == '__main__':
    # given
    firmware = []
    with open('input.txt', 'r') as f:
        while l := f.readline():
            firmware.append(l.strip())

    handheld = Handheld()

    # part 1
    handheld.load_firmware(firmware)
    print(handheld.run())

    # part 2
    flipflop = lambda op: 'jmp' if op == 'nop' else 'nop' if op == 'jmp' else op
    for i in range(len(firmware)):
        op, arg = firmware[i].split(' ', 1)
        if op in ['nop', 'jmp']:
            new_firmware = firmware[:i] + [ f'{ flipflop(op) } { arg }' ] + firmware[i+1:]
            handheld.load_firmware(new_firmware)
            if handheld.firmware_is_valid():
                break

    print(handheld.run())


