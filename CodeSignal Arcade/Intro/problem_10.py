# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
'''


# def commonCharacterCount(s1, s2):
#     char_1 = list(s1)
#     char_2 = list(s2)
#     count = 0
#     listOfChars = []
#
#     for x in range(len(char_1)):
#         for y in range(len(char_2)):
#             if char_1[x] == char_2[y]:
#                 count += 1
#                 char_2.pop(y)
#                 break
#     return count


def commonCharacterCount(s1, s2):
    com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(com)


print(commonCharacterCount("aabba", "adcaa"))
print(commonCharacterCount("babel", "dabel"))
print(commonCharacterCount("carpet", "maark"))
