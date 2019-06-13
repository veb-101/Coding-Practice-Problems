# https://app.codesignal.com/challenge/vJMeEAya7gEckYfQW?solutionId=43t4tzMo4mL3PFNWo
'''
Given an integer n consisting of an even number of digits, swap pairs of
adjacent digits in it, i.e. swap the first digit with the second one, the third
digit with the fourth one, etc.

Example

For n = 1234, the output should be
swapNeighbouringDigits(n) = 2143.
'''

import re


def swapNeighbouringDigits(n):
    n = str(n)
    l = ''
    for i in range(0, len(n), 2):
        b, a = n[i:i+2]
        l += a+b
    return int(l)


def swapNeighbouringDigits(n):
    return int(re.sub('(.)(.)', r'\2\1', str(n)))


print(swapNeighbouringDigits(12345678))
