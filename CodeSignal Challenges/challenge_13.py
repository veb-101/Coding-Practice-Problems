# https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n
'''
Given an integer index n, find the nth Fibonacci number.

Note: Write a solution with O(n) complexity
and O(1) additional memory.

Example

For n = 2, the output should be
fibonacciNumber(n) = 1.

F2 = F0 + F1 = 0 + 1 = 1
'''


def fibonacciNumber(n):
    a = 0
    b = 1
    if n == 1:
        return b
    else:
        for i in range(2, n+1):
            a, b = b, a + b
        return b


def fn(n):
    # if n > 0
    # binets
    # 1 ≤ n ≤ 15
    return round(1.6180**n / 5**.5)


def binet(n):
    # fails for n > 70
    phi = (1 + 5**.5) / 2
    psi = (1 - 5**.5) / 2
    return round((phi**n - psi**n) / 5**.5)


for i in range(1, 100):
    print(f"{i}-> ", end=" ")
    print(fibonacciNumber(i), end=", ")
    # print(fn(i), end=" ")
    print(binet(i))
    print()
