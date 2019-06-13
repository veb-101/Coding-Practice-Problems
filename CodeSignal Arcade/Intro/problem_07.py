# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG/solutions
'''
Given a sequence of integers as an array, determine whether it is possible to
obtain a strictly increasing sequence by removing no more than one element from
the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if
a0 < a1 < ... < an. Sequence containing only one element is also considered to
be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a
strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2].
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
'''


def first_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1


def almostIncreasingSequence(sequence):

    j = first_bad_pair(sequence)
    if j == -1:
        return True
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False


print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([1, 4, 2, 6, 1, 7]))
print(almostIncreasingSequence([1, 3, 2]))
