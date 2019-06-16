# https://app.codesignal.com/challenge/Xa5wqxrtQB9e47Yeq
'''
Write an algorithm that constructs an array of non unique prime factors of a
number n.

Example

For n = 100, the output should be
primeFactors(n) = [2, 2, 5, 5].
'''

# https://www.mathsisfun.com/prime-factorization.html


def primeFactors(n):
    result = []
    for i in range(2, n):
        while n % i == 0:
            n //= i
            result.append(i)
        if n == 1:
            break
    if n > 1:
        result.append(n)
    return result


def primeFactors(n):
    r = []
    x = 2
    while n > 1:
        while n % x:
            x += 1
        r += x,
        n /= x
    return r


for i in range(1, 151):
    print(f"{i:03} -> {primeFactors(i)}")
