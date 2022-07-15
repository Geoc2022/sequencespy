from umbral import *


def clean_sequence(sequence_str):
    sequence_list = []
    sequence_str_list = (sequence_str.replace(', ', ',')).split(',')
    for item in sequence_str_list:
        if item.isnumeric():
            sequence_list.append(float(item))
    print(f'\n{sequence_list}')
    return sequence_list


if input('Is the sequence polynomial or exponential based? (p/e)\t').lower() == 'e':
    sequence = array(clean_sequence(input('Enter the exponential based sequence:\n')))
    print(e_formula(sequence))
else:
    sequence = array(clean_sequence(input('Enter the polynomial based sequence:\n')))
    print(formula(sequence))

# # Delta
# a = array([n * (n + 1) * (n + 2) / 6 for n in range(1, 10)])
# for i in range(4):
#     print(delta(a, i))
#
# # Delta_x
# a = array([factorial(n) for n in range(1, 10)])
# print(delta_x(a))
#
# # Continued Summation
# a = array([1 for n in range(1, 10)])
# for i in range(4):
#     print(s_sum(a, i))
#
# # Jackson's Difference Fan (altered)
# a = array([2 ** n for n in range(1, 10)])
# for i in range(3):
#     print(jackson_difference_fan(a, i))
#
# # Falling exponent
# print(falling_ex(3))
