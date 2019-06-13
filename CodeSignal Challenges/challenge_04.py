# https://app.codesignal.com/challenge/wBBHdf8aSNd4q9ECZ

'''
Given a string, return its encoding defined as follows:
First, the string is divided into the least possible number of disjoint
 substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a
concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order
and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
'''


def lineEncoding(s):
    chars = []
    i = 0
    s = s + " "
    while i != len(s) - 1:
        same = []
        for j in range(i, len(s)):
            if s[i] == s[j]:
                same.append(s[j])
            if s[i] != s[j]:
                i += len(same)
                chars.append([len(same), same[0]])
                break
    string = []
    for i in chars:
        if i[0] > 1:
            string.append(str(i[0]))
        string.append(i[1])
    return "".join(string)


s = ["aabbbc", "abbcabb", "abcd", "zzzz", "wwwwwwwawwwwwww", "ccccccccccccccc",
     "qwertyuioplkjhg", "ssiiggkooo", "adfaaa", "bbjaadlkjdl"]


for i, j in enumerate(s, 1):
    print(f"Test {i} -> {j}: Ans -> {lineEncoding(j)}")
    print()
s
