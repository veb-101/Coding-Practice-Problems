# https: // app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example
picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

'''


def addBorder(picture):
    myList = []
    for i in picture:
        i = "*" + i + "*"
        myList.append(i)
    x = len(myList[0])
    myList.insert(0, "*" * x)
    y = len(myList)
    myList.insert(y, "*" * x)
    return myList

# def addBorder(picture):
#     l=len(picture[0])+2
#     return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]


picture = ["abc",
           "ded"]

print(addBorder(picture))
