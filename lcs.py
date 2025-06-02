# Brute force approach
s1 = "RAMESH"
s2 = "SURESH"


def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs(s1, s2, m - 1, n - 1)
    else:
        return max(lcs(s1, s2, m - 1, n), lcs(s1, s2, m, n - 1))


m = len(s1)
n = len(s2)
ans = lcs(s1, s2, m, n)
print(ans)

# Memoization DP approach
s1 = "RAMESH"
s2 = "SURESH"


def lcs2(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if memo[m][n] != -1:
        return memo[m][n]
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = 1 + lcs2(s1, s2, m - 1, n - 1, memo)
        return memo[m][n]
    else:
        memo[m][n] = max(lcs2(s1, s2, m - 1, n, memo), lcs2(s1, s2, m, n - 1, memo))
        return memo[m][n]


m = len(s1)
n = len(s2)
memo = [[-1 for i in range(n + 1)] for _ in range(m + 1)]
ans = lcs2(s1, s2, m, n, memo)
print(ans)


def minCoinsRecur(i, sum, coins):
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float("inf")
    take = float("inf")
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins)
        if take != float("inf"):
            take += 1
    noTake = minCoinsRecur(i + 1, sum, coins)
    return min(take, noTake)


coins = [9, 6, 5, 1]
sum = 19
ans = minCoinsRecur(0, sum, coins)
print(ans if ans != float("inf") else -1)
