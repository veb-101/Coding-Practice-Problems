# https: // app.codesignal.com / arcade / intro / level - 1 / s5PbmwxfECC52PWyQ
'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''


def checkPalindrome(inputString):
    return inputString[::-1] == inputString


print(checkPalindrome("abba"))
print(checkPalindrome("radar"))
print(checkPalindrome("abab"))
