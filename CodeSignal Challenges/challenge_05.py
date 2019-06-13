# https://app.codesignal.com/challenge/E9FdTL6H2qa2bBjJp
'''
Given a rectangular matrix of integers and integers n and m,
 we are looking for the submatrix of size n × m that has the
 maximal sum among all submatrices of the given size.

For Example

matrix = [[1, 12, 11, 10],
          [4,  3,  2,  9],
          [5,  6,  7,  8]]
n = 2, and
m = 1,
the output should be
maxSubmatrixSum(matrix, n, m) = 19.
'''


def maxSubmatrixSum_mine(matrix, n, m):
    values = []
    for row in range(len(matrix) - n + 1):
        for col in range(len(matrix[0]) - m + 1):
            total = 0
            for r in range(n):
                for c in range(m):
                    total += matrix[row+r][col+c]
            values.append(total)
    return max(values)


# import sys
# def maxSubmatrixSum(matrix, n, m):
#     reference = -sys.maxsize
#     for row in range(len(matrix) - n + 1):  # 0, 1
#         print(f"row: {row}")
#         for column in range(len(matrix[0]) - m + 1):  # 0, 1, 2, 3
#             print(f"col: {column}")
#             summation = 0
#             for x in range(n):  # 0, 1
#                 print(f"x:{x}")
#                 for y in range(m):  # 0
#                     print(f"y:{y}")
#                     print(f"matrix[{row+x}][{column + y}]: {matrix[row + x][column + y]}")
#                     summation += matrix[row + x][column + y]
#                     print(f"summation: {summation}")
#                 print()
#             reference = max(summation, reference)
#             print(f"reference: {reference}")
#         print()
#     return reference


# import scipy.signal as S
# def maxSubmatrixSum(matrix, n, m):
#     kernel = [[1]*m]*n
#     for i in range(len(kernel)):
#         for j in range(len(kernel[0])):
#             print(kernel[i][j], end=" ")
#         print()
#     # matrix, kernel,mode
#     return S.convolve2d(matrix, kernel, "valid").max()
matrix = [[1, 2, -1],
          [-4, -8, 3]]
n = 2
m = 2
print(maxSubmatrixSum_mine(matrix, n, m))

matrix = [[1, 12, 11, 10],
          [4, 3, 2, 9],
          [5, 6, 7, 8]]
n = 2
m = 1

print(maxSubmatrixSum_mine(matrix, n, m))
