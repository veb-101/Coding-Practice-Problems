# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
'''
Some people are standing in a row in a park. There are trees between them which
cannot be moved. Your task is to rearrange the people by their heights in a
non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''


def sortByHeight(a):
    l1 = sorted([x for x in a if x != -1])
    for i, j in enumerate(a):
        if j == -1:
            l1.insert(i, j)
    return(l1)


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
print(sortByHeight([-1, -1, -1, -1, -1]))
print(sortByHeight([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]))
