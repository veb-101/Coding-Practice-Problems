# https://app.codesignal.com/challenge/Fucm34ZryB8EBKbJP

'''
Given a string, find the shortest possible string which
can be achieved by adding characters to the end of initial
string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''


def buildPalindrome(st):
    c = []
    s = st[:]
    while not check(st):
        c.append(st[0])
        st = st[1:]
    return s + "".join(reversed(c))


def check(s):
    if list(s) == list(reversed(s)):
        return True
    return False


st = ["abcdc", "ababab", "abba", "abaa", "aaaaba", "abc",
      "kebab", "abccba", "abcabc", "cbdbedffcg", "euotmn"]

for i, j in enumerate(st, 1):
    print(f"Test {i} -> {j}: Ans -> {buildPalindrome(j)}")
    print()
