# https://app.codesignal.com/challenge/GZdTPCPGovsDsFK7A
'''
An integer number (0<=number<=1e9) is raised to an integer power (0<=power<=1e9)
What will be the last digit of the result?

Example:

number=2, power=2: 2^2=4, so the answer is 4;
number=5, power=3: 5^3=125, so the answer is 5;
number=2019, power=1: 2019^1=2019, so the answer is 9.
Of course, we can't allow to raise 0 into 0 power (0^0 -> 1/0, which is
strictly prohibited!), so in this case please return -1.
'''


def powerTail(n, p):
    return pow(n, p, 10) if n > 0 else -1


def PowerTail(n, p):
    return -0**n or pow(n, p, 10)


print(powerTail(128, 28))
