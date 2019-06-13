# https://app.codesignal.com/arcade/code-arcade/intro-gates/DdNKFA3XCX6XN7bNz/solutions
'''
n children have got m pieces of candy. They want to eat as much candy as they
can, but each child must eat exactly the same amount of candy as any other child.
Determine how many pieces of candy will be eaten by all the children together.
Individual pieces of candy cannot be split.

Example

For n = 3 and m = 10, the output should be
candies(n, m) = 9.

Each child will eat 3 pieces. So the answer is 9.
'''


def candies(n, m):
    return m//n * n

# def candies(n, m):
#     return m - m % n


alist = [[3, 10], [1, 2], [10, 5], [4, 4], [4, 15], [9, 100],
         [8, 2], [3, 3], [7, 10], [3, 23]]


for i, j in alist:
    print("candies eaten equally:", candies(i, j))
