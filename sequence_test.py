import math
from sympy import *


import timeit


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


self_list = [-2, 94, 864, 3844, 12010, 30258, 65884, 129064, 233334]

def delta(repeat=1):
    if repeat <= 0:
        return list
    if repeat != 1:
        return delta(delta(list), repeat - 1)
    return [list[x + 1] - list[x] for x in range(len(list) - 1)]


def delta2(list, repeat=1):
    if repeat <= 0:
        return list
    if repeat != 1:
        return delta(delta(list), repeat - 1)
    return list(map(lambda q, r: r - q, [0] + list, list))[1:]


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


t1 = timeit.Timer("delta(self_list)", "from sequence_test import delta")

print(t1.timeit(number=100))

# b = seq([3, 9, 27, 81, 243])

# for i in range(10):
#     start_time = datetime.now()
#     print(a.delta(i))
#     print(f'Duration Δ1:\t{datetime.now() - start_time}')
#
#     start_time = datetime.now()
#     print(a.delta2(i))
#     print(f'Duration Δ2:\t{datetime.now() - start_time}')
#
#     print('\n')

# deltatime = datetime.now() - datetime.now()
# delta2time = datetime.now() - datetime.now()
# for i in range(1,1000):
#     start_time = datetime.now()
#     a.delta()
#     end_time = datetime.now()
#     deltatime += end_time - start_time
#     # print(f'Delta Non:\t{end_time - start_time}')
#
#     start_time = datetime.now()
#     a.delta2()
#     end_time = datetime.now()
#     delta2time += end_time - start_time
#     # print(f'Delta Map:\t{end_time - start_time}')
# print(f'1Delta Non:\t{deltatime/1000}')
# print(f'1Delta Map:\t{delta2time/1000}')


# print(f'{a.sequence}')
# start_time = datetime.now()
# print(a.equation)
# print(f'Duration: {datetime.now() - start_time}')
# exec(f'print([int({a.equation}) for x in range(1,10)])')

# for i in range(0,5):
#     start_time = datetime.now()
#     print(seq.delta(a, i).equation)
#     print(datetime.now()-start_time)

# counter = 0
# start_time = datetime.now()
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for l in range(10):
#                 a = seq([(i * (x ** 3) + j * (x ** 2) + k * x + l) for x in range(1, 10)])
#                 exec(f'test_sequence = [int({a.equation}) for x in range(1,10)]')
#                 if a.sequence == test_sequence:
#                     counter += 1
#                 else:
#                     print(f'{a.sequence} = {test_sequence}: {a.sequence == test_sequence}')
#                 if counter % 100 == 0:
#                     print(counter)
# print(datetime.now()-start_time)
