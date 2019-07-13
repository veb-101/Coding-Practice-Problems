# https://app.codesignal.com/challenge/TWCeD2Wrmgz7T5ZoE?solutionId=mMhP5mTSXmYNToFoa
'''
As seen in movies, ransom holders do not send out the note with instructions and
details with their own handwriting, fearing that they will be identified.
Instead, they cut up magazine headlines and titles and use them to assemble sentences.

Your job is to write a program that detects whether you have enough magazine
letters to create a ransom notes. Given an arbitrary ransom note string and
another string containing magazine letters, write a function that will return
the missing letters required to form the ransom note string from the magazine
letters if there are any. Each letter in the magazine string can only be used
once in your ransom note.

Ignore whitespace and return the missing letters sorted by keyCode.
'''


def missingLetters(ransomNote, magazineLetters):
    [*a], b = ransomNote, magazineLetters
    [a.remove(i) for i in b if i in a]
    return ''.join(sorted(a)).strip(' ')


ransomNote = "abcde"
magazineLetters = "abcef"
print(missingLetters(ransomNote, magazineLetters))


ransomNote = "pay up pal!"
magazineLetters: "apples are pretty lucky."
print(missingLetters(ransomNote, magazineLetters))


ransomNote = "zzz missing letters in the ransom note?"
magazineLetters = "The Fitnesskilogram Pacer Test is a multistage aerobic capacity test."
print(missingLetters(ransomNote, magazineLetters))
