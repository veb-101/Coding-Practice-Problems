def numbersPresent(a, sum):
    for x in a:
        for y in a:
            if x + y == sum:
                return True
    return False


a = [10, 15, 3, 7]
sum = 18
print(numbersPresent(a, sum))
