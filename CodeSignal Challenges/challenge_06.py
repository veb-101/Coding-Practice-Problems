# https://app.codesignal.com/challenge/i7AAfRDur9TybJQ2P
'''
Given integers l and r, and a polynomial f(x) = P[0] + P[1] * x + P[2] * x2 + ...,
find the value of definite integral of f(x) over the interval [l, r].

Example
For l = -1, r = 2, and p = [0, 0, 0, 1], the output should be
computeDefiniteIntegral(l, r, p) = 3.75.
f(x) = x^3, so its indefinite integral is x^4/4.
Thus, the answer is 24/4 - (-1)4/4 = 3.75.
'''


def computeDefiniteIntegral(l, r, p):
    summation = 0
    index = 0
    for i in p:
        index += 1
        summation += (r ** index - l ** index) * i / index
    return summation


l = 1
r = 3
p = [1, 0, 0, 4]

print(computeDefiniteIntegral(l, r, p))
