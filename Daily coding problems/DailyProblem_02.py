from functools import reduce
# import operator


def multiplySumExceptCurrent(a):
    values = []
    for x in range(len(a)):
        # total = functools.reduce(operator.mul, a)
        total = reduce(lambda a, b: a * b, a)
        total /= a[x]
        values.append(int(total))
    return values


# inputs = [1, 2, 3, 4, 5]
inputs = [3, 2, 1]
print(multiplySumExceptCurrent(inputs))
