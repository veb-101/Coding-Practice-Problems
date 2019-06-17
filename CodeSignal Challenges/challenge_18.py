# https://app.codesignal.com/challenge/j4tsozmpSzHSzS8sF
'''
Given an array of integers, find the number of inversions it contains.

Example

For inputArray = [1, 3, 2, 0], the output should be
countInversionsNaive(inputArray) = 4.
'''


def countInversionsNaive(i):
    a = len(i)
    return sum([1 for x in range(a) for y in range(x, a) if i[x] > i[y]])


print(countInversionsNaive([1, 3, 2, 0]))


def countInversionsNaive(inputArray):
    t = 0
    while inputArray:
        x, *inputArray = inputArray
        for y in inputArray:
            t += x > y
    return t


print(countInversionsNaive([1, 3, 2, 0]))
