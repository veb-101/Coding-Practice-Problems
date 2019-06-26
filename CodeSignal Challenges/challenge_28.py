# https://app.codesignal.com/challenge/JwirnFz8qyM87a3yG
'''
Implement a function that can subtract two reduced fractions and produce a
new one.

Example

For a = [7, 10] and b = [3, 10], the output should be
fractionSubtraction(a, b) = [2, 5].

7/10 - 3/10 = 4/10 = 2/5, so the answer is [2, 5].
'''

from fractions import Fraction as f
import numpy as np


def fractionSubtraction(a, b):
    a = f(*a) - f(*b)
    return a.numerator, a.denominator


def fractionSubtraction(a, b):
    a, b, c, d = *a, *b
    e = a * d - b * c, b * d
    e = e / np.gcd(*e)
    print(e)
    return e


print(fractionSubtraction([7, 10], [3, 10]))
