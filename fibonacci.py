num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end="\n")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end="\n")

print()


# DP for fibonacci
def fib(num):
    dp = [0] * (num + 1)
    dp[1] = 1
    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[num]


print(fib(10))


# DP for climbing stairs
def strairs(num):
    dp = [0] * (num + 1)
    dp[0] = dp[1] = 1
    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[num]


print(strairs(10))


def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


# Example usage:
for num in fib(5):
    print(num)
