# https://app.codesignal.com/challenge/zA4ckXkvYQQ8Zitys
'''
You are given a positive integer x and you should perform n operations, where on the ith operation you increase x in such a way that its new value is divisible by i (operations are numbered from 1 to n).

Find the minimal value of x you can obtain by performing n operations described above.

Example

For x = 9 and n = 5, the output should be
increasingNumber(x, n) = 15.

Example:
1: 9+0=9 (9%1=0)
2: 9+1=10 (10%2=0)
3: 10+2=12 (12%3=0)
4: 12+0=12 (12%4=0)
5: 12+3=15 (15%5=0)
'''


# short and preferable
# https://math.stackexchange.com/a/519856/446524
# https://www.quora.com/What-should-be-added-to-4057-to-make-it-divisible-by-9
# complexity: O(n)

def makeDivisible(n, d):
    return -n % d


# print(makeDivisible(14, 3))

def increasingNumber(x, n):
    i = 0
    while i < n:
        i += 1
        x += -x % i
    return x


# for i in range(1, n+1):
#     x += -x % i
# return x


print(increasingNumber(9, 5))
print(increasingNumber(1, 100))
print(increasingNumber(4, 5))

# long method

# increases complexity to : O(n^2)


def increasingNumber(x, n):
    for i in range(1, n + 1):
        for j in range(i + 1):
            x += j
            if x % i == 0:
                break
            else:
                x -= j
    return x
