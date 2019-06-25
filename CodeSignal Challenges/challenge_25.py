# https: // app.codesignal.com/challenge/jmv55DMT7ywJaPcsC
'''
You find yourself in Bananaland trying to buy a banana. You are super rich so you
have an unlimited supply of banana-coins, but you are trying to use as few coins
as possible.

The coin values available in Bananaland are stored in a sorted array coins.
coins[0] = 1, and for each i (0 < i < coins.length) coins[i] is divisible by
coins[i - 1]. Find the minimal number of banana-coins you'll have to spend to
buy a banana given the banana's price.

Example

For coins = [1, 2, 10] and price = 28, the output should be
minimalNumberOfCoins(coins, price) = 6.

You have to use 10 twice, and 2 four times.
'''


def minimalNumberOfCoins(coins, price):
    result = 0
    i = len(coins) - 1
    while i > 0:
        result += price // coins[i]
        price %= coins[i]
        i -= 1
    return result


def minimalNumberOfCoins(coins, price):
    result = 0
    while price:
        *coins, last = coins
        result += price//last
        price %= last
    return result


coins = [1, 3, 6, 30]
price = 45

coins = [1, 2, 10]
price = 28
print(minimalNumberOfCoins(coins, price))
