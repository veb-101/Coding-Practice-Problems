# https://app.codesignal.com/challenge/rCfCTkrbE4PDE9J2w?solutionId=daTseu4cdz2ThK7B7
'''
Implement a function that determines if a given positive integer
is a prime or not.

Example

For n = 47, the output should be
isPrime(n) = true;
For n = 4, the output should be
isPrime(n) = false.
'''


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0 and n > 2:
            return False
    return True


# https://en.wikipedia.org/wiki/Fermat_primality_test

# ~ binary operator -> complement the number
def isPrime(n):
    if n > 0:
        return f"{n}: {7 ** ~-n % n < 2}"
    else:
        return f"{n}: {False}"


def isPrime(n):
    if n > 0:
        return f"{n}: {2 ** n % n == 2 % n}"
    else:
        return f"{n}: {False}"


def isPrime(n):
    if n > 0:
        return f"{n}: {2 in [n, 2**n % n]}"
    else:
        return f"{n}: {False}"
