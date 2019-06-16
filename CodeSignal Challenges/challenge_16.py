# https://app.codesignal.com/challenge/wLCaREGyjbocrdBDA
'''
Given a set of complex values, find their product.

Example

For real = [1, 2] and imag = [1, 3], the output should be
arrayComplexElementsProduct(real, imag) = [-1, 5].
The task is to calculate product of 1 + 1 * i and 2 + 3 * i, so the answer is
(1 + 1i) * (2 + 3i) = -1 + 5i.
'''


def arrayComplexElementsProduct(r, i):
    t = 1 + 0j
    for x, y in zip(r, i):
        t *= complex(x, y)
    return t.real, t.imag


def arrayComplexElementsProduct(r, i):
    t = 1
    for x, y in zip(r, i):
        t *= x + y*1j
    return t.real, t.imag


# real = [1, 2]
# imag = [1, 3]
real = [1, 2, 3]
imag = [0, 0, 0]

print(arrayComplexElementsProduct(real, imag))
