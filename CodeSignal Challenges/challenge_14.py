# https://app.codesignal.com/challenge/EmRRenvtbS4x5i2ud
'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

import re


def commonCharacterCount(a, b):
    return sum([min(a.count(i), b.count(i)) for i in set(a)])


def commonCharacterCount(a, b):
    i = 0
    for e in a:
        b, j = re.subn(e, "", b, 1)
        i += j
    return i


print(commonCharacterCount("aabcacs", "aca"))
