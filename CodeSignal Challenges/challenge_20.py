# https://app.codesignal.com/challenge/TuHac4M5746kwqTaH
'''
Given an array of integers, find the product of its elements.

Example
For inputArray = [1, 3, 2, 10], the output should be
arrayElementsProduct(inputArray) = 60.
'''


import numpy as np


def arrayElementsProduct(inputArray):
    product = 1
    for i in inputArray:
        product *= i
    return product


print(arrayElementsProduct([1, 2, 3, 10]))


def arrayElementsProduct(inputArray):
    return np.prod(inputArray)


print(arrayElementsProduct([1, 2, 3, 10]))
