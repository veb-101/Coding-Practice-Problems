# https://app.codesignal.com/challenge/3rokc7xtdSQoZBJBv

'''
Concatenate given strings using a specific separator.

Example

For strings = ["Code", "Fight", "On", "!"] and separator = "/", the output should be
myConcat(strings, separator) = "Code/Fight/On/!/".
'''
def myConcat(strings, separator):
    return separator.join(strings) + separator


def myConcat(a, b):
    return b.join(a)+b


strings = ["Code",
           "Fight",
           "On",
           "!"]

separator = "/"


print(myConcat(strings, separator))
