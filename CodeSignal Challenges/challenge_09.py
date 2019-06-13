# https: // app.codesignal.com/challenge/hDqJT8AqKJAQS4vEw
'''
Given a number and a range, find the largest integer within the given range
that's divisible by the given number.

Example

For left = 1, right = 10, and divisor = 3, the output should be
maxDivisor(left, right, divisor) = 9.
The largest integer divisible by 3 in range[1, 10] is 9.
'''


def maxDivisor(left, right, divisor):
    return max([i if not i % divisor else -1 for i in range(left, right+1)])


def maxDivisor(a, b, c):
    print(-(b - b % c < a))
    print(b - b % c)
    return -(b - b % c < a) | b - b % c


def maxDivisor(l, r, d):
    return r-r % d >= l and r-r % d or -1


def maxDivisor(l, r, d):
    return -1 if r % d > r-l else r-r % d


left = 1
right = 10
divisor = 3
# ans = 9

left = -99
right = -96
divisor = 5
# ans = -1
print(maxDivisor(left, right, divisor))
