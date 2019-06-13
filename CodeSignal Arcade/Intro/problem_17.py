# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
'''
You are given an array of integers. On each move you are allowed to increase
exactly one of its element by one. Find the minimal number of moves required to
obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''


def arrayChange(inputArray):
    x, count = inputArray, 0
    for i in range(len(x) - 1):
        a, b = x[i], x[i + 1]
        if a >= b:
            count += a + 1 - b
            x[i + 1] = a + 1
    return count


print(arrayChange([1, 1, 1]))
print(arrayChange([3, 2, 4]))
print(arrayChange([1, 1, 2]))
