def cantor(n):
    if dp[n]:
        return dp[n]
    prev = cantor(n-1)
    dp[n] = prev+" "*len(prev)+prev
    return dp[n]

dp = [False for _ in range(13)]
dp[0] = "-"

while True:
    try:
        n = int(input())
        print(cantor(n))
    except EOFError:
        break