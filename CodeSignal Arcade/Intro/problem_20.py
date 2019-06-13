# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
'''
Given an array of integers, find the maximal absolute difference between any
two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
'''


def arrayMaximalAdjacentDifference(a):
    mine = []
    for i in range(len(a) - 1):
        mine.append(abs(a[i] - a[i + 1]))
    return max(mine)


print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))
print(arrayMaximalAdjacentDifference([1, 7, 1, 6]))
