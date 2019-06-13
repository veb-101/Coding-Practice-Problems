# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
'''
Given an array of strings, return another array containing all of its
longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''


def allLongestStrings(inputArray):
    x = len(max(inputArray, key=len))
    return [i for i in inputArray if len(i) == x]


print(allLongestStrings(["aba", "vcd", "aba"]))

inputArray = ["abc", "eeee", "abcd", "dcd"]
print(allLongestStrings(inputArray))

inputArray = ["abacaba", "abacab", "abac", "xxxxxx"]
print(allLongestStrings(inputArray))
