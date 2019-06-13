# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''


def palindromeRearranging(inputString):
    return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1


print(palindromeRearranging("abbccba"))
print(palindromeRearranging("abbcc"))
print(palindromeRearranging("abbc"))
print(palindromeRearranging("abbccccf"))
print(palindromeRearranging("aabbccccf"))
