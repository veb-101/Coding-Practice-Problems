def alphabetSubsequence(s):
    return [*s] == sorted({*s})


def alphabetSubsequence(s):
    p = ''
    for x in s:
        if x <= p:
            return 0
        p = x
    return 1


def alphabetSubsequence(s):
    # m = ord('a')-1
    m = 96
    for i in s:
        if ord(i) <= m:
            return 0
        m = max(m, ord(i))
    return 1


def alphabetSubsequence(s):
    return all([not i >= j for i, j in zip(s, s[1:])])


strings = ["effg", "cdce", "ace", "bxz", "cdefghijkxyzz", "qa", "fkyz", "xz",
           "pfyz", "fz"]

for i in strings:
    print(f"{i} -> {alphabetSubsequence(i)}")
