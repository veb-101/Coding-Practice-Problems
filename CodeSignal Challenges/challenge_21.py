# https://app.codesignal.com/challenge/rApnerc87hMTtXB3a
'''
The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to swap its longest diagonals by exchanging
their elements at the corresponding positions.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
the output should be

swapDiagonals(matrix) = [[3, 2, 1],
                         [4, 5, 6],
                         [9, 8, 7]]
'''


def swapDiagonals(matrix):
    N = len(matrix)
    for i in range(N):

        matrix[i][i], matrix[i][N - i - 1] = \
            matrix[i][N - i - 1], matrix[i][i]

    return matrix


def swapDiagonals(matrix):
    i = 0
    for e in matrix:
        e[i], e[~i] = e[~i], e[i]
        i += 1
    return matrix


matrix = [
    [[1, 10],
     [100, 1000]],

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[239]],

    [[43, 455, 32, 103],
     [102, 988, 298, 981],
     [309, 21, 53, 64],
     [2, 22, 35, 291]],

    [[34, 1000, 139, 248, 972, 584],
     [98, 1, 398, 128, 762, 654],
     [33, 498, 132, 543, 764, 43],
     [329, 12, 54, 764, 666, 213],
     [928, 109, 489, 71, 837, 332],
     [93, 298, 42, 53, 76, 43]],

    [[1, 2],
     [1, 2]]]

for i in matrix:
    mat = swapDiagonals(i)
    for j in mat:
        print(j)
    print()
