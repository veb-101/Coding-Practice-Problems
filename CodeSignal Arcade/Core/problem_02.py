# https://app.codesignal.com/arcade/code-arcade/intro-gates/SZB5XypsMokGusDhX
'''
Given an integer n, return the largest number that contains
exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99
'''


def largestNumber(n):
    return 10 ** n - 1


print(largestNumber(2))
print(largestNumber(1))
print(largestNumber(7))
print(largestNumber(4))
