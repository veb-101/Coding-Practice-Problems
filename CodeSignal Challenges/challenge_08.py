# https://app.codesignal.com/challenge/Y4m8j4dDxFSxyuDjh
'''
Given an array of strings, sort them in the order of increasing lengths. If two
strings have the same length, their relative order must be the same as in the
initial array.

Example
For
inputArray = ["abc", "", "aaa", "a", "zz"]
the output should be

sortByLength(inputArray) = ["", "a", "zz", "abc", "aaa"]
'''


def sortByLength(inputArray):
    return sorted(inputArray, key=len)


inputArray = [["abc", "", "aaa", "a", "zz"],
              ["zz", "", "bb", "ccc", "cc"],
              ["abc", "e", "abcd"],
              ["a", "c", "a", "a"],
              ["thitl", "", "sadhxirg", "hx", "ondyxds", "kncor", "sqrg", "hqtchyxku", "rl", "wd"]
              ]
# sortByLength(inputArray)

for i, j in enumerate(inputArray, 1):
    print(f"Test {i}: Ans: {sortByLength(j)}")
