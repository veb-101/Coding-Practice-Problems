# https://app.codesignal.com/challenge/YZkenvHqAjS9fh7HM?solutionId=kq6hF24Z4jGFTkx8k

'''
Given an array of integers, count the odd numbers before the
first (i.e. leftmost) occurrence of zero.

Example

For sequence = [1, 2, 3, 0, 4, 5, 6, 0, 1], the output should be
oddNumbersBeforeZero(sequence) = 2.
'''


def oddNumbersBeforeZero(s):
    return len([1 for i in s[:s.index(0)] if i % 2])
