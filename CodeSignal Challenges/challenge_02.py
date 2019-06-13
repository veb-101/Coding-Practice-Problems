# https://app.codesignal.com/challenge/w5Hu5cMNCf5BKsZee?solutionId=FQkhMveNAnFR5fcxy

'''
We need to turn a mixed fraction into an improper reduced fraction

Example

For a = [3, 1, 2], the output should be
mixedFractionToImproper(a) = [7, 2].

Explanation: 3 + 1/2 = 7/2.

'''


def mixedFractionToImproper(a):
    x = []
    x.append(a[0] * a[-1] + a[1])
    x.append(a[-1])
    return x


def mixedFractionToImproper(a):
    return [a[0] * a[2] + a[1]] + [a[2]]
