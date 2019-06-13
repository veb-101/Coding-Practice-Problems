# https: // app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
''''
You are given an array of integers representing coordinates of obstacles situated
on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. You
are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
'''


def avoidObstacles(a):
    a = sorted(a)
    rem = [x for x in range(min(a), max(a) + 2) if x not in a]
    for i in rem:
        if i * 2 not in a:
            if i > 9 and i % 9 not in a:
                return i % 9

            else:
                return i


print(avoidObstacles([5, 3, 6, 7, 9]))
print(avoidObstacles([1, 4, 10, 6, 2]))
print(avoidObstacles([19, 32, 11, 23]))
