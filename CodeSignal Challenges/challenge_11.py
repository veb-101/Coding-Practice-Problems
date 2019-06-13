# https://app.codesignal.com/challenge/gnc8fMQSsxshLj9BY
'''
In this problem, the product of the elements of an arbitrary array x is
expressed as p(x).You are given an array of integers a. Any array that you can
obtain from a by removing some elements (possibly none, but not all) is denoted
as s. Among all such arrays s, what is the maximum possible value of p(s)? Since
the answer could potentially be very large, return the value of p(a) / p(s)
instead.

Example

For a = [1, 2, -2, -3, 3, 5], the output should be
maximumSubsetProduct(a) = 1.

Consider s = a (no elements were removed from the original array):
p(s) = 1 · 2 · (-2) · (-3) · 3 · 5 = 180. There is no other s that has elements
with a product larger than that. In this case, p(a) = p(s),
therefore p(a) / p(s) = 1.

For a = [10, -10], the output should be
maximumSubsetProduct(a) = -10.

p(a) = -100. For s = [10], p(s) = 10. p(s) cannot be any larger.
Thus, the answer is p(a) / p(s) = -100 / 10 = -10.
'''


def maximumSubsetProduct(arr):
    c = sum([1 for i in arr if i < 0])
    if c % 2 == 0 or len(arr) == 1:
        return 1
    else:
        return max([i for i in arr if i < 0])


def maximumSubsetProduct(arr):
    q = [x for x in a if x < 0]
    return ~len(a[1:] and q) % 2 or max(q)


a = [
    [1, 2, -2, -3, 3, 5],
    [10, -10],
    [1, -1, -1, 1],
    [3, 2, 1, 5, 10],
    [-1, -1, 2, 3, 4, 5],
    [-4, -2, 10, 20, -3],
    [-1],
    [1000000000, -1000000000]
]

for i in a:
    print(i, "Ans:",  maximumSubsetProduct(i))
    print()
