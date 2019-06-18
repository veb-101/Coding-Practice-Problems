# https://app.codesignal.com/challenge/nckaDwhQf2gb4HFhS
'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
'''

import numpy as np


def evenDigitsOnly(n):
    return sum(np.array([int(i) for i in str(n)]) % 2) == 0
    # return sum([1  if int(j) %2 else 0  for i in str(n) for j in i ]) == 0


def evenDigitsOnly(n):
    if len(str(n)) <= 1:
        return not n % 2
    else:
        return (n % 10) % 2 == 0 and evenDigitsOnly(n // 10)

# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/


def evenDigitsOnly(n):
    return not {*"13579"} & {*str(n)}


l = [248622, 642386, 248842, 1, 8, 2462487,
     468402800, 2468428, 5468428, 7468428]

for j, i in enumerate(l, 1):
    print(f'{j:02}: {i} -> {evenDigitsOnly(i)}')
