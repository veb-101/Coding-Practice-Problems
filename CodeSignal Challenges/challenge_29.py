# https://app.codesignal.com/challenge/jpaALgHRyNZCcuakt
'''
Given an integer n, find the number of trailing zeros in the decimal
representation of n! (the exclamation mark means factorial).

Example

For n = 10, the output should be
factorialTrailingZeros(n) = 2.
10! = 3628800, it has 2 trailing zeros.
'''

# Matching challenge requirements 10 <= n <= 35


def factorialTrailingZeros(n):
    n //= 5
    return n if n < 5 else n + 1


def factorialTrailingZeros(n):
    return n//4.3

# works for all


def factorialTrailingZeros(n):
    if n < 4:
        return 0
    else:
        x = n // 5
        return x + factorialTrailingZeros(x)


for i in range(10, 101):
    print(f"{i} -> {factorialTrailingZeros(i)}")
