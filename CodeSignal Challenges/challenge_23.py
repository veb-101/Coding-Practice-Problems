# https://app.codesignal.com/challenge/3yXnrkrRohrQ2av8E
'''
Return the value of prefix function for a given string.

Example

For s = "acacbab", the output should be
prefixFunctionNaive(s) = [0, 0, 1, 2, 0, 1, 0].
'''

# https://stackoverflow.com/questions/13792118/kmp-prefix-table
# http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/


def prefixFunctionNaive_mine(pattern):
    prefix_table = [0]
    i = 1
    while i < len(pattern):
        j = prefix_table[i - 1]
        while(j > 0 and pattern[j] != pattern[i]):
            j = prefix_table[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix_table.append(j)
        i += 1
    return prefix_table


def prefixFunctionNaive2(s):
    p, q = '', []
    for c in s:
        p += c
        i = l = 0
        for _ in p:
            if p[:i] == p[-i:]:
                l = i
            i += 1
        q += l,
    return q


def prefixFunctionNaive_better(pattern):
    current, result = -1, []
    for x in pattern:
        # print(x == pattern[current], pattern.index(pattern[current]))
        current += (-current, 1)[x == pattern[current]]
        result.append(current)
        # print()
    return result


print(prefixFunctionNaive_better("acacbab"))
