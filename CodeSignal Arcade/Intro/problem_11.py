# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
'''
Ticket numbers usually consist of an even number of digits. A ticket number is
considered lucky if the sum of the first half of the digits is equal to the sum
of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''


def isLucky(n):
    digits = [int(x) for x in str(n)]
    firstpart = sum(digits[:len(digits) // 2])
    secondpart = sum(digits[len(digits) // 2:])
    return firstpart == secondpart


print(isLucky(2130))
print(isLucky(2134))
