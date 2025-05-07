def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(fact(10))


def fact2(num):
    if num < 2:
        return 1
    return fact(num - 1)


print(fact(10))

# Update
