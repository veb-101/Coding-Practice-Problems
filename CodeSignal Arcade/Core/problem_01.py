# https://app.codesignal.com/arcade/code-arcade/intro-gates/wAGdN6FMPkx7WBq66
'''
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.
'''


def addTwoDigits(n):
    return n // 10 + n % 10


# def addTwoDigits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
