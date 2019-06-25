# https://app.codesignal.com/challenge/2S8ZobHRrpmFn4TiC
'''
Define GCPD (Greatest Common Prime Divisor) as the largest prime number that
divides both given positive integers. Your task is to find GCPD of the given
integers a and b.

Example

For a = 12 and b = 18, the output should be
greatestCommonPrimeDivisor(a, b) = 3;
For a = 12 and b = 13, the output should be
greatestCommonPrimeDivisor(a, b) = -1.
'''


def greatestCommonPrimeDivisor(a, b):
    for e in 7, 5, 3, -1:
        if a % e == b % e:
            return e


def greatestCommonPrimeDivisor(a, b):
    return [5, 7, -1, 3][b * 4 % 54 % 5]


print(greatestCommonPrimeDivisor(12, 13))

print(greatestCommonPrimeDivisor(12, 4))

print(greatestCommonPrimeDivisor(100, 140))

print(greatestCommonPrimeDivisor(12, 18))
