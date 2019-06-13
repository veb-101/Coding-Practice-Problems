# https://app.codesignal.com/challenge/53DMcWRBbZMdsF6vm
'''
The factorial of n is defined as the product of all natural numbers
 up to and including n - 1 * 2 * 3 * ... * n. The quasifactorial of
 n is different in that after each multiplication the result is decreased
 by one. So the quasifactorial of n is (...((1 * 2 - 1) * 3 - 1) * ... * n - 1).
 The quasifactorial of 1 is 1.

Given a positive integer n, calculate its quasifactorial.

Example

For n = 4, the output should be
quasifactorial(n) = 7.
'''


def quasifactorial(n):
    t = 1
    for i in range(2, n + 1):
        t = ~-(t * i)
    return t


print(quasifactorial(4))

print(quasifactorial(8))
