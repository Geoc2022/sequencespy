from numpy import array
from math import factorial
from numpy import diff
from numpy import cumsum
from sympy import expand


# def r_ex(power, variable_name='x'):
#     if power == 0:
#         return 1
#     return '*'.join([f'({variable_name}+{difference})' for difference in range(power)])


def falling_ex(power: int, variable_name='x'):
    if power == 0:
        return 1
    return '*'.join([f'({variable_name}-{i})' for i in range(power)])


def delta(sequence, n=1):
    return diff(sequence, n)


def delta_x(sequence, n=1):
    if n <= 0:
        return sequence
    if n != 1:
        return delta_x(delta_x(sequence), n - 1)
    return sequence[1:] / sequence[:-1]


def s_sum(seq, n=1, init=0):
    if n <= 0:
        return seq
    if n != 1:
        return s_sum(cumsum(seq), n - 1, init)
    return cumsum(seq)


def jackson_difference_fan(sequence, n=1):
    if n <= 0:
        return sequence
    if n != 1:
        return jackson_difference_fan(jackson_difference_fan(sequence), n - 1)
    return array([delta(sequence, i)[0] for i in range(1, len(sequence))])


def formula(seq):
    temp_seq = array(seq)
    deltas_list = [temp_seq[0]]
    while (not all(delta(temp_seq) == 0)) and delta(temp_seq).size:
        temp_seq = delta(temp_seq)
        deltas_list.append(temp_seq[0])
    equation_str = ''
    initial_coefficient = 0
    for inv_delta_depth in range(len(deltas_list) - 1, -1, -1):
        initial_coefficient = deltas_list[inv_delta_depth] - initial_coefficient
        equation_str += f'({initial_coefficient / factorial(inv_delta_depth)})*({falling_ex(inv_delta_depth)})+'
    return expand(equation_str[:-1])


def e_formula(seq):
    temp_seq = seq
    for depth in range(len(seq)):
        previous_initial = temp_seq[0]
        temp_seq = jackson_difference_fan(temp_seq)
        if all(temp_seq) == 0:
            leading_exponent = depth + 1
            break
    else:
        return formula(seq)
    leading_exponent_co = int(previous_initial / (factorial(depth)))
    leading_exponent_array_diff = seq - array([leading_exponent_co * (leading_exponent ** n) for n in range(len(seq))])
    if all(leading_exponent_array_diff) == 0:
        return f'{leading_exponent_co}*{leading_exponent}**x'
    else:
        return f'{leading_exponent_co}*{leading_exponent}**x + {e_formula(leading_exponent_array_diff)}'
