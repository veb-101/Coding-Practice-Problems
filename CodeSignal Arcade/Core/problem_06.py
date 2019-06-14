# https://app.codesignal.com/arcade/code-arcade/intro-gates/vExYvcGnFsEYSt8nQ
'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a
way that the distance between any two neighboring numbers is equal (note that 0
and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially
opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
'''


def circleOfNumbers(n, firstNumber):
    return (firstNumber + (n // 2)) % n


print(circleOfNumbers(10, 2))
print(circleOfNumbers(10, 7))
print(circleOfNumbers(4, 1))
print(circleOfNumbers(6, 3))
print(circleOfNumbers(18, 6))
print(circleOfNumbers(12, 10))
print(circleOfNumbers(18, 5))
