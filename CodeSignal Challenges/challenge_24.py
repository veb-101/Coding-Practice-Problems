# https://app.codesignal.com/challenge/2w6tp2Lxk6T5QzZxq?solutionId=df2vCF9K63Zp78YHS
'''
Ratiorg got statues of different sizes as a present from CodeMaster for his
birthday, each statue having an non-negative integer size. Since he likes to
make things perfect, he wants to arrange them from smallest to largest so that
each statue will be bigger than the previous one exactly by 1. He may need some
additional statues to be able to accomplish that. Help him figure out the minimum
number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''

import numpy as np


def makeArrayConsecutive2(s):
    return -~max(s) - min(s) - len(s)


def makeArrayConsecutive2(s):
    return np.ptp(s) - len(s) + 1


print(makeArrayConsecutive2([2, 6, 3, 8]))
print(makeArrayConsecutive2([0, 2, 100]))
