import sys

input = sys.stdin.readline

N,K = map(int,input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1,N+1):
    W,V = map(int,input().split())
    for k in range(0,K+1):
        if k >= W:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-W] + V)
        else:
            dp[n][k] = dp[n-1][k]
print(dp[N][K])