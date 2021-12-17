import math
from sympy import *


def recursive(formula, a, steps=10):
    for n in range(len(a) + 1, steps + 1):
        try:
            exec(f'a.append({formula})')
        except IndexError:
            return 'invalid function'
    return a


def r_ex(power, variable_name='x'):
    if power == 0:
        return 1
    return '*'.join([f'({variable_name}+{difference})' for difference in range(power)])


def f_ex(power, variable_name='x'):
    if power == 0:
        return 1
    return '*'.join([f'({variable_name}-{i})' for i in range(power)])


class seq:
    def __init__(self, list_sequence):
        self.sequence = list_sequence

    def __getattr__(self, method):
        return getattr(self.sequence, method)

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        return self.sequence[item]

    def __repr__(self):
        return self.sequence

    def __str__(self):
        return str(self.sequence)

    def s_sum(self, repeat=1, initial=0):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.s_sum()).s_sum(repeat - 1)
        return seq([(sum(self.sequence[0:x]) + initial) for x in range(len(self) + 1)])

    def delta(self, repeat=1):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.delta()).delta(repeat - 1)
        return seq([self.sequence[x + 1] - self.sequence[x] for x in range(len(self) - 1)])

    def delta2(self, repeat=1):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.delta2()).delta2(repeat - 1)
        return seq(list(map(lambda q, r: r - q, [0] + self.sequence, self.sequence))[1:])

    def delta_x(self, repeat=1):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.delta_x()).delta_x(repeat - 1)
        return seq([(self.sequence[x + 1] / self.sequence[x]) for x in range(len(self) - 1)])

    def delta_x2(self, repeat=1):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.delta_x2()).delta_x2(repeat - 1)
        return seq(list(map(lambda q, r: r / q, self.sequence, self.sequence + [0])))

    def multi_list(self, mul=1):
        for item in self:
            mul *= item
        return mul

    def x_sum(self, repeat=1, initial=0):
        if repeat <= 0:
            return self
        if repeat != 1:
            return (self.x_sum()).x_sum(repeat - 1)
        return seq([(seq.multi_list(self.sequence[0:x]) * initial) for x in range(len(self) + 1)])

    @property
    def equation(self):
        temp_seq = self
        deltas_list = [temp_seq[0]]
        while sum(temp_seq.delta()) != 0:
            temp_seq = temp_seq.delta()
            deltas_list.append(temp_seq[0])
        equation = ''
        initial_coefficient = 0
        for inv_delta_depth in range(len(deltas_list) - 1, -1, -1):
            initial_coefficient = deltas_list[inv_delta_depth] - initial_coefficient
            equation += f'({initial_coefficient / math.factorial(inv_delta_depth)})*({f_ex(inv_delta_depth)})+'
        return expand(equation[:-1])

    @property
    def equation2(self):
        temp_seq = self
        deltas_list = [temp_seq[0]]
        while sum(temp_seq.delta2()) != 0:
            temp_seq = temp_seq.delta2()
            deltas_list.append(temp_seq[0])
        equation = ''
        initial_coefficient = 0
        for inv_delta_depth in range(len(deltas_list) - 1, -1, -1):
            initial_coefficient = deltas_list[inv_delta_depth] - initial_coefficient
            equation += f'({initial_coefficient / math.factorial(inv_delta_depth)})*({f_ex(inv_delta_depth)})+'
        return expand(equation[:-1])

    @property
    def depth(self):
        counter = 0
        temp_seq = self
        while sum(temp_seq.delta()) != 0:
            temp_seq = temp_seq.delta()
            counter += 1
            print(temp_seq)
        return counter


a = seq([1,2,3,6])
print(a.equation)
