import sys

input = sys.stdin.readline
inf = int(1e9)

N = int(input())
D = []
for _ in range(N):
    D.append(list(map(int, input().split())))

dp = [inf for _ in range(1<<N)]
dp[0] = 0

for mask in range(1<<N):
    alloc_job = bin(mask).count('1')
    for j in range(N):
        if not (mask & (1<<j)):
            dp[mask | (1<<j)] = min(dp[mask | (1<<j)], dp[mask] + D[alloc_job][j])

print(dp)